from Objet.point import Point
from Objet.cercle import Cercle


def trouverDiametre(listPoint: list):
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
    res = Cercle(None, None)
    diam = trouverDiametre(listPoint)
    res.initFromDiametre(diam[0], diam[1])
    return res
