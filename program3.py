# Program 3
table = []
def multiplicationTable(n):
    for i in range(n):
        nlist = [j*(i+1) for j in range(1,n+1)]
        table.append(nlist)

    for i in range(n):
        print(table[i])

multiplicationTable(4)
