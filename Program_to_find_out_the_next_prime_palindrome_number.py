def is_prime(num):
    if num<2:
        return False
    for i in range(2,int(num**0.5)+1):
        if num%i==0:
            return False
    return True
def is_pald(num):
    rev=0
    while num>0:
        rem=num%10
        rev=rev*10+rem
        num=num//10
    return rev
n=int(input())
n+=1
while True:
    if n==is_pald(n) and is_prime(n)==True:
        print(n)
        break
    n+=1