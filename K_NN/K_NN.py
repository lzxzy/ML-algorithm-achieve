# -*- coding: utf-8 -*-
"""
This script is an exercise on KNN.

Created on Tue Nov 03 21:21:39 2015

@author: 90Zeng
"""

import numpy as np
from sklearn import datasets
import operator

    
#-----------------function classify--------------------------------------    
def classify0(inX, dataSet, labels, k):
    dataSetSize = dataSet.shape[ 0 ]
    # 计算输入的向量inX与所有样本的距离
    diffMat = np.tile(inX, (dataSetSize, 1)) - dataSet
    sqDiffMat = diffMat ** 2
    sqDistances = sqDiffMat.sum(axis = 1)
    distances = sqDistances ** 0.5
    # 对距离大小进行排序
    sortedDistIndices = distances.argsort()
    classCount = {}
    # 选择距离最小的 K 个点
    for i in range(k):
        voteLabel = labels[ sortedDistIndices[i] ]
        classCount[ voteLabel ] = classCount.get(voteLabel, 0) + 1  
    # 按照类别的数量多少进行排序
    sortedClassCount = sorted(classCount.iteritems(),
                                 key=operator.itemgetter(1), reverse=True)                               
    return sortedClassCount[0][0]  # 返回类别数最多的类别名称
#-------------------end of function classify--------------------------------


def handwritingClassTest():
    # 导入数据
    digits = datasets.load_digits()
    totalNum = len(digits.data)
    # 选出90%样本作为训练样本，其余10%测试
    trainNum = int(0.8 * totalNum)
    trainX = digits.data[0 : trainNum]
    trainY = digits.target[0 : trainNum]
    
    testX = digits.data[trainNum:]
    testY = digits.target[trainNum:]
    
    errorCount = 0
    testExampleNum = len( testX )
    for i in range( testExampleNum ):
        # 测试样本在测试集中真实的类别
        trueLabel = testY[i]
        classifierResult = classify0( testX[ i, : ], trainX, trainY, 5 )
        print "\nThe classifier came back with: %d, the real answer is: %d"\
            % ( classifierResult, trueLabel )
        if trueLabel != classifierResult:
            errorCount += 1
        else:
            pass
    print "\nThe total number of errors is: %d" % errorCount
    print "\nthe total error rate is: %f" % ( 
        errorCount / float( testExampleNum) 
        )
    
    
if __name__ == '__main__':
    print "start..."
    handwritingClassTest()