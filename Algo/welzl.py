from Objet.point import Point
from Objet.cercle import Cercle
import random as ran
import utils as u


def Welzl(points: list):
    contour = []
    return bMinDisk(points, contour)


def bMinDisk(points_: list, contour: list):
    """
    Récursion de l'algo de Welzl
    """
    points = points_.copy()
    D = Cercle(Point(0, 0), 0)

    if not points or len(contour) == 3:
        return bmd([], contour)
    else:
        p = points[ran.randint(0, len(points)-1)]
        points.remove(p)
        D = bMinDisk(points, contour)
        if D and not D.contient(p):
            contour.append(p)
            D = bMinDisk(points, contour)
            contour.remove(p)
    return D


def bmd(points: list, contour: list):
    """
    Dessine un cercle de rayon minimum avec les résultats de Welzl
    """
    if not points and len(contour) == 0:
        # Cas où c'est vide du coup cercle arbitraire
        return Cercle(Point(0, 0), 10)

    elif len(contour) == 1:
        return Cercle(contour[0], 0)

    elif len(contour) == 2:
        C = Cercle(Point(0, 0), 0)
        C.initFromDiametre(contour[0], contour[1])
        return C

    elif len(contour) == 3:
        return u.cercle3pts(contour[0], contour[1], contour[2])

    else:
        # Wat
        return -1
