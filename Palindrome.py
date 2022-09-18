N=int(input())
rev=0
temp=N
while N>0:
    digit=N%10
    rev=rev*10+digit
    N=N//10
if temp==rev:
    print("True")
else:
    print("False")