class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def distance(self):
        # Distance from origin: sqrt(x^2 + y^2)
        return float((self.x ** 2 + self.y ** 2) ** 0.5)

    def is_origin(self):
        # True if point is (0, 0)
        return self.x == 0 and self.y == 0

    def on_xaxis(self):
        # On x-axis if y = 0
        return self.y == 0

    def on_yaxis(self):
        # On y-axis if x = 0
        return self.x == 0

    def quadrant(self):
        # Assume: point is not on either axis
        if self.x > 0 and self.y > 0:
            return 'first'
        elif self.x < 0 and self.y > 0:
            return 'second'
        elif self.x < 0 and self.y < 0:
            return 'third'
        else:
            return 'fourth'

    def slope(self):
        # Assume: point is not on y-axis, so x != 0
        return self.y / self.x
