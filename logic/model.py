# coding=utf-8
from enum import Enum
from .utils import load_map_array


# 游戏模式
class MODE(Enum):
    LOCAL = 0
    INTERNET = 1
    AI = 2


# 角色
class ROLE(Enum):
    P1 = 0
    P2 = 1


class Player:

    def __init__(self, role: ROLE, map_arr: list):
        self.role = role
        self.chessman_list = self.init_chessman_list(self.role, map_arr)

    def init_chessman_list(self, role, map_arr):

        pass


class ChessBoard:

    def __init__(self, mode: MODE):
        self.mode = mode
        self.map_arr = load_map_array(self.mode)
