n=int(input())
n=str(n)
s=set(n)
if len(n)>len(s):
    print("Not Unique Number")
else:
    print("Unique Number")