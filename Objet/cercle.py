from Objet.point import Point


class Cercle(object):
    def __init__(self, centre: Point, rayon: int):
        self.centre = centre
        self.rayon = rayon

    def contient(self, p: Point):
        return self.centre.distance(p) <= self.rayon

    def initFromDiametre(self, A: Point, B: Point):
        newC = Point(0,0)
        newC.x = 0.5*(A.x + B.x)
        newC.y = 0.5*(A.y + B.y)
        newR = 0.5*(A.distance(B))

        self.centre = newC
        self.rayon = newR

    def __str__(self):
        return "Cercle [Centre :{0}, Rayon: {1} ]".format(str(self.centre), str(self.rayon))
