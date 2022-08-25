import math
x,y,z=map(int,input().split())
p=math.pow(x,y)
m=p%z
print(int(m))