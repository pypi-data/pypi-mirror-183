"""An abstraction for a grid of pixels that can be drawn onto."""
from __future__ import annotations
from typing import Optional
import sdl2, sdl2.ext, sdl2.sdlimage, ctypes
import os

from ...c_src import c_draw
from .. import Vector, Color, Display, get_path


class Surface:
    """
    A grid of pixels that can be modified without being attached to a game object.

    Args:
        width: The width of the surface in pixels. Once set this cannot be changed. Defaults to 32.
        height: The height of the surface in pixels. Once set this cannot be changed. Defaults to 32.
        scale: The scale of the surface. Defaults to (1, 1).
        rotation: The clockwise rotation of the sprite.
        af: Whether to use anisotropic filtering. Defaults to False.
    """

    def __init__(
        self,
        width: int = 32,
        height: int = 32,
        scale: Vector | tuple[float, float] = (1, 1),
        rotation: float = 0,
        af: bool = False,
    ):
        if width <= 0 or height <= 0:
            raise ValueError("Width and height must be greater than 0")

        self.rotation: float = rotation
        """The clockwise rotation of the sprite."""
        self.scale: Vector = Vector.create(scale)
        """The scale of the sprite."""
        self._af: bool = af
        self._width: int = width
        self._height: int = height
        self._color_key: Optional[int] = None

        sdl2.SDL_SetHint(b"SDL_RENDER_SCALE_QUALITY", b"linear" if self._af else b"nearest")
        self._tx: sdl2.SDL_Texture = sdl2.SDL_CreateTexture(
            Display.renderer.sdlrenderer, Display.pixel_format, sdl2.SDL_TEXTUREACCESS_STREAMING, width, height
        ).contents
        sdl2.SDL_SetTextureBlendMode(self._tx, sdl2.SDL_BLENDMODE_BLEND)
        self._pixels: int = c_draw.create_pixel_buffer(width, height)
        self._pixels_colorkey: int = 0
        self.uptodate: bool = False
        """
        Whether the texture is up to date with the surface.
        Can be set to False to trigger a texture regeneration at the next draw cycle.
        """

    @property
    def width(self) -> int:
        """The width of the surface in pixels (read-only)."""
        return self._width

    @property
    def height(self) -> int:
        """The height of the surface in pixels (read-only)."""
        return self._height

    @property
    def af(self):
        """Whether to use anisotropic filtering."""
        return self._af

    @af.setter
    def af(self, new: bool):
        self._af = new
        sdl2.SDL_SetHint(b"SDL_RENDER_SCALE_QUALITY", b"linear" if self._af else b"nearest")
        self._tx: sdl2.SDL_Texture = sdl2.SDL_CreateTexture(
            Display.renderer.sdlrenderer, Display.pixel_format, sdl2.SDL_TEXTUREACCESS_STREAMING, self.width,
            self.height
        ).contents
        sdl2.SDL_SetTextureBlendMode(self._tx, sdl2.SDL_BLENDMODE_BLEND)
        self.uptodate = False

    def size_scaled(self) -> Vector:
        """
        Gets the current size of the Surface. (Scaled)

        Returns:
            The size of the Surface
        """
        return Vector(self._width * self.scale.x, self._height * self.scale.y)

    def size(self) -> Vector:
        """
        Gets the current size of the Surface. (Unscaled)

        Returns:
            The size of the Surface
        """
        return Vector(self._width, self._height)

    def _blit(
        self,
        other: Surface,
        src_rect: tuple[int, int, int, int] | None = None,
        dst_rect: tuple[int, int, int, int] | None = None,
    ):
        """
        This function uses the SDL coordinate system and should only be used internally. This is mainly kept for
        Spritesheet. Blits (merges / copies) another Surface onto this one.

        Args:
            other: The Surface to blit onto this one.
            src_rect: The area (x, y, width, height) to blit from in the source surface (other).
                Defaults to the whole surface.
            dst_rect: The area (x, y, width, height) to blit to in the destination surface (self).
                Defaults to the whole surface.
        Note:
            Will not stretch the other surface to fit the destination rectangle.
        """
        c_draw.blit(
            other._pixels,
            self._pixels,
            other.width,
            other.height,
            self.width,
            self.height,
            *(src_rect or (0, 0, other.width, other.height)),
            *(dst_rect or (0, 0, self.width, self.height)),
        )
        self.uptodate = False

    def blit(
        self,
        other: Surface,
        src_rect: tuple[int, int, int, int] | None = None,
        dst: Vector | tuple[int, int] = (0, 0),
    ):
        """
        Blits (merges / copies) another Surface onto this one.

        Args:
            other: The Surface to blit onto this one.
            src_rect: The area (center_x, center_y, width, height) to crop from the source surface (other).
                Defaults to the whole surface.
            dst: The position to place the other surface. Defaults to (0, 0).

        Note:
            Will not stretch the other surface to fit the destination rectangle.
        """
        src_rect = src_rect or (0, 0, int(other.width), int(other.height))
        src_top_left = Display._center_to_top_left(other._convert_to_surface_space((0, 0)), src_rect[2:4])
        dst_final = Display._center_to_top_left(self._convert_to_surface_space((*dst,)), src_rect[2:4])
        c_draw.blit(
            other._pixels,
            self._pixels,
            other.width,
            other.height,
            self.width,
            self.height,
            int(src_top_left[0]),
            int(src_top_left[1]),
            *src_rect[2:4],
            int(dst_final[0]),
            int(dst_final[1]),
            *src_rect[2:4],
        )
        self.uptodate = False

    def flip_x(self):
        """Flips the surface horizontally."""
        c_draw.flip_x(self._pixels, self.width, self.height)
        self.uptodate = False

    def flip_y(self):
        """Flips the surface vertically."""
        c_draw.flip_y(self._pixels, self.width, self.height)
        self.uptodate = False

    def flip_anti_diagonal(self):
        """Flips the surface along the anti diagonal."""
        c_draw.flip_anti_diagonal(self._pixels, self.width, self.height)
        self.uptodate = False

    def _regen(self):
        """Updates the texture."""
        if self._color_key is not None:
            c_draw.colorkey_copy(self._pixels, self._pixels_colorkey, self._width, self._height, self._color_key)

        sdl2.SDL_UpdateTexture(
            self._tx, None, self._pixels if self._color_key is None else self._pixels_colorkey, self.width * 4
        )
        self.uptodate = True

    def clear(self):
        """
        Clears the surface.
        """
        c_draw.clear_pixels(self._pixels, self._width, self._height)
        self.uptodate = False

    def fill(self, color: Color):
        """
        Fill the surface with a color.

        Args:
            color: The color to fill with.
        """
        self.draw_rect((0, 0), (self._width, self._height), fill=color)

    def _convert_to_surface_space(self, pos: Vector | tuple[float, float]) -> tuple[float, float]:
        """Simple function that converts cartesian coordinates to surface space."""
        return (pos[0] + self._width / 2, -pos[1] + self._height / 2)

    def _convert_to_cartesian_space(self, pos: Vector | tuple[float, float]) -> tuple[float, float]:
        """Simple function that converts surface space to cartesian coordinates."""
        return (pos[0] - self._width / 2, -pos[1] + self._height / 2)

    def get_pixel(self, pos: Vector | tuple[float, float]) -> Color:
        """
        Gets the color of a pixel on the surface.

        Args:
            pos: The position of the pixel.

        Returns:
            The color of the pixel.
        """
        cart_pos = self._convert_to_surface_space(pos)
        x, y = round(cart_pos[0]), round(cart_pos[1])
        if 0 <= x < self._width and 0 <= y < self._height:
            return Color.from_argb32(c_draw.get_pixel(self._pixels, self._width, self._height, x, y))
        else:
            raise ValueError(f"Position is outside of the ${self.__class__.__name__}.")

    def set_pixel(self, pos: Vector | tuple[float, float], color: Color = Color.black, blending: bool = True):
        """
        Draws a point on the surface.

        Args:
            pos: The position to draw the point.
            color: The color of the point. Defaults to black.
            blending: Whether to use blending. Defaults to False.
        """
        cart_pos = self._convert_to_surface_space(pos)
        x, y = round(cart_pos[0]), round(cart_pos[1])
        c_draw.set_pixel(self._pixels, self._width, self._height, x, y, color.argb32(), blending)
        self.uptodate = False

    def draw_line(
        self,
        start: Vector | tuple[float, float],
        end: Vector | tuple[float, float],
        color: Color = Color.black,
        aa: bool = False,
        thickness: int = 1,
        blending: bool = True
    ):
        """
        Draws a line on the surface.

        Args:
            start: The start of the line.
            end: The end of the line.
            color: The color of the line. Defaults to black.
            aa: Whether to use anti-aliasing. Defaults to False.
            thickness: The thickness of the line. Defaults to 1.
            blending: Whether to use blending. Defaults to False.
        """
        start_pos = self._convert_to_surface_space(start)
        end_pos = self._convert_to_surface_space(end)
        sx, sy = round(start_pos[0]), round(start_pos[1])
        ex, ey = round(end_pos[0]), round(end_pos[1])
        c_draw.draw_line(
            self._pixels, self._width, self._height, sx, sy, ex, ey, color.argb32(), aa, blending, thickness
        )
        self.uptodate = False

    def draw_rect(
        self,
        center: Vector | tuple[float, float],
        dims: Vector | tuple[float, float],
        border: Color | None = None,
        border_thickness: int = 1,
        fill: Color | None = None,
        blending: bool = True
    ):
        """
        Draws a rectangle on the surface.

        Args:
            center: The top left corner of the rectangle.
            dims: The dimensions of the rectangle.
            border: The border color of the rectangle. Defaults to None.
            border_thickness: The thickness of the border. Defaults to 1.
            fill: The fill color of the rectangle. Set to None for no fill. Defaults to None.
            blending: Whether to use blending. Defaults to False.
        """
        top_left = Display._center_to_top_left(self._convert_to_surface_space(center), dims)
        x, y = round(top_left[0]), round(top_left[1])
        w, h = round(dims[0]), round(dims[1])
        c_draw.draw_rect(
            self._pixels,
            self._width,
            self._height,
            x,
            y,
            w,
            h,
            border.argb32() if border else 0,
            fill.argb32() if fill else 0,
            blending,
            border_thickness,
        )
        self.uptodate = False

    def draw_circle(
        self,
        center: Vector | tuple[float, float],
        radius: int,
        border: Color | None = None,
        border_thickness: int = 1,
        fill: Color | None = None,
        aa: bool = False,
        blending: bool = True,
    ):
        """
        Draws a circle on the surface.

        Args:
            center: The center of the circle.
            radius: The radius of the circle.
            border: The border color of the circle. Defaults to None.
            border_thickness: The thickness of the border. Defaults to 1.
            fill: The fill color of the circle. Set to None for no fill. Defaults to None.
            aa: Whether to use anti-aliasing. Defaults to False.
            blending: Whether to use blending. Defaults to False.
        """
        center_pos = self._convert_to_surface_space(center)
        x, y = round(center_pos[0]), round(center_pos[1])
        c_draw.draw_circle(
            self._pixels,
            self._width,
            self._height,
            x,
            y,
            radius,
            border.argb32() if border else 0,
            fill.argb32() if fill else 0,
            aa,
            blending,
            border_thickness,
        )
        self.uptodate = False

    def draw_poly(
        self,
        points: list[Vector] | list[tuple[float, float]],
        center: Vector | tuple[float, float] = (0, 0),
        border: Color | None = None,
        border_thickness: int = 1,
        fill: Color | None = None,
        aa: bool = False,
        blending: bool = True,
    ):
        """
        Draws a polygon on the surface.

        Args:
            points: The points of the polygon.
            center: The center of the polygon.
            border: The border color of the polygon. Defaults to None.
            border_thickness: The thickness of the border. Defaults to 1.
            fill: The fill color of the polygon. Set to None for no fill. Defaults to None.
            aa: Whether to use anti-aliasing. Defaults to False.
            blending: Whether to use blending. Defaults to False.
        """
        center_pos = self._convert_to_surface_space(center)
        c_draw.draw_poly(
            self._pixels,
            center_pos,
            self._width,
            self._height,
            points,
            border.argb32() if border else 0,
            fill.argb32() if fill else 0,
            aa,
            blending,
            border_thickness,
        )
        self.uptodate = False

    def switch_color(self, color: Color, new_color: Color):
        """
        Switches a color in the surface.

        Args:
            color: The color to switch.
            new_color: The new color to switch to.
        """
        c_draw.switch_colors(self._pixels, self._width, self._height, color.argb32(), new_color.argb32())
        self.uptodate = False

    def set_colorkey(self, color: Color):
        """
        Sets the colorkey of the surface.

        Args:
            color: Color to set as the colorkey.
        """
        if self._pixels_colorkey == 0:
            self._pixels_colorkey = c_draw.create_pixel_buffer(self.width, self.height)
        self._color_key = color.argb32()
        self.uptodate = False

    def remove_colorkey(self):
        """
        Remove the colorkey of the surface.
        """
        if self._pixels_colorkey != 0:
            c_draw.free_pixel_buffer(self._pixels_colorkey)
            self._pixels_colorkey = 0
        self._color_key = None
        self.uptodate = False

    def clone(self) -> Surface:
        """
        Clones the current surface.

        Returns:
            The cloned surface.
        """
        new = Surface(
            self.width,
            self.height,
            scale=self.scale.clone(),
            rotation=self.rotation,
            af=self.af,
        )
        new.blit(self)
        new._pixels_colorkey = self._pixels_colorkey
        new._color_key = self._color_key
        new.set_alpha(self.get_alpha())

        return new

    def set_alpha(self, new: int):
        """
        Sets surface wide alpha.

        Args:
            new: The new alpha. (value between 0-255)
        """
        new = max(min(new, 255), 0)
        sdl2.SDL_SetTextureAlphaMod(self._tx, new)

    def get_alpha(self) -> int:
        """
        Gets the surface wide alpha.
        """
        y = ctypes.c_uint8()
        sdl2.SDL_GetTextureAlphaMod(self._tx, ctypes.byref(y))
        return y.value

    def save_as(
        self,
        filename: str,
        path: str = "./",
        extension: str = "png",
        save_to_temp_path: bool = False,
        quality: int = 100,
    ) -> bool:
        """
        Save the surface to a file.

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

        render_surface = self._as_surf()

        path_bytes: bytes = path.encode("utf-8")
        if save_to_temp_path:
            path_bytes = bytes(get_path(os.path.join(path, filename, filename + "." + extension)), "utf-8")
        else:
            path_bytes = bytes(os.path.join(path, filename + "." + extension), "utf-8")

        succeeded = False
        if extension == "png":
            succeeded = sdl2.sdlimage.IMG_SavePNG(render_surface, path_bytes) == 0
        elif extension == "jpg":
            succeeded = sdl2.sdlimage.IMG_SaveJPG(render_surface, path_bytes, quality) == 0
        else:
            succeeded = sdl2.SDL_SaveBMP(render_surface, path_bytes) == 0

        sdl2.SDL_FreeSurface(render_surface)
        return succeeded

    def _as_surf(self) -> sdl2.SDL_Surface:
        """
        Converts the underlying texture to a SDL_Surface.

        Returns:
            The SDL_Surface.
        """
        if not self.uptodate:
            self._regen()

        surf = sdl2.SDL_CreateRGBSurfaceWithFormatFrom(
            self._pixels if self._pixels_colorkey == 0 else self._pixels_colorkey,
            self._width,
            self._height,
            32,
            self._width * 4,
            Display.pixel_format,
        )
        sdl2.SDL_SetSurfaceAlphaMod(surf, self.get_alpha())

        return surf

    @classmethod
    def from_file(
        cls,
        path: str,
        scale: Vector | tuple[float, float] = (1, 1),
        rotation: float = 0,
        af: bool = False,
    ) -> Surface:
        """
        Loads a surface from an image file.

        Args:
            path: The path to the file.
            scale: The scale of the surface. Defaults to (1, 1).
            rotation: The clockwise rotation of the sprite. Defaults to 0.
            af: Whether to use anisotropic filtering. Defaults to False.

        Returns:
            The resultant surface.
        """
        try:
            surf_bad = sdl2.ext.load_img(path, False)
        except OSError:
            surf_bad = sdl2.ext.load_img(get_path(path), False)
        except sdl2.ext.SDLError as e:
            fname = path.replace("\\", "/").split("/")[-1]
            raise TypeError(f"{fname} is not a valid image file") from e

        surf = sdl2.SDL_ConvertSurfaceFormat(surf_bad, Display.pixel_format, 0).contents
        s = cls(surf.w, surf.h, scale=scale, rotation=rotation, af=af)
        c_draw.free_pixel_buffer(s._pixels)
        s._pixels = c_draw.clone_pixel_buffer(surf.pixels, surf.w, surf.h)
        sdl2.SDL_FreeSurface(surf)
        sdl2.SDL_FreeSurface(surf_bad)
        return s

    @classmethod
    def _from_surf(
        cls,
        surf: sdl2.SDL_Surface,
        scale: Vector | tuple[float, float] = (1, 1),
        rotation: float = 0,
        af: bool = False
    ) -> Surface:
        """
        Creates a Surface from an SDL_Surface.
        Note that this does not free the original SDL_Surface.

        Args:
            surf: The SDL_Surface to create the surface from.
            scale: The scale of the surface. Defaults to (1, 1).
            rotation: The clockwise rotation of the sprite. Defaults to 0.
            af: Whether to use anisotropic filtering. Defaults to False.

        Returns:
            The resultant surface.
        """
        new_surf = sdl2.SDL_ConvertSurfaceFormat(surf, Display.pixel_format, 0).contents
        s = cls(surf.w, surf.h, scale=scale, rotation=rotation, af=af)
        c_draw.free_pixel_buffer(s._pixels)
        s._pixels = c_draw.clone_pixel_buffer(new_surf.pixels, surf.w, surf.h)
        sdl2.SDL_FreeSurface(new_surf)
        return s

    def __del__(self):
        sdl2.SDL_DestroyTexture(self._tx)
        c_draw.free_pixel_buffer(self._pixels)
