def s(n):
    sum=0
    for i in range(1,n):
        if n%i==0:
            sum=sum+i
    return sum
a=int(input())
b=int(input())
if s(a)==b and s(b)==a:
    print("Amicable")
else:
    print("Not Amicable")