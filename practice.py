fileBases = ["a_example","b_small","c_medium","d_quite_big","e_also_big"]

def genRes(fileBase):
    fileIn = open(fileBase+".in","r")
    lines = [[int(j) for j in i.split()] for i in fileIn.readlines()]
    fileIn.close()

    target_slices = lines[0][0]
    num_pizza = lines[0][1]
    taken = []

    #greedy approach
    for p in reversed(range(0,len(lines[1]))):
        if lines[1][p]<=target_slices:
            target_slices-=lines[1][p]
            taken.insert(0,p)

    fileOut = open(fileBase+".out","w")
    fileOut.write(str(len(taken))+"\n")
    pizzas = " ".join([str(i) for i in taken])
    fileOut.write(pizzas)
    fileOut.close()

for f in fileBases:
    genRes(f)