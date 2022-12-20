import numpy as np
import matplotlib.pyplot as plt

def Perceptron(X, Y, epoch=100):
    weights = np.zeros(2, dtype=float)
    guessPlusOrMinus = 0
    count_error = 0
    flag = 0
    for i in range(epoch):
        if flag == 0:
            flag = 1
            for labels, point in enumerate(X):
                if np.dot(weights, point) > 0:
                    guessPlusOrMinus = 1
                else:
                    guessPlusOrMinus = -1
                if guessPlusOrMinus != Y[labels]:
                    flag = 0
                    count_error += 1
                    weights += Y[labels] * np.squeeze(np.asarray(point))
                    break
        else:
            break
    return count_error, weights


if __name__ == '__main__':
    file = open("two_circle.txt", "r")
    list_nodes = []
    X = []
    Y = []
    for point in file:
        XYZ = point.split()
        list_nodes.append([float(XYZ[0]), float(XYZ[1]), float(XYZ[2])])
        X.append([float(XYZ[0]), float(XYZ[1])])
        Y.append(float(XYZ[2]))

    P = Perceptron(X, Y, epoch=100)
    print(P)


