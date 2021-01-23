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
    listPoint = set(listPoint)
    PQ_notRet = set()
    for p in listPoint:
        for q in listPoint:
            if p is not None and q is not None and p != q and (p, q) not in PQ_notRet:
                PQ_notRet.add((p, q))
                PQ_notRet.add((q, p))
                newC = Cercle(None, None)
                newC.initFromDiametre(p, q)
                if u.verifToutPoints(listPoint, newC):
                    return newC

    res = Cercle(None, math.inf)
    PQR_notRet = set()
    for p in listPoint:
        for q in listPoint:
            for r in listPoint:
                if p != q and p != r and q != r and (p, q, r) not in PQR_notRet:
                    PQR_notRet.add((p, q, r))
                    PQR_notRet.add((r, p, q))
                    PQR_notRet.add((q, r, p))
                    C = u.cercle3pts(p, q, r)
                    if C:
                        if C.rayon < res.rayon and u.verifToutPoints(listPoint, C):
                            res = C

    return res
