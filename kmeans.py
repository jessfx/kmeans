import random
import sys
from copy import deepcopy
from math import pow, sqrt
from time import time


def loadData():  # 读数据 格式[学号，时间，数据1,数据2,......]
    dataSet = []
    for line in sys.stdin:
        line = line.strip().split(' ')
        data = [line[0], line[1]]
        for value in line[2:]:
            data.append(int(value))
        dataSet.append(data)
    return dataSet


def randCent(size, k):  # 随机中心点
    centList = random.sample(range(size), k)
    return centList


def distCal(vecA, vecB):  # 计算向量距离
    length = 0
    for i in range(2, len(vecA)):
        length = length + calFunc1(vecA[i], vecB[i])
    return int(sqrt(length / (len(vecA) - 2)))


def calFunc1(a, b):  # 距离公式
    return (a - b) * (a - b)


def kMeans(dataSet, k, maxIterate):
    # 随机中心点
    randList = randCent(len(dataSet), k)
    # 类数组
    items = []
    # 中心点数组
    centItems = []
    for num in randList:
        items.append([])
        centItems.append(deepcopy(dataSet[num]))
    for j in range(maxIterate):
        for item in items:
            item.clear()
        for data in dataSet:
            length = distCal(centItems[0], data)
            centNum = 0
            i = 1
            # 计算向量与中心点距离，选最小距离
            for cent in centItems[1:]:
                len0 = distCal(cent, data)
                if length > len0:
                    centNum = i
                    length = len0
                i = i + 1
            items[centNum].append(data)
        i = 0
        # 退出循环标志
        exitCode = 0
        # 计算每一类中心点
        for item in items:
            cent = deepcopy(centItems[i])
            for key in range(2, len(centItems[0])):
                value = 0
                for data in item:
                    value = value + data[key]
                value = int(value / (len(item)))
                cent[key] = value
            # 计算新中心点与原中心点距离
            len0 = distCal(centItems[i], cent)
            if len0 == 0:
                exitCode = exitCode + 1
            centItems[i] = cent
            i = i + 1
        if exitCode == len(centItems):
            break
    for cent in centItems:
        print(cent)
    return j + 1, items


def run(fileName, k, maxIterate):
    startTime = time()
    dataSet = loadData(fileName)
    i, items = kMeans(dataSet, k, maxIterate)
    stopTime = time()
    print('%d' % i)
    print('%.2f' % (stopTime - startTime))
    return items


if __name__ == '__main__':
    # module = sys.modules[__name__]
    # fileName = getattr(module, sys.argv[2])
    # k = getattr(module, sys.argv[3])
    # maxIterate = getattr(module, sys.argv[4])
    items = run("D:\\data.txt", 5, 100)
