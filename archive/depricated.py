#vanha koodi funktiolle. Huomattavasti tehokkaampi suurilla matriiseilla,
#mutta ei anna rationaalilukuvastauksia, mikä tekee siitä melko kehnon
def gauss_elim(A):
    res = []
    i=0
    j=0
    m = len(A)
    n = len(A[0])
    while (i < m and j < n):
        max_val = A[i][j]
        max_row = i
        for k in range(i+1, m):
            value = A[k][j]
            if (abs(value) > abs(max_val)):
                max_val = value
                max_row = k
        if(not (max_val == 0)):
            temp1 = A[i]
            temp2 = A[max_row]
            A[i]=temp2
            A[max_row]=temp1
            for x in range(0, len(A[i])):
                A[i][x] = A[i][x]/max_val
            for u in range(0, m):
                if (not (u == i)):
                    temp = [-A[u][j]*A[i][x] for x in range(0, n)]
                    A[u] = [temp[x]+A[u][x] for x in range(0, n)]
            i = i + 1
            print_matrix(A)
        j = j + 1
    return A


#debuggausta varten
def print_matrix(A):
    biggest = max([max(x) for x in A])
    chars = len(str(biggest))
    chars_matrix = []
    for row in A:
        temp = []
        for item in row:
            temp.append(len(str(item)))
        chars_matrix.append(temp)
    prows = []
    for row in range(0, len(A)):
        text = "["
        for item in range(0, len(A[row])):
            text = text + (chars - chars_matrix[row][item])*" " + str(A[row][item]) + ","
        text = text + "]"
        prows.append(text)
    print("-----------------")
    for item in prows:
        print(item)
    print("-----------------")