from Objet.point import Point
from Objet.cercle import Cercle
import math
import utils as u


def trouverC(listPoint: list):
    if len(listPoint) < 3:
        return None

    dummy = listPoint[0]
    dist = -1
    P = Point(0, 0)
    Q = Point(0, 0)
    for p in listPoint:
        tmp_dist = dummy.distance(p)
        if (tmp_dist > dist):
            dist = tmp_dist
            P = p

    dist = -1
    for q in listPoint:
        tmp_dist = P.distance(q)
        if (tmp_dist > dist):
            dist = tmp_dist
            Q = q

    return P, Q


def algoNaif(listPoint: list):
    C = Cercle(None, None)
    diam = trouverC(listPoint)
    C.initFromDiametre(diam[0], diam[1])
    if not u.verifToutPoints(listPoint, C):
        return C
    else:
        listPoint = set(listPoint)
        res = Cercle(None, math.inf)
        for p in listPoint:
            for q in listPoint:
                for r in listPoint:
                    C = u.cercle3pts(p, q, r)
                    if C:
                        if C.rayon < res.rayon and not u.verifToutPoints(listPoint, C):
                            res = C
        return res
