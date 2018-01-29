from numpy import *


def biKmeans(dataSet, k, distMeas=distEclud):
    m = shape(dataSet)[0]
    clusterAssment = mat(zeros((m, 2)))  # 记录簇分配的结果及误差
    centroid0 = mean(dataSet, axis=0).tolist()[0]  # 计算整个数据集的质心
    centList = [centroid0]  # create a list with one centroid
    for j in range(m):  # 计算初始聚类点与其他点的距离
        clusterAssment[j, 1] = distMeas(mat(centroid0), dataSet[j, :])**2
    while (len(centList) < k):
        lowestSSE = inf
        for i in range(len(centList)):  # 尝试划分每一簇
            # get the data points currently in cluster i
            ptsInCurrCluster = dataSet[nonzero(
                clusterAssment[:, 0].A == i)[0], :]
            centroidMat, splitClustAss = kMeans(
                ptsInCurrCluster, 2, distMeas)  # 对这个簇运行一个KMeans算法，k=2
            # compare the SSE to the currrent minimum
            sseSplit = sum(splitClustAss[:, 1])
            sseNotSplit = sum(clusterAssment[nonzero(
                clusterAssment[:, 0].A != i)[0], 1])
            print "sseSplit, and notSplit: ", sseSplit, sseNotSplit
            if (sseSplit + sseNotSplit) < lowestSSE:  # 划分后更好的话
                bestCentToSplit = i
                bestNewCents = centroidMat
                bestClustAss = splitClustAss.copy()
                lowestSSE = sseSplit + sseNotSplit
        bestClustAss[nonzero(bestClustAss[:, 0].A == 1)[0], 0] = len(
            centList)  # 更新簇的分配结果change 1 to 3,4, or whatever
        bestClustAss[nonzero(bestClustAss[:, 0].A == 0)
                     [0], 0] = bestCentToSplit
        print 'the bestCentToSplit is: ', bestCentToSplit
        print 'the len of bestClustAss is: ', len(bestClustAss)
        # replace a centroid with two best centroids
        centList[bestCentToSplit] = bestNewCents[0, :].tolist()[0]
        centList.append(bestNewCents[1, :].tolist()[0])
        clusterAssment[nonzero(clusterAssment[:, 0].A == bestCentToSplit)[
            0], :] = bestClustAss  # reassign new clusters, and SSE
    return mat(centList), clusterAssment
