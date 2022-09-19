A=int(input())
B=int(input())
for i in range(A,B+1):
    N=i
    flag=0
    while N:
        digit=N%10
        if digit==0 or i%digit!=0:
            flag=1
            break
        N=N//10
    if flag==0:
        print(i,end=' ')