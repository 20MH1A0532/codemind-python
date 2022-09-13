N=int(input())
a=list(input().split())
digit=[]
for i in a:
    digit.append(len(i))
maxlen=max(digit)
print(digit.count(maxlen))