def sum2(A,n)
    sum=0
    for i in range(0,n-1):
        for j=i to n-1 do
            sum+=A[i]*A[j]
    return sum