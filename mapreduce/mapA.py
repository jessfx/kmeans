import sys
from copy import deepcopy
import random

import numpy as np
import scipy as sp
from time import time


def readInput(filename):
    for line in filename:
        yield line.strip().split(' ')


def kMeansMapper():
    string = '%d\t'
    fp = open('./old_centlist.txt')
    centlist = []
    for num, line in enumerate(fp.readlines()):
        string1 = num + '\t' + line.strip()
        print(string1)
        values = line.strip().split(' ')
        array = []
        for value in values[2:]:
            array.append(int(value))
        array = np.array(array)
        cent = [value[0], value[1], array]
        centlist.append(cent)
    fp.close()
    values = readInput(sys.stdin)
    array = []
    for value in values[2:]:
        string += '%s ' % value
        array.append(int(value))
    array = np.array(array)
    data = [values[0], values[1], array]
    distance = np.linalg.norm(centlist[0][2] - data[2])
    cluster_num = 0
    num = 1
    for cent in centlist[1:]:
        distance1 = np.linalg.norm(cent[2] - data[2])
        if distance > distance1:
            cluster_num = num
            distance = distance1
        num += num + 1
    print((string % cluster_num).strip())


if __name__ == '__main__':
    kMeansMapper()
