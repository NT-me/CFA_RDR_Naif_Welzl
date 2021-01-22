from Objet.point import Point
from Objet.cercle import Cercle
from Algo import naif as an
from Algo import welzl as we
from OpenFile import executiveOF as eof
import time
import utils as u

if __name__ == "__main__":

    print("\n\n === Naïf === \n\n")
    # OP = eof.openTestBase(1)
    OP = []
    OP.append(u.generateRanPoints(100))
    for listOfPoint in OP:

        start_time = time.time()
        resC = an.algoNaif(listOfPoint)
        interval = time.time() - start_time

        print("\n=========\nTps pour {0} pts : {1}s".format(len(listOfPoint), interval))
        print(resC)
        VTP = u.verifToutPoints(listOfPoint, resC)
        if VTP:
            for pt in VTP:
                print("\n====")
                print(pt.distance(resC.centre))
                print(pt)

    print("\n\n === Welzl === \n\n")
    # OP = eof.openTestBase(1)
    # OP = []
    # OP.append(u.generateRanPoints(990))
    for listOfPoint in OP:
        
        lopCopy = listOfPoint.copy()
        start_time = time.time()
        resC = we.Welzl(lopCopy)
        interval = time.time() - start_time

        print("\n=========\nTps pour {0} pts : {1}s".format(len(listOfPoint), interval))
        print(resC)
        VTP = u.verifToutPoints(listOfPoint, resC)
        if VTP:
            for pt in VTP:
                print("\n====")
                print(pt.distance(resC.centre))
                print(pt)
