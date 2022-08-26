n=int(input())
sum=0
prd=1
while n:
    a=n%10
    sum=sum+a
    prd=prd*a
    n=n//10
print(prd-sum)