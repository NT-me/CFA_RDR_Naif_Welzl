import math


class Point(object):
    def __init__(self, posx, posy):
        self.x = posx
        self.y = posy

    def __eq__(self, other):
        return ((other.x == self.x) and (other.y == self.y))

    def __ne__(self, other):
        return ((other.x != self.x) or (other.y != self.y))

    def __gt__(self, other):
        return ((other.x < self.x) or (other.y < self.y))

    def __lt__(self, other):
        return ((other.x > self.x) or (other.y > self.y))

    def __ge__(self, other):
        return ((other.x <= self.x) or (other.y <= self.y))

    def __le__(self, other):
        return ((other.x >= self.x) or (other.y >= self.y))

    def __str__(self):
        return "Point [x: "+str(self.x) + ", y: " + str(self.y) + "]"

    def __hash__(self):
        return hash((self.x, self.y))

    def distance(self, other):
        A = (other.x-self.x) * (other.x-self.x)
        B = (other.y-self.y) * (other.y-self.y)
        return math.sqrt(A+B)
