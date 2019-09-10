# coding=utf-8
# 控件封装
from enum import Enum

# 默认字体大小
DEFAULT_FONT_SIZE = 16
# 默认字体
DEFAULT_FONT = 'assets/fonts/msyh.ttf'


class ALIGN(Enum):
    LEFT = 0
    RIGHT = 1
    TOP = 2
    BOTTOM = 3
    CENTER = 4


# 基本控件，所有控件的父类
class Widget:

    def __init__(self, x, y, width=None, height=None):
        self.x = x
        self.y = y
        self.width = width
        self.height = height


# 文本控件
class Label(Widget):

    def __init__(self, x, y, text, width=None, height=None, font=None, font_size=None):
        Widget.__init__(self, x, y, width, height)
        self.text = text
        if font is None:
            self.font = DEFAULT_FONT
        else:
            self.font = font

        if font_size is None:
            self.font_size = DEFAULT_FONT_SIZE
        else:
            self.font_size = font_size


# 按钮控件
class Button(Label):

    def __init__(self, x, y, text, click, width=None, height=None, font=None, font_size=None, hover=None):
        Label.__init__(self, x, y, text, width, height, font, font_size)
        self.click = click
