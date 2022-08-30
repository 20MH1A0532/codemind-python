n=int(input())
l=list(map(int,input().split()))
sum=0
j=0
l.reverse()
for i in l:
    sum+=i*(2**j)
    j+=1
print(sum)
    