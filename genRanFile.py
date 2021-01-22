import utils as u

if __name__ == "__main__":
    OP = {**u.generateRanPoints(10), **u.generateRanPoints(20)
    , **u.generateRanPoints(30), **u.generateRanPoints(40)
    , **u.generateRanPoints(50), **u.generateRanPoints(60)
    , **u.generateRanPoints(70), **u.generateRanPoints(80)
    , **u.generateRanPoints(90), **u.generateRanPoints(100)}
    for namelistOfPoint in OP:
        listOfPoint = OP[namelistOfPoint]
        file = open("OpenFile/baseDeTest/"+namelistOfPoint+".points", "w", newline='')
        for pt in listOfPoint:
            file.write("{0} {1}\n".format(pt.x, pt.y))
        file.close()
