import math
from objet import Point


def crossproduct(p, q, s, t):
    return(((q.x-p.x)*(t.y-s.y))-((q.y-p.y)*(t.x-s.x)))
