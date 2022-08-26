p,r,t=map(int,input().split())
c_i=p*(1+(r/100))**t
print('{:.2f}'.format(c_i))