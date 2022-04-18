#!/usr/bin/python
import random
import numpy
import matplotlib.pyplot as plt
import matplotlib
import time

plate = [[1, 1, 1, 3],
         [1, 3, 1, 1],
         [2, 2, 3, 2],
         [3, 2, 2, 2]]


def pprint(array: list) -> None:
    a = numpy.asarray(array)
    print(a)
    del a


def swap_list(pos_1: tuple, pos_2: tuple) -> None:
    global plate
    if type(pos_1) != tuple or type(pos_2) != tuple:
        raise TypeError("Function parameter must be <tuple>")
    temp = plate[pos_1[0]][pos_1[1]]
    plate[pos_1[0]][pos_1[1]] = plate[pos_2[0]][pos_2[1]]
    plate[pos_2[0]][pos_2[1]] = temp
    return None


def check_entropy() -> int:
    t_horizontal = []
    for i in plate:
        for j in i:
            t_horizontal.append(j)

    t_vertical = []
    for i in numpy.asarray(plate).transpose():
        for j in i:
            t_vertical.append(int(j))

    del i, j
    entropy = 0
    for i in range(16):
        try:
            if t_horizontal[i] == t_horizontal[i + 1]:
                entropy -= 0.5
            else:
                entropy += 0.75
        except IndexError:
            pass
    try:
        for j in range(16):
            if t_vertical[j] == t_horizontal[j + 1]:
                entropy -= 0.5
            else:
                entropy += 0.75
    except IndexError:
        pass
    del i, j
    return entropy


n = int(input("输入需要随机打乱的次数:"))
ns = []
entropy_ = []


for _count in range(n):
    print(f"第{str(_count+1)}次打乱：")
    p11 = random.randint(0, 3)
    p12 = random.randint(0, 3)
    p21 = random.randint(0, 3)
    p22 = random.randint(0, 3)
    position_1 = (p11, p12)
    position_2 = (p21, p22)
    swap_list(position_1, position_2)
    pprint(plate)
    print("混乱度", check_entropy())
    ns.append(_count + 1)
    entropy_.append(check_entropy())
    # time.sleep(0.2)

x_axis = numpy.asarray(ns)
y_axis = numpy.asarray(entropy_)
chinese_font = matplotlib.font_manager.FontProperties(fname="SourceHanSansSC-Bold.otf")
plt.title("")
plt.xlabel("打乱次数", fontproperties=chinese_font)
plt.ylabel("混乱度", fontproperties=chinese_font)
plt.plot(x_axis, y_axis)
plt.show()
