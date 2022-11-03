def is_happy(n):
    rev=sum=0
    while n>0:
        rev=n%10
        sum+=rev**2
        n=n//10
    return sum
n=int(input())
res=n
while (res!=1) and (res!=4):
    res=is_happy(res)
if (res==1):
    print("True")
elif (res==4):
    print("False")