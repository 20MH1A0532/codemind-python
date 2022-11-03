def is_prime(n):
    if n<2:
        return Flase
    for i in range(2,n):
        if n%i==0:
            return False
    return True
n=int(input())
l=[]
for i in range(2,n):
    if is_prime(i):
        l.append(i)
flag=0
for i in range(len(l)):
    for j in range(i+1,len(l)):
        if l[i]*l[j]==n:
            print(l[i],l[j])
            flag=1
            break
if flag==0:
    print("-1")