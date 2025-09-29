def splice(self,a,b,x):
    #조건1: a-> ... -> b
    #조건2: a와b 사이에 head, x 존재 안 함
    ap=a.prev,bn=b.next,xn=x.next
    ap.next=bn
    bn.prev=ap
    x.next=bn
    a.prev=x
    b.next=xn
    xn.prev=b