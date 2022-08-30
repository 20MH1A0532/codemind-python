n=list(input())
if len(n)==n.count('9'):
    print("".join(n))
else:
    n[n.index('6')]='9'
    print("".join(n))