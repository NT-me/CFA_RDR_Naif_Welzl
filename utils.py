import math
import random as r
from Objet.point import Point
from Objet.cercle import Cercle


def crossproduct(p, q, s, t):
    return(((q.x-p.x)*(t.y-s.y))-((q.y-p.y)*(t.x-s.x)))


def generateRanPoints(nbre: int):
    res = []
    for i in range(0, nbre):
        res.append(Point(r.randint(0, 9999), r.randint(0, 9999)))
    return res


def verifToutPoints(listOfPoint: list, C: Cercle):
    res = []
    for lop in listOfPoint:
        if not C.contient(lop):
            res.append(lop)
    return res


def norme(a: Point):
    return (a.x * a.x) + (a.y * a.y)


def cercle3pts(A: Point, B: Point, C: Point):
    d = (A.x * (B.y - C.y) + B.x * (C.y - A.y) + C.x * (A.y - B.y)) * 2
    if d == 0:
        return None
    x = ((norme(A) * (B.y - C.y)) + (norme(B) * (C.y - A.y)) + (norme(C) * (A.y - B.y)))/d
    y = ((norme(A) * (C.x - B.x)) + (norme(B) * (A.x - C.x)) + (norme(C) * (B.x - A.x)))/d

    P = Point(x, y)

    return Cercle(P, P.distance(A))
