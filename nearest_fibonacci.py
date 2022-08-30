n=int(input())
n1,n2=0,1
n3=0
while True:
    n3=n1+n2
    n1=n2
    n2=n3
    if n3>n:
        break
if abs(n2-n)<abs(n1-n):
    print(n2)
elif abs(n2-n)>abs(n1-n):
    print(n1)
else:
    print(n1,n2)
    