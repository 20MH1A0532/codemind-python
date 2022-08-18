X,Y=map(int,input().split())
if X+1==Y or X==Y+1 or X==Y+9 or Y==X+9:
    print("Yes")
else:
    print("No")