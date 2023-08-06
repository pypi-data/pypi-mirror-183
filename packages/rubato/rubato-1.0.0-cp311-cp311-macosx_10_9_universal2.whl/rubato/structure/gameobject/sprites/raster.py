"""Abstract component for manipulating pixels attached to a game object."""
from __future__ import annotations
from .. import Component, Rectangle
from .... import Vector, Camera, Draw, Color, Surface


class Raster(Component):
    """
    A raster is a component that contains a surface.

    Args:
        width: The width of the Raster. Defaults to 32.
        height: The height of the Raster. Defaults to 32.
        af: Whether to use anisotropic filtering. Defaults to False.
        scale: The scale of the Raster. Defaults to (1, 1).
        offset: The offset of the Raster. Defaults to (0, 0).
        rot_offset: The rotation offset of the Raster. Defaults to 0.
        z_index: The z-index of the Raster. Defaults to 0.
        hidden: Whether to hide the Raster. Defaults to False.
    """

    def __init__(
        self,
        width: int = 32,
        height: int = 32,
        af: bool = False,
        scale: Vector | tuple[float, float] = (1, 1),
        offset: Vector | tuple[float, float] = (0, 0),
        rot_offset: float = 0,
        z_index: int = 0,
        hidden: bool = False,
    ):
        super().__init__(offset, rot_offset, z_index, hidden)
        self.surf: Surface = Surface(width, height, scale, rot_offset, af)

    @property
    def scale(self) -> Vector:
        """The scale of the raster."""
        return self.surf.scale

    @scale.setter
    def scale(self, new: Vector):
        self.surf.scale = new

    @property
    def af(self) -> bool:
        """Whether to use anisotropic filtering."""
        return self.surf.af

    @af.setter
    def af(self, new: bool):
        self.surf.af = new

    def get_rect(self) -> Rectangle:
        """
        Generates the rectangular bounding box of the raster.

        Returns:
            The Rectangle hitbox that bounds the raster.
        """
        size = self.get_size()
        return Rectangle(offset=self.offset, width=size.x, height=size.y, scale=self.scale)

    def blit(
        self,
        other: Raster,
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
        self.surf.blit(other.surf, src_rect, dst)

    def flip_x(self):
        """
        Flips the raster along the x-axis.
        """
        self.surf.flip_x()

    def flip_y(self):
        """
        Flips the raster along the y-axis.
        """
        self.surf.flip_y()

    def flip_anti_diagonal(self):
        """
        Flips the surface along the anti-diagonal.
        """
        self.surf.flip_anti_diagonal()

    def draw(self, camera: Camera):
        self.surf.rotation = self.true_rotation()
        Draw.queue_surface(self.surf, self.true_pos(), self.true_z(), camera)

    def clear(self):
        """
        Clears the surface.
        """
        self.surf.clear()

    def fill(self, color: Color):
        """
        Fill the surface with a color.

        Args:
            color: The color to fill with.
        """
        self.surf.fill(color)

    def get_pixel(self, pos: Vector | tuple[float, float]) -> Color:
        """
        Gets the color of a pixel on the surface.

        Args:
            pos: The position of the pixel.

        Returns:
            The color of the pixel.
        """
        return self.surf.get_pixel(pos)

    def set_pixel(self, pos: Vector | tuple[float, float], color: Color = Color.black, blending: bool = True):
        """
        Draws a point on the surface.

        Args:
            pos: The position to draw the point.
            color: The color of the point. Defaults to black.
            blending: Whether to use blending. Defaults to False.
        """
        self.surf.set_pixel(pos, color, blending)

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
        self.surf.draw_line(start, end, color, aa, thickness, blending)

    def draw_rect(
        self,
        center: Vector | tuple[float, float],
        dims: Vector | tuple[float, float],
        border: Color = Color.black,
        border_thickness: int = 1,
        fill: Color | None = None,
        blending: bool = True,
    ):
        """
        Draws a rectangle on the surface.

        Args:
            center: The top left corner of the rectangle.
            dims: The dimensions of the rectangle.
            border: The border color of the rectangle. Defaults to black.
            border_thickness: The thickness of the border. Defaults to 1.
            fill: The fill color of the rectangle. Set to None for no fill. Defaults to None.
            blending: Whether to use blending. Defaults to False.
        """
        self.surf.draw_rect(center, dims, border, border_thickness, fill, blending)

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
        self.surf.draw_circle(center, radius, border, border_thickness, fill, aa, blending)

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
        self.surf.draw_poly(points, center, border, border_thickness, fill, aa, blending)

    def get_size(self) -> Vector:
        """
        Gets the current size of the surface.

        Returns:
            The size of the surface
        """
        return self.surf.size_scaled()

    def switch_color(self, color: Color, new_color: Color):
        """
        Switches a color in the surface.

        Args:
            color: The color to switch.
            new_color: The new color to switch to.
        """
        self.surf.switch_color(color, new_color)

    def set_colorkey(self, color: Color):
        """
        Sets the colorkey of the surface.
        Args:
            color: Color to set as the colorkey.
        """
        self.surf.set_colorkey(color)

    def set_alpha(self, new: int):
        """
        Sets surface wide alpha.

        Args:
            new: The new alpha. (value between 0-255)
        """
        self.surf.set_alpha(new)

    def get_alpha(self) -> int:
        """
        Gets the surface wide alpha.
        """
        return self.surf.get_alpha()

    def save_as(
        self,
        filename: str,
        path: str = "./",
        extension: str = "png",
        save_to_temp_path: bool = False,
        quality: int = 100,
    ) -> bool:
        """
        Save the raster to a file.

        Args:
            filename: The name of the file to save to.
            path: Path to output folder.
            extension: The extension to save the file as. (png, jpg, bmp supported)
            save_to_temp_path: Whether to save the file to a temporary path (i.e. MEIPASS used in exe).
            quality: The quality of the jpg 0-100 (only used for jpgs).

        Returns:
            If save was successful.
        """
        return self.surf.save_as(filename, path, extension, save_to_temp_path, quality)

    def clone(self) -> Raster:
        """
        Clones the current raster.

        Returns:
            The cloned raster.
        """
        r = Raster(
            width=self.surf.width,
            height=self.surf.height,
            scale=self.scale,
            af=self.af,
            offset=self.offset.clone(),
            rot_offset=self.rot_offset,
            z_index=self.z_index,
        )
        r.surf = self.surf.clone()
        return r


class Image(Raster):
    """
    An image is a raster subclass that generates the surface from an image file.

    Args:
        path: The path to the file.
        af: Whether to use anisotropic filtering. Defaults to False.
        scale: The scale of the Raster. Defaults to (1, 1).
        offset: The offset of the Raster. Defaults to (0, 0).
        rot_offset: The rotation offset of the Raster. Defaults to 0.
        z_index: The z-index of the Raster. Defaults to 0.
        hidden: Whether to hide the Raster. Defaults to False.
    """

    def __init__(
        self,
        path: str,
        af: bool = False,
        scale: Vector | tuple[float, float] = (1, 1),
        offset: Vector | tuple[float, float] = (0, 0),
        rot_offset: float = 0,
        z_index: int = 0,
        hidden: bool = False,
    ):
        super().__init__(offset=offset, rot_offset=rot_offset, z_index=z_index, hidden=hidden)
        if path == "":
            self.surf = Surface(1, 1)
        else:
            self.surf = Surface.from_file(path, scale, rot_offset, af)

    def clone(self) -> Image:
        img = Image(
            path="",
            scale=self.scale,
            offset=self.offset.clone(),
            rot_offset=self.rot_offset,
            af=self.af,
            z_index=self.z_index
        )
        img.surf = self.surf.clone()
        return img
