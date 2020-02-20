fileBases = ["a_example","b_read_on","c_incunabula","d_tough_choices","e_so_many_books","f_libraries_of_the_world"]

def genRes(fileBase):
    fileIn = open(fileBase+".txt","r")
    lines = [[int(j) for j in i.split()] for i in fileIn.readlines()]
    fileIn.close()
    # line 1 is number of books + number of libraries + number of days
    num_books = lines[0][0]
    num_libraries = lines[0][1]
    num_days = lines[0][2]
    # line 2 is book scores
    bookScores = lines[1]
    # 2 lines per library:
    #   1. number of books + signup cost + books per day
    #   2. IDs of the books
    library_data = []
    for i in range(2,num_libraries*2+1,2):
        library_data.append([lines[i], lines[i+1]])
    print(len(library_data),num_libraries)

for f in fileBases:
    genRes(f)