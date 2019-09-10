# coding=utf-8
# 逻辑相关的工具类
from commons.utils import read_lines


# 载入地图原始数据
def load_map_array(mode):
    path = f'assets/maps/MAP_{mode}'
    lines = read_lines(path)
    game_map_arr = []
    for line in lines:
        items = list(map(lambda x: x.strip(), line.split(",")))
        items = list(map(lambda x: None if x == 'None' else int(x), items))
        game_map_arr.append(items)
    return game_map_arr
