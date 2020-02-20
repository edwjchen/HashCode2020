fileBases = ["a_example","b_read_on","c_incunabula","d_tough_choices","e_so_many_books","f_libraries_of_the_world"]

def genFile(libraryOrder,bookOrderPerLibrary,fileBase):
    # libraryOrder = list of library order
    # bookOrderPerLibrary = sorted list of book IDs per library
    # fileBase = outpute file base
    fileOut = open(fileBase+".out","w")
    fileOut.write(str(len(libraryOrder))+"\n")
    for id in libraryOrder:
        fileOut.write(str(id)+" "+str(len(bookOrderPerLibrary[id]))+"\n")
        bookOrderPerLibrary[id] = [str(x) for x in bookOrderPerLibrary[id]]
        fileOut.write(" ".join(bookOrderPerLibrary[id])+"\n")
    fileOut.close()

def genRes(fileBase):
    fileIn = open(fileBase+".txt","r")
    lines = [[int(j) for j in i.split()] for i in fileIn.readlines()]
    fileIn.close()
    # line 1 is number of books + number of libraries + number of days
    num_books = lines[0][0]
    num_libraries = lines[0][1]
    num_days = lines[0][2]
    # line 2 is book scores
    done_scanning = set()
    bookScores = {ind : val for ind,val in enumerate(lines[1])}
    book_scores = {}
    for i, x in enumerate(lines[1]):
        book_scores[i] = x

    # 2 lines per library:
    #   1. number of books + signup cost + books per day
    #   2. IDs of the books
    library_data = []
    for i in range(2,num_libraries*2+1,2):
        books = lines[i+1]
        sorted_books = [(i,book_scores[i]) for i in books]
        sorted_books.sort(key = lambda x: x[1]) 
        library_data.append([lines[i], sorted_books])

    
    
    #find unique number of books per library 
    # for i, data in enumerate(library_data):
    #     print(i)
    #     print(data)

    #find number of libraries
    #output books

    #assume list of libraries 
    #given first library
    #given second library

    heuristics = []

    for index,libraryDat in enumerate(library_data):
        totScore = sum([i[1] for i in libraryDat[1]])
        heuristic = (libraryDat[0][1]+totScore/libraryDat[0][2])
        daysToWork = num_days - libraryDat[0][1]
        heuristic/=libraryDat[0][1]
        #libraryDat.append([heuristic,daysToWork])
        heuristics.append([index, heuristic, daysToWork, libraryDat[0][2]])

    heuristics.sort(key = lambda x: x[1]) 
    lib_scan = {}
    final_libs = []
    for lib, score, days_left, tp in heuristics:
        final_libs.append(lib)
        for days in range(int(days_left)):
            if not library_data[lib][1]:
                break
            book = library_data[lib][1].pop(len(library_data[lib][1])-1)
            if lib not in lib_scan:
                lib_scan[lib] = []
            if book not in done_scanning:
                done_scanning.add(book[0])
                lib_scan[lib].append(book[0])

    genFile(final_libs, lib_scan ,"results/"+fileBase)

    # find number of days it can output books
    # write output 


    #number of libraries
    #repeat:
    #library ids + num books
    #list of books

    #output file 

    # fileOut = open(fileBase+".out","w")
    # fileOut.write(str(len(taken))+"\n")
    # pizzas = " ".join([str(i) for i in taken])
    # fileOut.write(pizzas)
    # fileOut.close()

for f in fileBases:
    genRes(f)