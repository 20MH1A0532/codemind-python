N=int(input()) 
max=0
while N>0:
    digit=N%10
    if max<digit:
        max=digit
    N=N//10
print(max)
