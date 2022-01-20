import math
from tuple import *
from matrix_to_tex import *
from csv_parser.py import *

#käytössä oleva versio, joka käyttää tupleja ns. ratinoaalilukuina
def gauss_elim_tuple(A):
    res = []
    #print_matrix_tuple(res[0])
    copyA = []
    for row in A:
        temp = []
        for item in row:
            temp.append(item)
        copyA.append(temp)
    res.append(copyA)
    i=0
    j=0
    m = len(A)
    n = len(A[0])
    while (i < m and j < n):
        max_val = A[i][j]
        max_row = i
        for k in range(i+1, m):
            value = A[k][j]
            if (tuple_abs(value) > tuple_abs(max_val)):
                max_val = value
                max_row = k
        if(not (max_val[0] == 0)):
            temp1 = A[i]
            temp2 = A[max_row]
            A[i]=temp2
            A[max_row]=temp1
            res.append(A[:][:])
            for x in range(0, len(A[i])):
                A[i][x] = div(A[i][x], max_val)
            for u in range(0, m):
                if (not (u == i)):
                    temp = [multiply(multiply(A[u][j], A[i][x]), (-1, 1)) for x in range(0, n)]
                    A[u] = [add(temp[x],A[u][x]) for x in range(0, n)]
            i = i + 1
            #print_matrix_tuple(A) vanha debuggaus
            res.append(A[:][:])
        j = j + 1
    return res


#debuggausta tuple-funktiolle  
def print_matrix_tuple(A):
    prows = []
    for row in range(0, len(A)):
        text = "["
        for item in range(0, len(A[row])):
            text = text + str(A[row][item]) + ","
        text = text + "]"
        prows.append(text)
    print("-----------------")
    for item in prows:
        print(item)
    print("-----------------")
    
#itse main-loop           
if __name__ == "__main__":
    A=[
        [2, 0, 6, 0, 10, 5],
        [2, 0, 6, 8, 0, 5],
        [2, 4, 0, 0, 0, 5],
        [1, -1, -1, 0, 0, 0],
        [0, 0, 1, -1, -1, 0]
        ]
    for row in range(0, len(A)):
        for item in range(0, len(A[row])):
            A[row][item] = (A[row][item], 1)
    res = gauss_elim_tuple(A)
    #for item in res:
    #    print_matrix_tuple(item)

    full_latex(res)

