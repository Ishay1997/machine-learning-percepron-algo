# python 3.7
# coding: utf-8

from Point import Point

class hypothesis:
    """
        this class represents the set of rules on our dataset of points.
        each rule is a line between two points
    """

    def __init__(self, point1=Point(), point2=Point()):
        self.point1 = point1
        self.point2 = point2
        if point1.getx() - point2.getx() == 0:
            self.m = 0
            self.n = 0
            self.vertical = True
        else:
            self.m = (point1.gety() - point2.gety()) / (point1.getx() - point2.getx())
            self.n = point1.gety() - (self.m * point1.getx())
            self.vertical = False


    def classify(self, otherPoint):
        """
            This function classify between my point and the other point to get the label (-1/1).
        """
        if self.vertical:
            if otherPoint.getx() >= self.point1.getx():
                return 1
            else:
                return -1
        else:
            resultOfY = (self.m * otherPoint.getx()) + self.n
            if otherPoint.gety() >= resultOfY:
                return -1
            else:
                return 1
        