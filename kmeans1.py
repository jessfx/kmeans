import sys
from copy import deepcopy
import random

import numpy as np
import scipy as sp
from time import time


def loadData(filename):
    datalist = []
    fp = open(filename)
    for line in fp.readlines():
        values = line.strip().split(' ')
        array = []
        for value in values[2:]:
            array.append(int(value))
        array = np.array(array)
        data = [values[0], values[1], array]
        datalist.append(data)
    return datalist


def randCent(size, k):  # 随机中心点
    centlist = random.sample(range(size), k)
    return centlist


def kMeans(datalist, k, max_iterate=20):
    randnum = randCent(len(datalist), k)
    clusters = []
    centlist = []
    distances = []
    for num in randnum:
        clusters.append([])
        centlist.append(
            ['xxxxxxxxxxxx', 'xxxxxxxxxx', datalist[num][2].copy()])
    for iterate_time in range(max_iterate):
        for cluster in clusters:
            cluster.clear()
        distances.clear()
        for data in datalist:
            distance = np.linalg.norm(centlist[0][2] - data[2])
            cluster_num = 0
            num = 1
            for cent in centlist[1:]:
                distance1 = np.linalg.norm(cent[2] - data[2])
                if distance > distance1:
                    distance = distance1
                    cluster_num = num
                num += 1
            clusters[cluster_num].append(data)
            distances.append(distance)
        exit_code = 0
        for num, cluster in enumerate(clusters):
            new_cent = ['xxxxxxxxxxxx', 'xxxxxxxxxx', np.array([0])]
            for element in cluster:
                new_cent[2] = new_cent[2] + element[2]
            new_cent[2] = (new_cent[2] / len(cluster)).astype(np.int32)
            if (new_cent[2] == centlist[num][2]).all():
                exit_code = exit_code + 1
            else:
                centlist[num] = new_cent
        if exit_code == len(clusters):
            break
    return centlist, clusters, iterate_time + 1, distance


def biKmeans(datalist, k):
    cluster_assment = np.zeros((len(datalist, 2)))
    clusters_centlist, clusters cluster_assment[:, 1] = kMeans(datalist, 1)
    cluster_num = 1:
    while cluster_num < k:
        for cluster in clusters:


def run(filename, k, max_iterate):
    startTime = time()
    datalist = loadData(filename)
    centlist, clusters, iterate_time = kMeans(datalist, k, max_iterate)
    stopTime = time()
    print('%d' % iterate_time)
    print('%.2f' % (stopTime - startTime))


if __name__ == '__main__':
    run('D:\\data.txt', 5, 100)
