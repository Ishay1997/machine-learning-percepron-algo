# python 3.7
import numpy
import random
from Point import Point
from itertools import combinations
from hypothesis import hypothesis
from numpy import log as ln
from numpy import exp

adaboost_runs = 100
K = 8
EmpirError = numpy.zeros(shape=K)
Error = numpy.zeros(shape=K)


def Adaboost_algorythem(numOfRuns, pointsSet):
    mid = int(len(pointsSet) / 2)
    random.shuffle(pointsSet)
    trainSet = pointsSet[0:mid]
    testSet = pointsSet[mid:]

    for k in range(0, numOfRuns):
        algorithmResult = algorithmAdaboost(trainSet, k + 1)
        sumTrain = Sum(trainSet, algorithmResult)
        # Empirical error
        sumTest = Sum(testSet, algorithmResult)
        EmpirError[k] = sumTrain / mid
        Error[k] = sumTest / mid


def algorithmAdaboost(trainSet, iter: int):
    HypeWeight = []
    for p in trainSet:
        p.set_weight(1 / len(trainSet))
    for k in range(iter):
        bestLine, sumOfError = bestHype(trainSet)
        weight = 0.5 * ln((1 - sumOfError) / sumOfError)
        normalization = 0
        for p in trainSet:
            p.set_weight(p.get_weight() * exp(-weight * bestLine.classify(p) * p.get_label()))
            normalization += p.get_weight()  # Add into normalization parameter all the weights
        for p in trainSet:
            p.set_weight(p.get_weight() / normalization)  # Normalize all the weights
        HypeWeight.append((bestLine, weight))  # Add the best rule and its weight into the list
    return HypeWeight

def bestHype(trainPoints):
    per = combinations(trainPoints, 2)
    bestLine = hypothesis()
    sumOfError = 1
    for pairs in per:
        lineBetweenPoints = hypothesis(pairs[0], pairs[1])
        tempSum = 0
        for p in trainPoints:
            tempSum += p.get_weight() * int(p.get_label() != lineBetweenPoints.classify(p))
        if tempSum != 0 and tempSum < sumOfError:
            bestLine = lineBetweenPoints
            sumOfError = tempSum
    return bestLine, sumOfError

def Sum(set, algorithmResult):
    sumOfSet = 0
    for point in set:
        tempSum = 0
        for bestRule, alpha in algorithmResult:
            tempSum += alpha * bestRule.classify(point)
        sumOfSet += int(tempSum * point.get_label() < 0)
    return sumOfSet




def readData(fileName):
    file = open(fileName, "r")
    DataSet = []
    for line in file:
        point = line.split()
        DataSet.append(Point(point[0], point[1], point[2]))
    return DataSet


def beginOutput():
    output = "K = " + str(K) + "\n"
    print(output)
    return output


def addOutput(trainSetError: float, testSetError: float, k: int):
    output = "\n i = " + str(k) + "\n"
    output += "Train error = " + str(trainSetError) + "\n"
    output += "Test error = " + str(testSetError) + "\n"
    print(output)
    return output


if __name__ == '__main__':
    dataSet = readData("four_circle.txt")
    totalTrainErrorList = numpy.zeros(K)
    totalTestErrorList = numpy.zeros(K)
    outputString = beginOutput()
    for i in range(0, adaboost_runs):
        Adaboost_algorythem(K ,dataSet)
        totalTrainErrorList += EmpirError
        totalTestErrorList += Error

    for k in range(0, K):
        outputString += addOutput(totalTrainErrorList[k] / adaboost_runs, totalTestErrorList[k] / adaboost_runs, k + 1)

