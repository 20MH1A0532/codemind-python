n=int(input())
l=[]
for i in range(0,n):
    a,b=map(int,input().split())
    l.append(a)
    l.append(b)
for i in range(0,(2*n)-1,2):
    print(l[i]+l[i+1])
