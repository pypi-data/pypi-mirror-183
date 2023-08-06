"""
A game object is a basic element describing a "thing" in rubato.
Its functionality is defined by the components it holds.
"""
from __future__ import annotations
from typing import Type, TypeVar

from . import Component
from ... import Game, Vector, DuplicateComponentError, Draw, ImplementationError, Camera, Color, Surface, Math

T = TypeVar("T", bound=Component)


# DEV comment: changes to arguments of Game Object should be reflected in rubato.wrap().
class GameObject:
    """
    An element describing a set of functionality grouped as a "thing", such as a player or a wall.

    Args:
        pos: The position of the game object. Defaults to (0, 0).
        rotation: The rotation of the game object. Defaults to 0.
        z_index: The z-index of the game object. Defaults to 0.
        ignore_cam: Whether the game object ignores the scene's camera when drawing or not. If set, all children will
            ignore the scene's camera. Defaults to False.
        parent: The parent of the game object. Defaults to None.
        name: The name of the game object. Defaults to "".
        debug: Whether to draw the center of the game object. Defaults to False.
        active: Whether the game object is active or not. Defaults to True.
        hidden: Whether the game object is hidden or not. Defaults to False.
    """

    def __init__(
        self,
        pos: Vector | tuple[float, float] = (0, 0),
        rotation: float = 0,
        z_index: int = 0,
        ignore_cam: bool = False,
        parent: GameObject | None = None,
        name: str = "",
        debug: bool = False,
        active: bool = True,
        hidden: bool = False,
    ):
        self.name: str = name
        """
        The name of the game object. Will default to: ""
        """
        self.pos: Vector = Vector.create(pos)
        """The current position of the game object."""
        self.ignore_cam: bool = ignore_cam
        """Whether the game object ignores the scene's camera when drawing or not."""
        self.debug: bool = debug
        """Whether to draw a debug crosshair for the game object."""
        self.z_index: int = z_index
        """The z_index of the game object."""
        self.rotation: float = rotation
        """The rotation of the game object in degrees."""
        self.hidden: bool = hidden
        """Whether the game object is hidden (not drawn)."""
        self.active: bool = active
        """Whether the game object should update and draw."""

        self._parent: GameObject | None = None
        self.parent = parent
        self._children: list[GameObject] = []
        self._components: dict[type, list[Component]] = {}
        self._debug_cross: Surface = Surface(10, 10)
        self._debug_cross.draw_line(Vector(0, 5), Vector(0, -5), Color.debug, thickness=2)  # vertical line
        self._debug_cross.draw_line(Vector(-5, 0), Vector(5, 0), Color.debug, thickness=2)  # horizontal line

    @property
    def parent(self) -> GameObject | None:
        """The parent of the game object."""
        return self._parent

    @parent.setter
    def parent(self, parent: GameObject | None):
        """Sets the parent of the game object."""
        if self._parent:
            self._parent._children.remove(self)
        self._parent = parent
        if self._parent:
            self._parent._children.append(self)

    def true_z(self) -> int:
        """
        The true z-index of the game object.

        Returns:
            int: The true z-index of the game object.
        """
        if self.parent:
            return self.z_index + self.parent.true_z()
        return self.z_index

    def true_pos(self) -> Vector:
        """
        The position of the game object relative to the scene.

        Returns:
            Vector: The true position of the game object.
        """
        if self.parent:
            return self.pos.rotate(self.parent.true_rotation()) + self.parent.true_pos()
        return self.pos

    def true_rotation(self) -> float:
        """
        The rotation of the game object relative to the scene.

        Returns:
            float: The true rotation of the game object.
        """
        if self.parent:
            return self.rotation + self.parent.true_rotation()
        return self.rotation

    def children(self) -> tuple[GameObject]:
        """
        The children of the game object. Note that this is an immutable tuple.

        Returns:
            The children of the game object.
        """
        return tuple(self._children)

    def add(self, *components: Component) -> GameObject:
        """
        Add a component to the game object.

        Args:
            components (Component): The component(s) to add.

        Raises:
            DuplicateComponentError: Raised when there is already a component of the same type in the game object.
                Note that this error is only raised if the component type's 'singular' attribute is True.

        Returns:
            GameObject: This GameObject.
        """
        for component in components:
            comp_type = type(component)

            try:
                if component.singular and comp_type in self._components:
                    raise DuplicateComponentError(
                        f"There is already a component of type '{comp_type}' in the game object '{self.name}'"
                    )
            except AttributeError as err:
                raise ImplementationError(
                    "The component does not have the attribute 'singular'. You most likely overrode the"
                    "__init__ method of the component without calling super().__init__()."
                ) from err

            if comp_type not in self._components:
                self._components[comp_type] = []
            self._components[comp_type].append(component)
            component.gameobj = self

        return self

    def remove(self, comp_type: Type[Component]):
        """
        Removes the first instance of a type of component from the game object.

        Args:
            comp_type: The type of the component to remove.

        Raises:
            IndexError: The component was not in the game object and nothing was removed.
        """
        for key, val in self._components.items():
            if issubclass(key, comp_type):
                del val[0]
                if not val:
                    del val
                return
        raise IndexError(f"There are no components of type '{comp_type}' in game object '{self.name}'.")

    def remove_by_ref(self, component: Component) -> bool:
        """
        Removes a component from the game object.

        Args:
            component: The component to remove.

        Returns:
            Whether the component was removed.
        """
        for key, val in self._components.items():
            if issubclass(key, type(component)):
                if component in val:
                    val.remove(component)
                    return True
        return False

    def remove_all(self, comp_type: Type[Component]):
        """
        Removes all components of a type from the game object.

        Args:
            comp_type: The type of the component to remove.

        Raises:
            IndexError: The components were not in the game object and nothing was removed.
        """
        deleted = False
        for key, val in self._components.items():
            if issubclass(key, comp_type):
                del val
                deleted = True
        if not deleted:
            raise IndexError(f"There are no components of type '{comp_type}' in game object '{self.name}'.")

    def get(self, comp_type: Type[T]) -> T:
        """
        Gets a component from the game object.

        Args:
            comp_type: The component type (such as `ParticleSystem`, or `Hitbox`).

        Raises:
            ValueError: There were no components of that type found.

        Returns:
            The first component of that type that the gameobject holds.
        """
        for key, val in self._components.items():
            if issubclass(key, comp_type):
                return val[0]  # type: ignore
        raise ValueError(f"There are no components of type '{comp_type}' in game object '{self.name}'.")

    def get_all(self, comp_type: Type[T]) -> list[T]:
        """
        Gets all the components of a type from the game object.

        Args:
            comp_type: The type of component to search for.

        Returns:
            A list containing all the components of that type. If no components were found, the
                list is empty.
        """
        fin = []
        for key, val in self._components.items():
            if issubclass(key, comp_type):
                fin.extend(val)
        return fin

    def _deep_get_all(self, comp_type: Type[T]) -> list[T]:
        """
        Gets all the components of a type from the game object and its children.

        Args:
            comp_type: The type of component to search for.

        Returns:
            A list containing all the components of that type. If no components were found, the
                list is empty.
        """
        fin = self.get_all(comp_type)
        for child in self._children:
            fin.extend(child._deep_get_all(comp_type))
        return fin

    def _update(self):
        if not self.active:
            return

        all_comps = list(self._components.values())
        for comps in all_comps:
            for comp in comps:
                comp._update()

        for child in self._children:
            child._update()

    def _fixed_update(self):
        if not self.active:
            return

        for comps in self._components.values():
            for comp in comps:
                comp._fixed_update()

        for child in self._children:
            child._fixed_update()

    def _draw(self, camera: Camera):
        if self.hidden or not self.active:
            return

        cam = Game._zero_cam if self.ignore_cam else camera

        for comps in self._components.values():
            for comp in comps:
                if not comp.hidden:
                    comp._draw(cam)

        for child in self._children:
            child._draw(cam)

        if self.debug or Game.debug:
            self._debug_cross.rotation = self.true_rotation()

            Draw.queue_surface(self._debug_cross, self.true_pos(), Math.INF, cam)

    def clone(self) -> GameObject:
        """
        Clones the game object.
        """
        new_obj = GameObject(
            pos=self.pos.clone(),
            rotation=self.rotation,
            z_index=self.z_index,
            ignore_cam=self.ignore_cam,
            parent=self.parent,
            name=f"{self.name}",
            debug=self.debug,
            active=self.active,
            hidden=self.hidden,
        )
        for component in self._components.values():
            for comp in component:
                new_obj.add(comp.clone())

        for child in self._children:
            child.clone().parent = new_obj

        return new_obj

    def __contains__(self, comp_type):
        for key in self._components:
            if issubclass(key, comp_type):
                return True
        return False

    def __repr__(self):
        return (
            f"GameObject(pos={self.pos}, rotation={self.rotation}, z_index={self.z_index}, ignore_cam={self.ignore_cam}"
            f", parent={self.parent}, name='{self.name}', debug={self.debug}, active={self.active}, "
            f"hidden={self.hidden})"
        )

    def __str__(self):
        return (
            f"<GameObject '{self.name}', with {len(self.get_all(Component))} components and {len(self._children)} "
            f"children at {hex(id(self))}>"
        )
