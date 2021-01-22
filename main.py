from Objet.point import Point
from Objet.cercle import Cercle
from Algo import naif as an
from Algo import welzl as we
from OpenFile import executiveOF as eof
import time
import utils as u
import csv


if __name__ == "__main__":

    OP = eof.openTestBase('*')
    for namelistOfPoint in OP:
        file = open("rapport/"+namelistOfPoint+".csv", "w", newline='')
        writer = csv.writer(file)
        listOfPoint = OP[namelistOfPoint]

        ### Algorithme naïf
        print("\n\n === Naïf === \n\n")
        start_time = time.time()
        resC = an.algoNaif(listOfPoint)
        interval = time.time() - start_time

        print("\n=========\nTps pour {0} pts : {1}s".format(len(listOfPoint), interval))
        print(resC)
        VTP = u.verifToutPoints(listOfPoint, resC)
        ptPerdu = "EMPTY"
        if VTP:
            ptPerdu = ""
            for pt in VTP:
                ptPerdu+="||{0}|{1}||".format(str(pt), pt.distance(resC.centre))
                print("\n====")
                print(pt.distance(resC.centre))
                print(pt)
        writer.writerow(["N", len(listOfPoint), interval, str(resC), ptPerdu])

        ### Algorithme de Welzl
        print("\n\n === Welzl === \n\n")
        lopCopy = listOfPoint.copy()

        start_time = time.time()
        resC = we.Welzl(lopCopy)
        interval = time.time() - start_time

        print("\n=========\nTps pour {0} pts : {1}s".format(len(listOfPoint), interval))
        print(resC)
        VTP = u.verifToutPoints(listOfPoint, resC)
        ptPerdu = "EMPTY"
        if VTP:
            ptPerdu = ""
            for pt in VTP:
                ptPerdu+="||{0}|{1}||".format(str(pt), pt.distance(resC.centre))
                print("\n====")
                print(pt.distance(resC.centre))
                print(pt)
        writer.writerow(["W", len(listOfPoint), interval, str(resC), ptPerdu])
