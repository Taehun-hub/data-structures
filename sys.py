import sys
A=[]
print(sys.getsizeof(A)) #56
A.append(10)
print(sys.getsizeof(A)) #88