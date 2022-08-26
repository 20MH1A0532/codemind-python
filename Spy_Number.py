n=int(input())
sum=0
prd=1
n1=n
while (n>0):
    a=n%10
    sum=sum+a
    prd=prd*a
    n=n//10
if sum==prd:
    print("Spy Number")
else:
    print("Not Spy Number")