// Naive approach
def fre(myList):
    table = {}
    finale = 0
    for row in myList:
        if(row in table):
            table[row] -= 1
        else:
            table[row] = 1
    for i in table:
        if i > 0:
            finale = i
    return finale 

print(fre([1,2,3,4,3,2,1]))

// Improved algorithm
def Unique(myList):
    finale = 0
    for i in myList:
        finale ^= i
    return finale 
print(Unique([1,2,3,4,3,1,2]))
