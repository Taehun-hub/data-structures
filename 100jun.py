x,y=list(input().split())
count=0
save=[]
if len(x)==len(y):
    for i in range(len(x)):
        if x[i]!=y[i]:
            count=count+1
    print(count)
elif len(x)<len(y):
    for i in range(len(y)-len(x)+1):
        count2=0
        z=y[i:i+len(x)]
        for j in range(len(z)):
            if z[j]!=x[j]:
                count2=count2+1
        save.append(count2)
    print(min(save))









