#!/usr/bin/python3
import sys
import numpy as np


def readInput(filename):
    for line in filename:
        yield line.strip().split('/t')


def kMeansReducer():
    cent_num, cent = readInput(sys.stdin)
    new_cent = ['xxxxxxxxxxxx', 'xxxxxxxxxx', np.array([0])]
    datalist = []
    for cluster_num, values in readInput(sys.stdin):
        print(cluster_num + '\t' + values)
        array = []
        for value in values.split(' ')[2:]:
            array.append(int(value))
        data = [values[0], values[1], np.array(array)]
        datalist.append(values)
        new_cent[2] = new_cent[2] + data[2]
    new_cent[2] = new_cent[2] / len(datalist)
    fp = open('./new_centlist.txt', 'w')
    fp.write(cent_num + '\t' + cent + '\n')


if __name__ == '__main__':
    kMeansReducer()
