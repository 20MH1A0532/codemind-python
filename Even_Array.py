def is_even(l):
    for i in l:
        if i%2==0:
            continue
        else:
            return False
    return True
n=int(input())
l=list(map(int,input().split()))
print(is_even(l))