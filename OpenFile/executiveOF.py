from Objet.point import Point
import os


def openTestBase(value):
    fileListe = os.listdir(os.getcwd()+"/OpenFile/baseDeTest")
    listfilePoint = list()
    i = 0
    if value == "*":
        value = len(fileListe)

    for fichier in fileListe:
        i = i + 1
        if i > value:
            break

        filePoint = list()
        with open(os.getcwd()+"/OpenFile/baseDeTest/"+fichier) as f:
            content = f.read()
            contentPreParse = content.split("\n")
            for ligne in contentPreParse:
                token = ligne.split(" ")
                if len(token) == 2:
                    filePoint.append(Point(int(token[0]), int(token[1])))

            listfilePoint.append(filePoint)
    return listfilePoint
