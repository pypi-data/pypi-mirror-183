import threading
import pygame
from .wordtile import *
from .console import *
this_console = Console()
from .mocio import *
moprint = Printer()
moinput = Reader()
from .ui import *


def init(width, height, font_height, title) -> None:
    """
    生成控制台界面

    :param width: 窗口宽（字符）
    :param height: 窗口高（字符）
    :param font_height: 字符大小
    :param title: 窗口标题
    """
    ok = False

    def create_console():
        global this_console
        this_console.init(width, height, font_height, title)
        nonlocal ok
        ok = True
        this_console.start()

    thread = threading.Thread(target=create_console)
    thread.start()
    while not ok:
        pygame.time.wait(10)
    global this_console
    moprint.bind(this_console)
    moinput.bind(this_console, moprint)


def close() -> None:
    pygame.event.post(pygame.event.Event(pygame.QUIT))
