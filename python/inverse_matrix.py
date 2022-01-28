def insert(col, row):
    if (col==row):
        return (1, 1)
    else:
        return (0, 1)

def i_matrix(A):
    k = len(A)
    inverse = [[insert(col,row) for col in range(k)] for row in range(k)]
    
    for i in range(0, k):
        A[i].extend(inverse[i])
    
    return A