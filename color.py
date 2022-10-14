class Color(object):
    def __init__(self, r, g, b):

        self.r = r
        self.g = g
        self.b = b

    def __repr__(self):
            return str(bytes([self.b, self.g, self.r]))

    def multiply(self, other):

        min = 0
        max = 255

        return Color(
            self.minmax_color(self.r * other.r),
            self.minmax_color(self.g * other.g),
            self.minmax_color(self.b * other.b)
        )

    def minmax_color(self, value):
        if (0 < value < 255):
            return value
        if (value < 0):
            return 0
        if (value > 255):
            return 255

col = Color(0, 45, 65)
print(col)

col2 = Color(5, 0, 255)
print(col2)

col3 = col.multiply(col2)
print(col3)