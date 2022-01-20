import math

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