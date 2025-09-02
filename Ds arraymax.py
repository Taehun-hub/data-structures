def arraymax(A,n):
    currentMax = A[0]
    for i in range(1,n-1):
        if A[i] > currentMax:
            currentMax = A[i]
    return currentMax
