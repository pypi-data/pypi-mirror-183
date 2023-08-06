"""
Static class that allows for intuitive window management.
"""
from __future__ import annotations

import ctypes

import sdl2, sdl2.ext, sdl2.sdlimage
import os

from .. import Vector, get_path, InitError, Math


class _DisplayProperties(type):  # pylint: disable=missing-class-docstring
    # pyright: reportGeneralTypeIssues=false

    @property
    def window_size(cls) -> Vector:
        return Vector(*cls.window.size)

    @window_size.setter
    def window_size(cls, new: Vector | tuple[float, float]):
        cls.window.size = (int(new[0]), int(new[1]))

    @property
    def res(cls) -> Vector:
        return Vector(*cls.renderer.logical_size)

    @res.setter
    def res(cls, new: Vector | tuple[float, float]):
        cls.renderer.logical_size = (int(new[0]), int(new[1]))
        cls._half_res = (new[0] / 2, new[1] / 2)

    @property
    def window_pos(cls) -> Vector:
        return Vector(*cls.window.position)

    @window_pos.setter
    def window_pos(cls, new: Vector | tuple[float, float]):
        cls.window.position = (int(new[0]), int(new[1]))

    @property
    def window_name(cls):
        return cls.window.title

    @window_name.setter
    def window_name(cls, new: str):
        cls.window.title = new


# THIS IS A STATIC CLASS
class Display(metaclass=_DisplayProperties):
    """
    A static class that houses all of the display information

    Attributes:
        window (sdl2.Window): The pysdl2 window element.
        renderer (sdl2.Renderer): The pysdl2 renderer element.
        format (sdl2.PixelFormat): The pysdl2 pixel format element.
        window_size (Vector): The pixel size of the physical window.

            Warning:
                Using this value to determine the placement of your game objects may
                lead to unexpected results. You should instead use
                :func:`Display.res <rubato.utils.display.Display.res>`
        res (Vector): The pixel resolution of the game. This is the number of virtual pixels on the window.

            Example:
                The window (:func:`Display.window_size <rubato.utils.display.DisplayProperties.window_size>`)
                could be rendered at 500x500 while the resolution is at 1000x1000.
                This would mean that you can place game objects at 900, 900 and still see them despite
                the window not being 900 pixels tall.

            Warning:
                While this value can be changed, it is recommended that you do not
                alter it after initialization as it will scale your entire project in unexpected ways.
                If you wish to achieve scaling across an entire scene, simply utilize the
                :func:`camera zoom <rubato.structure.camera.Camera.zoom>` property in your scene's camera.
        window_pos (Vector): The current position of the window in terms of screen pixels.
        window_name (str): The name of the window.
        hidden (bool): Whether the window is currently hidden.
    """

    window: sdl2.ext.Window
    renderer: sdl2.ext.Renderer
    pixel_format = sdl2.SDL_PIXELFORMAT_ARGB8888
    argb_format = sdl2.SDL_CreateRGBSurfaceWithFormat(0, 1, 1, 32, pixel_format).contents.format.contents
    rgba_format = sdl2.SDL_CreateRGBSurfaceWithFormat(
        0, 1, 1, 32, sdl2.SDL_PIXELFORMAT_RGBA8888
    ).contents.format.contents
    hidden: bool = True

    _saved_window_size: Vector | None = None
    _saved_window_pos: Vector | None = None

    _half_res: tuple[float, float]

    def __init__(self) -> None:
        raise InitError(self)

    @classmethod
    def _update(
        cls,
        tx: sdl2.SDL_Texture,
        width: int,
        height: int,
        pos: Vector | tuple[float, float],
        scale: Vector | tuple[float, float] = (1, 1),
        angle: float = 0,
        flipx: bool = False,
        flipy: bool = False,
    ):
        """
        Note:
            pos is the center of the texture in cartesian coordinates.
        """
        flipx |= Math.sign(scale[0]) == -1
        flipy |= Math.sign(scale[1]) == -1

        flip = sdl2.SDL_FLIP_NONE
        if flipx:
            flip |= sdl2.SDL_FLIP_HORIZONTAL
        if flipy:
            flip |= sdl2.SDL_FLIP_VERTICAL

        x_dim = round(width * abs(scale[0]))
        y_dim = round(height * abs(scale[1]))

        final_pos = cls._center_cart_to_tl_sdl(pos, (x_dim, y_dim))

        sdl2.SDL_RenderCopyEx(
            cls.renderer.sdlrenderer,
            tx,
            None,
            sdl2.SDL_Rect(
                round(final_pos[0]),
                round(final_pos[1]),
                x_dim,
                y_dim,
            ),
            round(angle),
            None,
            flip,
        )

    @classmethod
    def _tl_sdl_to_center_cart(
        cls,
        pos: Vector | tuple[float, float],
        dims: Vector | tuple[float, float],
    ) -> tuple[float, float]:
        return cls._top_left_to_center(cls._sdl_to_cartesian(pos), dims)

    @classmethod
    def _center_cart_to_tl_sdl(
        cls,
        pos: Vector | tuple[float, float],
        dims: Vector | tuple[float, float],
    ) -> tuple[float, float]:
        return cls._center_to_top_left(cls._cartesian_to_sdl(pos), dims)

    @classmethod
    def _cartesian_to_sdl(cls, pos: Vector | tuple[float, float]) -> tuple[float, float]:
        return pos[0] + cls._half_res[0], cls._half_res[1] - pos[1]

    @classmethod
    def _sdl_to_cartesian(cls, pos: Vector | tuple[float, float]) -> tuple[float, float]:
        return pos[0] - cls._half_res[0], cls._half_res[1] - pos[1]

    @classmethod
    def _center_to_top_left(
        cls,
        pos: Vector | tuple[float, float],
        dims: Vector | tuple[float, float],
    ) -> tuple[float, float]:
        """
        Note:
            Assumes sdl coordinates.
        """
        return (pos[0] - (dims[0] / 2), pos[1] - (dims[1] / 2))

    @classmethod
    def _top_left_to_center(
        cls,
        pos: Vector | tuple[float, float],
        dims: Vector | tuple[float, float],
    ) -> tuple[float, float]:
        """
        Note:
            Assumes sdl coordinates.
        """
        return (pos[0] + (dims[0] / 2), pos[1] + (dims[1] / 2))

    @classmethod
    @property
    def display_ratio(cls) -> Vector:
        """
        The ratio of the renderer resolution to the window size. This is a read-only property.

        Returns:
            Vector: The ratio of the renderer resolution to the window size seperated by x and y.
        """
        return cls.res / cls.window_size

    @classmethod
    @property
    def border_size(cls) -> int:
        """The size of the black border on either side of the drawing area when the aspect ratios don't match."""
        # if a smart programmer can actually understand this, please check that its working correctly.
        # Thank you.
        render_rat = cls.res.y / cls.res.x
        window_rat = cls.window_size.y / cls.window_size.x

        if render_rat > window_rat:  # side burns
            rat = render_rat / window_rat  # how much fatter the window is than the render
            return round((cls.window_size.x - cls.window_size.x / rat) / 2)
        elif render_rat < window_rat:  # top burns
            rat = window_rat / render_rat  # how thinner the window is than the render
            return round((cls.window_size.y - cls.window_size.y / rat) / 2)
        return 0

    @classmethod
    def has_x_border(cls) -> bool:
        """Whether the window has a black border on the left or right side."""
        render_rat = cls.res.y / cls.res.x
        window_rat = cls.window_size.y / cls.window_size.x

        return render_rat > window_rat

    @classmethod
    def has_y_border(cls) -> bool:
        """Whether the window has a black border on the top or bottom."""
        render_rat = cls.res.y / cls.res.x
        window_rat = cls.window_size.y / cls.window_size.x

        return render_rat < window_rat

    @classmethod
    def set_window_icon(cls, path: str):
        """
        Set the icon of the window.

        Args:
            path: The path to the icon.
        """

        image = sdl2.ext.image.load_img(get_path(path))

        sdl2.SDL_SetWindowIcon(
            cls.window.window,
            image,
        )

    @classmethod
    def set_fullscreen(cls, on: bool = True):
        """
        Set the window to fullscreen.

        Args:
            on: Whether to set the window to fullscreen.
        """
        if on:
            if cls._saved_window_pos is None and cls._saved_window_size is None:
                cls._saved_window_size = cls.window_size.clone()
                cls._saved_window_pos = cls.window_pos.clone()
            sdl2.SDL_SetWindowFullscreen(cls.window.window, sdl2.SDL_WINDOW_FULLSCREEN_DESKTOP)
        else:
            if cls._saved_window_size is not None and cls._saved_window_pos is not None:
                cls.window_size = cls._saved_window_size
                cls.window_pos = cls._saved_window_pos
                cls._saved_window_size = None
                cls._saved_window_pos = None
            sdl2.SDL_SetWindowFullscreen(cls.window.window, 0)

    @classmethod
    def get_window_border_size(cls):
        """
        Get the size of the window border. pixels on the top sides and bottom of the window.

        Returns:
            The size of the window border.
        """
        top, left, bottom, right = ctypes.c_int(), ctypes.c_int(), ctypes.c_int(), ctypes.c_int()
        sdl2.SDL_GetWindowBordersSize(
            cls.window.window, ctypes.byref(top), ctypes.byref(left), ctypes.byref(bottom), ctypes.byref(right)
        )
        return top.value, left.value, bottom.value, right.value

    @classmethod
    def save_screenshot(
        cls,
        filename: str,
        path: str = "./",
        extension: str = "png",
        save_to_temp_path: bool = False,
        quality: int = 100
    ) -> bool:
        """
        Save the current screen to a file.

        Args:
            filename: The name of the file to save to.
            path: Path to output folder.
            extension: The extension to save the file as. (png, jpg, bmp supported)
            save_to_temp_path: Whether to save the file to a temporary path (i.e. MEIPASS used in exe).
            quality: The quality of the jpg 0-100 (only used for jpgs).

        Returns:
            If save was successful.
        """
        if extension not in ["png", "jpg", "bmp"]:
            raise ValueError("Invalid extension. Only png, jpg, bmp are supported.")

        w, h = ctypes.c_int(0), ctypes.c_int(0)

        sdl2.SDL_GetRendererOutputSize(cls.renderer.sdlrenderer, ctypes.byref(w), ctypes.byref(h))

        render_surface = sdl2.SDL_CreateRGBSurfaceWithFormat(0, w.value, h.value, 32, sdl2.SDL_PIXELFORMAT_ARGB8888)

        if not render_surface:
            raise RuntimeError(f"Could not create surface: {sdl2.SDL_GetError()}")
        try:
            if sdl2.SDL_RenderReadPixels(
                cls.renderer.sdlrenderer, sdl2.SDL_Rect(0, 0, w.value, h.value), sdl2.SDL_PIXELFORMAT_ARGB8888,
                render_surface.contents.pixels, render_surface.contents.pitch
            ) != 0:
                raise RuntimeError(f"Could not read screenshot: {sdl2.SDL_GetError()}")

            path_bytes: bytes = path.encode("utf-8")
            if save_to_temp_path:
                path_bytes = bytes(get_path(os.path.join(path, filename, filename + "." + extension)), "utf-8")
            else:
                path_bytes = bytes(os.path.join(path, filename + "." + extension), "utf-8")

            if extension == "png":
                return sdl2.sdlimage.IMG_SavePNG(render_surface, path_bytes) == 0
            elif extension == "jpg":
                return sdl2.sdlimage.IMG_SaveJPG(render_surface, path_bytes, quality) == 0
            elif extension == "bmp":
                return sdl2.SDL_SaveBMP(render_surface, path_bytes) == 0
            return False

        finally:
            sdl2.SDL_FreeSurface(render_surface)

    @classmethod
    def show_window(cls):
        """
        Show the window.
        """
        Display.hidden = False
        cls.window.open()

    @classmethod
    def hide_window(cls):
        """
        Hide the window.
        """
        Display.hidden = True
        cls.window.hide()

    @classmethod
    def maximize_window(cls):
        """
        Maximize the window.
        """
        sdl2.SDL_MaximizeWindow(cls.window.window)

    @classmethod
    def minmize_window(cls):
        """
        Minimize the window.
        """
        sdl2.SDL_MinimizeWindow(cls.window.window)

    @classmethod
    def restore_window(cls):
        """
        Restore the window.
        """
        sdl2.SDL_RestoreWindow(cls.window.window)

    @classmethod
    @property
    def center(cls) -> Vector:
        """The position of the center of the window."""
        return Vector(0, 0)

    @classmethod
    @property
    def top(cls) -> float:
        """The position of the top of the window."""
        return cls._half_res[1]

    @classmethod
    @property
    def right(cls) -> float:
        """The position of the right of the window."""
        return cls._half_res[0]

    @classmethod
    @property
    def left(cls) -> float:
        """The position of the left of the window."""
        return -cls._half_res[0]

    @classmethod
    @property
    def bottom(cls) -> float:
        """The position of the bottom of the window."""
        return -cls._half_res[1]

    @classmethod
    @property
    def top_left(cls) -> Vector:
        """The position of the top left of the window."""
        return Vector(cls.left, cls.top)

    @classmethod
    @property
    def top_right(cls) -> Vector:
        """The position of the top right of the window."""
        return Vector(cls.right, cls.top)

    @classmethod
    @property
    def bottom_left(cls) -> Vector:
        """The position of the bottom left of the window."""
        return Vector(cls.left, cls.bottom)

    @classmethod
    @property
    def bottom_right(cls) -> Vector:
        """The position of the bottom right of the window."""
        return Vector(cls.right, cls.bottom)

    @classmethod
    @property
    def top_center(cls) -> Vector:
        """The position of the top center of the window."""
        return Vector(0, cls.top)

    @classmethod
    @property
    def bottom_center(cls) -> Vector:
        """The position of the bottom center of the window."""
        return Vector(0, cls.bottom)

    @classmethod
    @property
    def center_left(cls) -> Vector:
        """The position of the center left of the window."""
        return Vector(cls.left, 0)

    @classmethod
    @property
    def center_right(cls) -> Vector:
        """The position of the center right of the window."""
        return Vector(cls.right, 0)
