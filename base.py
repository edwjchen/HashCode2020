fileBases = ["a_example","b_read_on","c_incunabula","d_tough_choices","e_so_many_books","f_libraries_of_the_world"]

def genRes(fileBase):
    fileIn = open(fileBase+".txt","r")
    lines = [[int(j) for j in i.split()] for i in fileIn.readlines()]
    fileIn.close()
    # line 1 is number of books + number of libraries + number of days
    num_books = lines[0][0]
    num_libraries = lines[0][1]
    num_days = lines[0][2]
    # line 2 is book scores (dict mapping id to value)
    bookScores = {ind : val for ind,val in enumerate(lines[1])}

    booksToLibrary = {}
    # 2 lines per library:
    #   1. number of books + signup cost + books per day
    #   2. IDs of the books
    library_data = []
    for i in range(2,num_libraries*2+1,2):
        library_data.append([lines[i], lines[i+1]])
    print(library_data)

    heuristics = []
    for index,libraryDat in enumerate(library_data):
        for i in libraryDat[1]:
            if i in booksToLibrary:
                booksToLibrary[i].append(index)
            else:
                booksToLibrary[i] = [index]
        totScore = sum([bookScores[i] for i in libraryDat[1]])
        heuristic = (libraryDat[0][1]+totScore/libraryDat[0][2])
        daysToWork = num_days - libraryDat[0][1]
        heuristic/=libraryDat[0][1]
        #libraryDat.append([heuristic,daysToWork])
        heuristics.append([index, heuristic, daysToWork])
    
    heuristics.sort(key=lambda x: x[1])
    print(heuristics)
    print(library_data)

def genFile(libraryOrder,bookOrderPerLibrary,fileBase):
    # libraryOrder = list of library order
    # bookOrderPerLibrary = sorted list of book IDs per library
    # fileBase = outpute file base
    fileOut = open(fileBase+".out","w")
    fileOut.write(str(len(libraryOrder))+"\n")
    for id in libraryOrder:
        fileOut.write(str(id)+" "+str(len(bookOrderPerLibrary[id]))+"\n")
        fileOut.write(" ".join(bookOrderPerLibrary[id])+"\n")
    fileOut.close()


def caculateHeuristics(libraryDat,bookScores,booksScanned,num_days,index):
    daysToWork = num_days - libraryDat[0][1]
    totScore = 0
    for i in libraryDat[1]:
        if i not in booksScanned:
            totScore += bookScores[i]
    heuristic = (libraryDat[0][1]+totScore/libraryDat[0][2])/libraryDat[0][1]
    return [index, heuristic, daysToWork]



genRes(fileBases[0])