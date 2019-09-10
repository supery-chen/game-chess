# coding=utf-8


# 按行读取文件
def read_lines(path):
    with open(path, 'r', encoding='utf-8') as f:
        lines = f.readlines()
        return list(map(lambda x: x.strip(), lines))
