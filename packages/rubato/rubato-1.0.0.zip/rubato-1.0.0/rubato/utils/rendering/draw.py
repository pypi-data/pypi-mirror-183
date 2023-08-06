"""A static class for drawing things directly to the window."""
from __future__ import annotations
from typing import Optional, Callable, TYPE_CHECKING
import cython, math

import sdl2, sdl2.ext

from . import Font, Surface
from .. import Vector, Color, Display, InitError, Math, Time

if TYPE_CHECKING:
    from . import Camera


@cython.cclass
class _DrawTask:
    priority: int = cython.declare(int, visibility="public")  # type: ignore
    func: Callable = cython.declare(object, visibility="public")  # type: ignore

    def __init__(self, priority: int, func: Callable):
        self.priority = priority
        self.func = func


# THIS IS A STATIC CLASS
class Draw:
    """A static class allowing drawing items to the window."""
    _queue: list[_DrawTask] = []

    _pt_surfs: dict[Color, Surface] = {}
    _line_surfs: dict[tuple, Surface] = {}
    _rect_surfs: dict[tuple, Surface] = {}
    _circle_surfs: dict[tuple, Surface] = {}
    _poly_surfs: dict[tuple, Surface] = {}

    def __init__(self) -> None:
        raise InitError(self)

    @staticmethod
    def _draw_fps(font: Font):
        """
        Draws the current FPS to the screen.
        Called automatically if `Game.show_fps` is True.

        Args:
            font: The font to use.
        """
        height: int = math.ceil(Display.res.y / 32)
        pad = max(height / 4, 1)

        scale = height / font.size

        Draw.text(
            str(Time.smooth_fps()),
            font=font,
            pos=Display.top_left + (pad, -pad),
            align=Vector(1, 1),
            justify="center",
            scale=(scale, scale),
            shadow=True,
            shadow_pad=(pad, pad),
            af=False
        )

    @classmethod
    def clear(cls, background_color: Color = Color.white, border_color: Color = Color.black):
        """
        Clears the screen and draws a background.

        Args:
            background_color: The background color. Defaults to white.
            border_color: The border color. Defaults to black.
                Shown when the aspect ratio of the game does not match the aspect ratio of the window.
        """
        Display.renderer.clear(border_color.to_tuple())
        Display.renderer.fill(
            (0, 0, *Display.renderer.logical_size),
            background_color.to_tuple(),
        )

    @classmethod
    def _push(cls, z_index: int, callback: Callable):
        """
        Add a custom draw function to the frame queue.

        Args:
            z_index: The z_index to call at (lower z_indexes get called first).
            callback: The function to call.
        """
        cls._queue.append(_DrawTask(z_index, callback))

    @classmethod
    def _dump(cls):
        """Draws all queued items. Is called automatically at the end of every frame."""
        if not cls._queue:
            return

        cls._queue.sort(key=lambda x: x.priority)

        for task in cls._queue:
            task.func()

        cls._queue.clear()

    @classmethod
    def queue_pixel(
        cls,
        pos: Vector | tuple[float, float],
        color: Color = Color.cyan,
        z_index: int = 0,
        camera: Camera | None = None
    ):
        """
        Draw a point onto the renderer at the end of the frame.

        Args:
            pos: The position of the point.
            color: The color to use for the pixel. Defaults to Color.cyan.
            z_index: Where to draw it in the drawing order. Defaults to 0.
            camera: The camera to use. Defaults to None.
        """
        if camera is not None and camera.z_index < z_index:
            return
        cls._push(z_index, lambda: cls.pixel(pos, color, camera))

    @classmethod
    def pixel(cls, pos: Vector | tuple[float, float], color: Color = Color.cyan, camera: Camera | None = None):
        """
        Draw a point onto the renderer immediately.

        Args:
            pos: The position of the point.
            color: The color to use for the pixel. Defaults to Color.cyan.
            camera: The camera to use. Defaults to None.
        """
        if (surf := cls._pt_surfs.get(color, None)) is None:
            surf = Surface(1, 1)
            surf.set_pixel((0, 0), color)
            cls._pt_surfs[color] = surf

        cls.surface(surf, pos, camera)

    @classmethod
    def queue_line(
        cls,
        p1: Vector | tuple[float, float],
        p2: Vector | tuple[float, float],
        color: Color = Color.cyan,
        width: int | float = 1,
        z_index: int = 0,
        camera: Camera | None = None
    ):
        """
        Draw a line onto the renderer at the end of the frame.

        Args:
            p1: The first point of the line.
            p2: The second point of the line.
            color: The color to use for the line. Defaults to Color.cyan.
            width: The width of the line. Defaults to 1.
            z_index: Where to draw it in the drawing order. Defaults to 0.
            camera: The camera to use. Defaults to None.
        """
        if camera is not None and camera.z_index < z_index:
            return
        cls._push(z_index, lambda: cls.line(p1, p2, color, width, camera))

    @staticmethod
    def line(
        p1: Vector | tuple[float, float],
        p2: Vector | tuple[float, float],
        color: Color = Color.cyan,
        width: int | float = 1,
        camera: Camera | None = None
    ):
        """
        Draw a line onto the renderer immediately.

        Args:
            p1: The first point of the line.
            p2: The second point of the line.
            color: The color to use for the line. Defaults to Color.cyan.
            width: The width of the line. Defaults to 1.
            camera: The camera to use. Defaults to None.
        """
        dims = Vector.create(p2) - p1
        hashing = dims, color, width

        if (surf := Draw._line_surfs.get(hashing, None)) is None:
            pad = round(width)
            sizex, sizey = abs(round(dims.x)), abs(round(dims.y))
            halfx, halfy = sizex / 2, sizey / 2
            surf = Surface(sizex + (2 * pad), sizey + (2 * pad))
            surf.draw_line(
                (halfx * Math.sign(-dims.x), halfy * Math.sign(-dims.y)),
                (halfx * Math.sign(dims.x), halfy * Math.sign(dims.y)),
                color,
                thickness=round(width),
            )
            Draw._line_surfs[hashing] = surf

        Draw.surface(surf, p1 + dims / 2 + round(width), camera)

    @classmethod
    def queue_rect(
        cls,
        center: Vector | tuple[float, float],
        width: int | float,
        height: int | float,
        border: Optional[Color] = Color.cyan,
        border_thickness: int | float = 1,
        fill: Optional[Color] = None,
        angle: float = 0,
        z_index: int = 0,
        camera: Camera | None = None
    ):
        """
        Draws a rectangle onto the renderer at the end of the frame.

        Args:
            center: The center of the rectangle.
            width: The width of the rectangle.
            height: The height of the rectangle.
            border: The border color. Defaults to Color.cyan.
            border_thickness: The border thickness. Defaults to 1.
            fill: The fill color. Defaults to None.
            angle: The angle in degrees. Defaults to 0.
            z_index: Where to draw it in the drawing order. Defaults to 0.
            camera: The camera to use. Defaults to None.
        """
        if camera is not None and camera.z_index < z_index:
            return
        cls._push(z_index, lambda: cls.rect(center, width, height, border, border_thickness, fill, angle, camera))

    @classmethod
    def rect(
        cls,
        center: Vector | tuple[float, float],
        width: int | float,
        height: int | float,
        border: Optional[Color] = Color.cyan,
        border_thickness: int | float = 1,
        fill: Optional[Color] = None,
        angle: float = 0,
        camera: Camera | None = None
    ):
        """
        Draws a rectangle onto the renderer immediately.

        Args:
            center: The center of the rectangle.
            width: The width of the rectangle.
            height: The height of the rectangle.
            border: The border color. Defaults to Color.cyan.
            border_thickness: The border thickness. Defaults to 1.
            fill: The fill color. Defaults to None.
            angle: The angle in degrees. Defaults to 0.
            camera: The camera to use. Defaults to None.

        Raises:
            ValueError: If the width and height are not positive.
        """
        hashing = width, height, border, border_thickness, fill

        if width <= 0 or height <= 0:
            raise ValueError("Width and height must be positive.")

        if (surf := cls._rect_surfs.get(hashing, None)) is None:
            pad = round(border_thickness) if border is not None else 0
            surf = Surface(pad + round(width), pad + round(height))
            surf.draw_rect((0, 0), (width, height), border, pad, fill)
            cls._rect_surfs[hashing] = surf

        surf.rotation = angle
        cls.surface(surf, center, camera)

    @classmethod
    def queue_circle(
        cls,
        center: Vector | tuple[float, float],
        radius: int = 4,
        border: Optional[Color] = Color.cyan,
        border_thickness: int | float = 1,
        fill: Optional[Color] = None,
        z_index: int = 0,
        camera: Camera | None = None
    ):
        """
        Draws a circle onto the renderer at the end of the frame.

        Args:
            center: The center.
            radius: The radius. Defaults to 4.
            border: The border color. Defaults to Color.cyan.
            border_thickness: The border thickness. Defaults to 1.
            fill: The fill color. Defaults to None.
            z_index: Where to draw it in the drawing order. Defaults to 0.
            camera: The camera to use. Defaults to None.
        """
        if camera is not None and camera.z_index < z_index:
            return
        cls._push(z_index, lambda: cls.circle(center, radius, border, border_thickness, fill, camera))

    @classmethod
    def circle(
        cls,
        center: Vector | tuple[float, float],
        radius: int | float = 4,
        border: Optional[Color] = Color.cyan,
        border_thickness: int | float = 1,
        fill: Optional[Color] = None,
        camera: Camera | None = None
    ):
        """
        Draws a circle onto the renderer immediately.

        Args:
            center: The center.
            radius: The radius. Defaults to 4.
            border: The border color. Defaults to Color.cyan.
            border_thickness: The border thickness. Defaults to 1.
            fill: The fill color. Defaults to None.
            camera: The camera to use. Defaults to None.

        Raises:
            ValueError: If the radius is not positive.
        """
        hashing = radius, border, border_thickness, fill

        if radius <= 0:
            raise ValueError("Radius must be positive.")

        if (surf := cls._circle_surfs.get(hashing, None)) is None:
            pad = round(border_thickness) if border is not None else 0
            surf = Surface(pad * 2 + round(radius * 2) + 1, pad * 2 + round(radius * 2) + 1)
            surf.draw_circle((0, 0), round(radius), border, round(border_thickness), fill)
            cls._circle_surfs[hashing] = surf

        cls.surface(surf, center, camera)

    @classmethod
    def queue_poly(
        cls,
        points: list[Vector] | list[tuple[float, float]],
        center: Vector | tuple[float, float],
        border: Optional[Color] = Color.cyan,
        border_thickness: int | float = 1,
        fill: Optional[Color] = None,
        z_index: int = 0,
        camera: Camera | None = None
    ):
        """
        Draws a polygon onto the renderer at the end of the frame.

        Args:
            points: The list of points to draw relative to the center.
            center: The center of the polygon.
            border: The border color. Defaults to Color.cyan.
            border_thickness: The border thickness. Defaults to 1.
            fill: The fill color. Defaults to None.
            z_index: Where to draw it in the drawing order. Defaults to 0.
            camera: The camera to use. Defaults to None.
        """
        if camera is not None and camera.z_index < z_index:
            return
        cls._push(z_index, lambda: cls.poly(points, center, border, border_thickness, fill, camera))

    @classmethod
    def poly(
        cls,
        points: list[Vector] | list[tuple[float, float]],
        center: Vector | tuple[float, float],
        border: Optional[Color] = Color.cyan,
        border_thickness: int | float = 1,
        fill: Optional[Color] = None,
        camera: Camera | None = None
    ):
        """
        Draws a polygon onto the renderer immediately.

        Args:
            points: The list of points to draw relative to the center.
            center: The center of the polygon.
            border: The border color. Defaults to Color.cyan.
            border_thickness: The border thickness. Defaults to 1.
            fill: The fill color. Defaults to None.
            camera: The camera to use. Defaults to None.
        """
        hashing = tuple(points), border, border_thickness, fill

        if (surf := cls._poly_surfs.get(hashing, None)) is None:
            min_x, min_y = Math.INF, Math.INF
            max_x, max_y = -Math.INF, -Math.INF
            for point in points:
                min_x = min(min_x, point[0])
                min_y = min(min_y, point[1])
                max_x = max(max_x, point[0])
                max_y = max(max_y, point[1])
            pad = round(border_thickness) if border is not None else 0
            surf = Surface(pad * 2 + round(max_x - min_x + 2), pad * 2 + round(max_y - min_y + 2))
            surf.draw_poly(points, (0, 0), border, round(border_thickness), fill)
            cls._poly_surfs[hashing] = surf

        cls.surface(surf, center, camera)

    @classmethod
    def queue_text(
        cls,
        text: str,
        font: Font,
        pos: Vector | tuple[float, float] = (0, 0),
        justify: str = "left",
        align: Vector | tuple[float, float] = (0, 0),
        width: int | float = 0,
        scale: Vector | tuple[float, float] = (1, 1),
        shadow: bool = False,
        shadow_pad: Vector | tuple[float, float] = (0, 0),
        af: bool = True,
        z_index: int = 0,
        camera: Camera | None = None
    ):
        """
        Draws some text onto the renderer at the end of the frame.

        Args:
            text: The text to draw.
            font: The Font object to use.
            pos: The top left corner of the text. Defaults to (0, 0).
            justify: The justification of the text. (left, center, right). Defaults to "left".
            align: The alignment of the text. Defaults to (0, 0).
            width: The maximum width of the text. Will automatically wrap the text. Defaults to -1.
            scale: The scale of the text. Defaults to (1, 1).
            shadow: Whether to draw a basic shadow box behind the text. Defaults to False.
            shadow_pad: What padding to use for the shadow. Defaults to (0, 0).
            af: Whether to use anisotropic filtering. Defaults to True.
            z_index: Where to draw it in the drawing order. Defaults to 0.
            camera: The camera to use. Defaults to None.
        """
        if camera is not None and camera.z_index < z_index:
            return
        cls._push(
            z_index, lambda: cls.text(text, font, pos, justify, align, width, scale, shadow, shadow_pad, af, camera)
        )

    @classmethod
    def text(
        cls,
        text: str,
        font: Font,
        pos: Vector | tuple[float, float] = (0, 0),
        justify: str = "left",
        align: Vector | tuple[float, float] = (0, 0),
        width: int | float = 0,
        scale: Vector | tuple[float, float] = (1, 1),
        shadow: bool = False,
        shadow_pad: Vector | tuple[float, float] = (0, 0),
        af: bool = True,
        camera: Camera | None = None
    ):
        """
        Draws some text onto the renderer immediately.

        Args:
            text: The text to draw.
            font: The Font object to use.
            pos: The top left corner of the text. Defaults to (0, 0).
            justify: The justification of the text. (left, center, right). Defaults to "left".
            align: The alignment of the text. Defaults to (0, 0).
            width: The maximum width of the text. Will automatically wrap the text. Defaults to -1.
            scale: The scale of the text. Defaults to (1, 1).
            shadow: Whether to draw a basic shadow box behind the text. Defaults to False.
            shadow_pad: What padding to use for the shadow. Defaults to (0, 0).
            af: Whether to use anisotropic filtering. Defaults to True.
            camera: The camera to use. Defaults to None.
        """
        shadow_pad = Vector.create(shadow_pad)

        if camera is not None:
            pos = camera.transform(pos)
            scale = camera.zoom * scale[0], camera.zoom * scale[1]
            shadow_pad = camera.zoom * shadow_pad

        surf = font._generate(text, justify, width)
        tx = Surface._from_surf(surf, scale=scale, af=af)
        sdl2.SDL_FreeSurface(surf)

        pad_x, pad_y = (shadow_pad / scale).tuple_int()

        if shadow:
            tx_dims = tx.width + 2 * pad_x, font.size + 2 * pad_y
            final_tx = Surface(*tx_dims, scale=scale)
            final_tx.fill(Color(a=200))
            final_tx.blit(
                tx,
                (0, 0, tx.width, font.size),
            )
        else:
            final_tx = tx

        size = final_tx.size_scaled()
        center = (
            pos[0] + (align[0] * size[0]) / 2,
            pos[1] - (align[1] * size[1]) / 2,
        )
        cls.surface(final_tx, center, camera)

    @classmethod
    def queue_surface(
        cls,
        surface: Surface,
        pos: Vector | tuple[float, float] = (0, 0),
        z_index: int = 0,
        camera: Camera | None = None
    ):
        """
        Draws an surface onto the renderer at the end of the frame.

        Args:
            surface: The surface to draw.
            pos: The position to draw the surface at. Defaults to (0, 0).
            z_index: The z-index of the surface. Defaults to 0.
            camera: The camera to use. Defaults to None.
        """
        if camera is not None and camera.z_index < z_index:
            return
        cls._push(z_index, lambda: cls.surface(surface, pos, camera))

    @classmethod
    def surface(cls, surface: Surface, pos: Vector | tuple[float, float] = (0, 0), camera: Camera | None = None):
        """
        Draws an surface onto the renderer immediately.

        Args:
            surface: The surface to draw.
            pos: The position to draw the surface at. Defaults to (0, 0).
            camera: The camera to use. Defaults to None.
        """
        if not surface.uptodate:
            surface._regen()

        if camera is not None:
            pos = camera.transform(pos)
            scale = camera.zoom * surface.scale
        else:
            scale = surface.scale

        Display._update(surface._tx, surface.width, surface.height, pos, scale, surface.rotation)

    @classmethod
    def clear_cache(cls):
        """
        Clears the draw cache.

        Generally, you shouldn't need to call this method, but it can help free up memory if you're running low;
        the true best way to avoid this though is to rely on surfaces for shapes that change/recolor often,
        and call the draw surface method directly instead of the draw shape methods.
        """
        cls._pt_surfs.clear()
        cls._line_surfs.clear()
        cls._rect_surfs.clear()
        cls._circle_surfs.clear()
        cls._poly_surfs.clear()

    @classmethod
    def _cache_size(cls):
        return len(cls._pt_surfs) + len(cls._line_surfs) + len(cls._rect_surfs) \
            + len(cls._circle_surfs) + len(cls._poly_surfs)
