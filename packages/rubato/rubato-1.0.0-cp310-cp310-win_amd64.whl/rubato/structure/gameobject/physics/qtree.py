"""
QuadTree implementation to optimize collision detection as part of the physics engine.
"""
import Cython

from . import Hitbox, _Engine
from .... import Vector


# _QTree acts like a function, but keep it as a class for future optimization as well as Cython.cclass optimization.
@Cython.cclass
class _QTree:
    """The Quadtree itself."""

    def __init__(self, hbs: list[list[Hitbox]]):
        self.bbs: list[tuple[Vector, Vector]] = []

        tl: Vector = Vector.infinity()
        br: Vector = -1 * Vector.infinity()
        for gen in hbs:
            local_tl: Vector = Vector.infinity()
            local_br: Vector = -1 * Vector.infinity()
            for hb in gen:
                aabb: tuple[Vector, Vector] = hb.get_aabb()

                if aabb[0].x < local_tl.x:
                    if aabb[0].x < tl.x:
                        tl.x = local_tl.x = aabb[0].x
                    else:
                        local_tl.x = aabb[0].x
                if aabb[0].y < local_tl.y:
                    if aabb[0].y < tl.y:
                        tl.y = local_tl.y = aabb[0].y
                    else:
                        local_tl.y = aabb[0].y
                if aabb[1].x > local_br.x:
                    if aabb[1].x > br.x:
                        br.x = local_br.x = aabb[1].x
                    else:
                        local_br.x = aabb[1].x
                if aabb[1].y > local_br.y:
                    if aabb[1].y > br.y:
                        br.y = local_br.y = aabb[1].y
                    else:
                        local_br.y = aabb[1].y
            self.bbs.append((local_tl, local_br))

        self.stack: list[list[Hitbox]] = []

        center: Vector = (tl + br) / 2

        self.northeast: _STree = _STree(Vector(center.x, tl.y), Vector(br.x, center.y))
        self.northwest: _STree = _STree(tl, center)
        self.southeast: _STree = _STree(center, br)
        self.southwest: _STree = _STree(Vector(tl.x, center.y), Vector(center.x, br.y))

        for i in range(len(hbs)):
            bb: tuple[Vector, Vector] = self.bbs[i]
            hbg: list[Hitbox] = hbs[i]

            for hb in hbg:
                for li in self.stack:
                    for item in li:
                        _Engine.collide(hb, item)

            self.northeast.collide(hbg, bb)
            self.northwest.collide(hbg, bb)
            self.southeast.collide(hbg, bb)
            self.southwest.collide(hbg, bb)

            if not self.northeast.insert(hbg, bb) and not self.northwest.insert(hbg, bb) \
                and not self.southeast.insert(hbg, bb) and not self.southwest.insert(hbg, bb):
                self.stack.append(hbg)


@Cython.cclass
class _STree:
    """A Subtree."""

    def __init__(self, top_left: Vector, bottom_right: Vector):
        self.top_left: Vector = top_left
        self.bottom_right: Vector = bottom_right

        self.stack: list[list[Hitbox]] = []

        self.has_children: bool = False

        self.northeast: _STree
        self.northwest: _STree
        self.southeast: _STree
        self.southwest: _STree

    def insert(self, hbs: list[Hitbox], bb: tuple[Vector, Vector]) -> bool:
        if (bb[0].x < self.top_left.x) or (bb[0].y < self.top_left.y) \
            or (bb[1].x > self.bottom_right.x) or (bb[1].y > self.bottom_right.y):
            return False

        if not self.stack:
            self.stack.append(hbs)
            return True

        if not self.has_children:
            self.has_children = True
            center: Vector = (self.top_left + self.bottom_right) / 2
            self.northeast = _STree(Vector(center.x, self.top_left.y), Vector(self.bottom_right.x, center.y))
            self.northwest = _STree(self.top_left, center)
            self.southeast = _STree(center, self.bottom_right)
            self.southwest = _STree(Vector(self.top_left.x, center.y), Vector(center.x, self.bottom_right.y))

        if not self.northeast.insert(hbs, bb) and not self.northwest.insert(hbs, bb) \
            and not self.southeast.insert(hbs, bb) and not self.southwest.insert(hbs, bb):
            self.stack.append(hbs)

        return True

    def collide(self, hbs: list[Hitbox], bb: tuple[Vector, Vector]):
        if (bb[1].y < self.top_left.y) or (bb[1].x < self.top_left.x) \
            or (bb[0].y > self.bottom_right.y) or (bb[0].x > self.bottom_right.x):
            return

        for hb in hbs:
            for current in self.stack:
                for item in current:
                    _Engine.collide(hb, item)

        if self.has_children:
            self.northeast.collide(hbs, bb)
            self.northwest.collide(hbs, bb)
            self.southeast.collide(hbs, bb)
            self.southwest.collide(hbs, bb)
