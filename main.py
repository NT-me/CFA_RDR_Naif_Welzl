from Objet.point import Point
from Objet.cercle import Cercle
from Algo import naif as an
from OpenFile import executiveOF as eof


if __name__ == "__main__":
    # A = Point(1, 0)
    # B = Point(2, 2)
    # C = Point(-1, 0)
    # D = Point(-1, 1)
    # E = Point(-3, 15)
    #
    # L = [A, B, C, D, E]
    # resC = an.algoNaif(L)
    OP = eof.openTestBase('*')
    print(OP[0][15])
