from functools import reduce
import matplotlib.pyplot as plot
from mpl_toolkits.mplot3d import Axes3D
import numpy as np
fig = plot.figure()
num1 = 0B0110011001100000
num2 = 0B0101010101010101
num3 = 0B1000111100001100
udp = [num1, num2, num3]
print("original UDP-package")
print("num1:"+format(num1, 'b'))
print("num2:"+format(num2, 'b'))
print("num3:"+format(num3, 'b'))


def res_num(num):
    return 0xffff - num & 0xffffffff


def udp_check(num01, num02):

    num03 = num01 + num02
    num03 = num03 % (2 ** 16) + (num03 >> 16)
    return num03


def sender_check(segment):
    num4 = res_num(reduce(udp_check, segment))
    udp.append(num4)
    return


def judge(segment):
    return reduce(udp_check, segment) == 2 ** 16 - 1


sender_check(udp)
print("start checking")

plot.scatter([1, 2, 3], [udp[:3]], color="blue", marker="x")
plot.scatter(4, udp[3], color="red", marker="o")
plot.xticks([])
plot.gcf().set_facecolor(np.ones(3) * 240 / 255)
plot.grid()

plot.show()
