from vector import *

class M4(object):
    def __init__(self, data = None):
        self.data = [
                    [0, 0, 0, 0],
                    [0, 0, 0, 0],
                    [0, 0, 0, 0],
                    [0, 0, 0, 0]
                    ]

        if data:
            for x in range(len(data)):
                for y in range(len(data[x])):
                    if (type(y) == int or type(y) == float ):
                        self.data[x][y] = data[x][y]

    
    def __repr__(self):
        retSting = ""
        for x in (self.data):
            retSting += '| ' + str(x[0]) + '\t' + str(x[1]) + '\t' + str(x[2]) + '\t' + str(x[3]) + ' |\n'
        return retSting

    def __mul__(self, other):

        if (type(other) == M4):

            Newdata = [
                    [0, 0, 0, 0],
                    [0, 0, 0, 0],
                    [0, 0, 0, 0],
                    [0, 0, 0, 0]
                    ]

            for x in range(4):
                for y in range(4):
                    Newdata[x][y] = self.data[x][0] * other.data[0][y] + self.data[x][1] * other.data[1][y] + self.data[x][2] * other.data[2][y] + self.data[x][3] * other.data[3][y]

            self.data = Newdata

            return self

        if (type(other) == int or type(other) == float):
            for x in range(len(self.data)):
                for y in range(len(self.data[x])):
                    self.data[x][y] *= other

        if (type(other) == V4):
            
            Newdata = [0, 0 , 0, 0]

            for x in range(3):
                Newdata[x] = self.data[x][0] * other.x + self.data[x][1] * other.y + self.data[x][2] * other.z + self.data[x][3] * other.w

            return V4(Newdata[0], Newdata[1], Newdata[2], Newdata[2])

    def __add__(self, other):

        if (type(other) == M4):
            
            for x in range(len(self.data)):
                for y in range(len(self.data[x])):
                    self.data[x][y] += other.data[x][y]

            return self


    def identity(self):

        for x in range(4):
            for y in range(4):
                if (x == y):
                    self.data[x][y] = 1
                else:
                    self.data[x][y] = 0

        return self

class M3(object):
    def __init__(self, data = None):
        self.data = [
                    [0, 0, 0],
                    [0, 0, 0],
                    [0, 0, 0]
                    ]

        if data:
            for x in range(len(data)):
                for y in range(len(data[x])):
                    if (type(y) == int or type(y) == float ):
                        self.data[x][y] = data[x][y]

    
    def __repr__(self):
        retSting = ""
        for x in (self.data):
            retSting += '| ' + str(x[0]) + '\t' + str(x[1]) + '\t' + str(x[2]) + ' |\n'
        return retSting

    def __mul__(self, other):

        if (type(other) == M3):

            Newdata = [
                    [0, 0, 0],
                    [0, 0, 0],
                    [0, 0, 0]
                    ]

            for x in range(3):
                for y in range(3):
                    Newdata[x][y] = self.data[x][0] * other.data[0][y] + self.data[x][1] * other.data[1][y] + self.data[x][2] * other.data[2][y]

            self.data = Newdata

            return self

        if (type(other) == int or type(other) == float):
            for x in range(len(self.data)):
                for y in range(len(self.data[x])):
                    self.data[x][y] *= other

        if (type(other) == V3):
            
            Newdata = [0, 0 , 0]

            for x in range(3):
                Newdata[x] = self.data[x][0] * other.x + self.data[x][1] * other.y + self.data[x][2] * other.z

            return V3(Newdata[0], Newdata[1], Newdata[2])

    def __add__(self, other):

        if (type(other) == M3):
            
            for x in range(len(self.data)):
                for y in range(len(self.data[x])):
                    self.data[x][y] += other.data[x][y]

            return self


    def identity(self):

        for x in range(3):
            for y in range(3):
                if (x == y):
                    self.data[x][y] = 1
                else:
                    self.data[x][y] = 0

        return self

class M2(object):
    def __init__(self, data = None):
        self.data = [
                    [0, 0],
                    [0, 0],
                    ]

        if data:
            for x in range(len(data)):
                for y in range(len(data[x])):
                    if (type(y) == int or type(y) == float ):
                        self.data[x][y] = data[x][y]

    
    def __repr__(self):
        retSting = ""
        for x in (self.data):
            retSting += '| ' + str(x[0]) + '\t' + str(x[1]) + ' |\n'
        return retSting

    def __mul__(self, other):

        if (type(other) == M2):

            Newdata = [
                    [0, 0],
                    [0, 0],
                    ]

            for x in range(2):
                for y in range(2):
                    Newdata[x][y] = self.data[x][0] * other.data[0][y] + self.data[x][1] * other.data[1][y] 

            self.data = Newdata

            return self

        if (type(other) == int or type(other) == float):
            for x in range(len(self.data)):
                for y in range(len(self.data[x])):
                    self.data[x][y] *= other

        if (type(other) == V3):
            
            Newdata = [0, 0]

            for x in range(2):
                Newdata[x] = self.data[x][0] * other.x + self.data[x][1] * other.y

            return V3(Newdata[0], Newdata[1])

    def __add__(self, other):

        if (type(other) == M2):
            
            for x in range(len(self.data)):
                for y in range(len(self.data[x])):
                    self.data[x][y] += other.data[x][y]

            return self


    def identity(self):

        for x in range(2):
            for y in range(2):
                if (x == y):
                    self.data[x][y] = 1
                else:
                    self.data[x][y] = 0

        return self
