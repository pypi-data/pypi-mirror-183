"""
rubato is a modern 2D game engine for python. Accurate fixed-step physics
simulations, robust scene and game object management, event listener system and more
all come prepackaged.

Fundamentally, rubato is built developer-focused. From intricate rigidbody
simulations to 2D games, rubato streamlines development for beginners and the
poweruser. And all that finally with some legible documentation.
"""

# pylint: disable=wrong-import-position
from warnings import simplefilter
from importlib.resources import files
import cython, sys

if not cython.compiled and "sphinx" not in sys.modules:
    raise Exception("rubato must be compiled with Cython")

simplefilter("ignore", UserWarning)

import sdl2, sdl2.sdlttf, sdl2.ext

simplefilter("default", UserWarning)
simplefilter("default", DeprecationWarning)

from .utils import *
from .game import Game
from .structure import *
from .misc import world_mouse, wrap


def init(
    res: Vector | tuple[float, float] = (500, 500),
    window_size: Vector | tuple[float, float] | None = None,
    window_pos: Vector | tuple[float, float] | None = None,
    fullscreen: bool = False,
    name: str = "Untitled Rubato App",
    icon: str = "",
    maximize: bool = False,
    target_fps: int = 0,
    physics_fps: int = 50,
    hidden: bool = False  # test: skip
):
    """
    Initializes rubato.

    Args:
        name: The title that appears at the top of the window. Defaults to "Untitled Rubato App".
        res: The pixel resolution of the game, cast to int Vector. Defaults to (500, 500).
        window_size: The size of the window, cast to int Vector. When not set, defaults to half the resolution.
            This is usually the sweet spot between performance and image quality.
        window_pos: The position of the window, cast to int Vector. Set to None to let the computer decide.
            Defaults to None.
        icon: The path to the icon that will appear in the window. Defaults to "" (the rubato logo).
        fullscreen: Whether the game should be fullscreen. Defaults to False.
        maximize: Whether the game should be maximized. If fullscreen is set to True, that will take priority.
            Defaults to False.
        target_fps: The target frames per second. If set to 0, the target fps will be uncapped. Defaults to 0.
        physics_fps: The physics simulation's frames per second. Defaults to 50.
        hidden: Whether the window should be hidden. Defaults to False.
    """
    sdl2.SDL_Init(sdl2.SDL_INIT_EVERYTHING)

    Game._initialized = True

    Time.target_fps = target_fps
    if Time.target_fps != 0:
        Time._normal_delta = int(1000 / target_fps)
    Time._physics_fps = physics_fps
    Time.fixed_delta = 1 / physics_fps

    flags = (
        sdl2.SDL_WINDOW_RESIZABLE | sdl2.SDL_WINDOW_ALLOW_HIGHDPI | sdl2.SDL_WINDOW_MOUSE_FOCUS |
        sdl2.SDL_WINDOW_INPUT_FOCUS | sdl2.SDL_WINDOW_HIDDEN
    )

    window_pos, change_pos = ((int(window_pos[0]), int(window_pos[1])), True) if window_pos else (None, False)

    size = res if not window_size else window_size

    Display.window = sdl2.ext.Window(name, (int(size[0]), int(size[1])), window_pos, flags)

    Display.renderer = sdl2.ext.Renderer(
        Display.window,
        flags=(sdl2.SDL_RENDERER_ACCELERATED | sdl2.SDL_RENDERER_TARGETTEXTURE),
        logical_size=(int(res[0]), int(res[1]))
    )
    Display._half_res = (res[0] / 2, res[1] / 2)

    if change_pos:
        Display.window_pos += Vector(0, Display.get_window_border_size()[0])

    if icon:
        Display.set_window_icon(icon)
    else:
        Display.set_window_icon(str(files("rubato.static.png").joinpath("logo_filled.png")))

    Display.set_fullscreen(fullscreen)

    if maximize and not fullscreen:
        Display.maximize_window()

    Display.hidden = hidden

    Game.debug_font = Font(size=22, font="Mozart", color=Color.debug)

    sdl2.SDL_JoystickEventState(sdl2.SDL_ENABLE)


def begin():
    """
    Starts the main game loop.

    Raises:
        RuntimeError: rubato has not been initialized before calling.
    """
    if Game._initialized:
        if not Display.hidden:
            Display.show_window()
        Game._start()
    else:
        raise RuntimeError(
            "You have not initialized rubato. Make sure to run rubato.init() right after importing the library"
        )


def end():
    """
    Quit the game and close the python process. You can also do this by setting ``Game.state`` to ``Game.STOPPED``.
    """
    Game.state = Game.STOPPED


def pause():
    """
    Pause the game. You can also do this by setting ``Game.state`` to ``Game.PAUSED``.
    """
    Game.state = Game.PAUSED


def resume():
    """
    Resumes the game. You can also do this by setting ``Game.state`` to ``Game.RUNNING``.
    """
    Game.state = Game.RUNNING
