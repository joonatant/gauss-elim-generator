import math

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

#määritelmät tupplejen laskutoimituksille
def div(a, b):
    """
    n = multiply(a, (b[1], b[0]))
    k = math.gcd(n[0], n[1])
    if(k > 1):
        return (round(n[0]/k), round(n[1]/k))
    else:
    """
    return multiply(a, (b[1], b[0]))

def add(a, b):
    n = math.lcm(a[1], b[1])
    am = n/a[1]
    bm = n/b[1]
    return simplify_tuple((round(am*a[0] + bm*b[0]), n))
        
def multiply(a, b):
    return simplify_tuple((a[0]*b[0], a[1]*b[1]))

def tuple_abs(a):
    return abs(a[0]/a[1])

def simplify_tuple(a):
    res = a
    if(res[0] == 0):
        res = (0, 1)
    else:
        k = math.gcd(res[0], res[1])
        if(k > 1):
            res = (round(res[0]/k), round(res[1]/k))
        if (a[0] < 0 and a[1] < 0):
            res =(-res[0], -res[1])
    return res


def matrix_latex_gen(A, num=0):
    rows = len(A)
    rowlen = len(A[0])
    output = "\\[\n\\left[\n\\begin{array}{" + (rowlen-1)*"c" + "|c}\n"
    for n in range(0, rows):
        temp = ""
        for m in range(0, rowlen):
            if(m == rowlen - 1):
                temp = temp + tuple_to_tex(A[n][m]) + " \\\\\n"
            else:
                temp = temp + tuple_to_tex(A[n][m]) + " & "
        output = output + temp
    title = ""
    if(num>0):
        title = "(" + str(num) + ")"
    output = output + "\\end{array}\n\\right]"+ title +"\n\\]\n"
    return output

def full_latex(total, fileName="gauss.tex"):
    begin = "\\documentclass{article}\n\\usepackage{amsmath}\n\\begin{document}\n"
    matricies = [matrix_latex_gen(total[i], i+1) for i in range(0, len(total))]
    end = "\\end{document}"

    file = open(fileName, "w")
    file.write(begin)
    file.writelines(matricies)
    file.write(end)
    file.close()
    
    
    

def tuple_to_tex(a):
    if(a[1]==1):
        return str(a[0])
    else:
        return "\\dfrac{"+str(a[0])+"}{"+str(a[1])+"}"

def csv_to_matrix():
    #todo
    return 1
    
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

