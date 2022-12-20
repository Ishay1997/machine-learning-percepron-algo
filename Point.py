# python 3.7

class Point:
    """
        this class represents a point in the data set
        parameters:
        x, y, label and a weight.
    """

    def __init__(self, x=0, y=0, tag=0):
        self.x = float(x)
        self.y = float(y)
        self.label = int(tag)
        self.weight = 0

    def getx(self):
        return self.x

    def setx(self,x):
        self.x=x

    def gety(self):
        return self.y

    def sety(self,y):
        self.y=y

    def get_weight(self):
        return self.weight 

    def set_weight(self, weight):
        self.weight = weight

    def get_label(self):
        return self.label

    def set_label(self,label):
        self.label=label