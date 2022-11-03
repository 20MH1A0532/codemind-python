n=input()
i=1
sum=0
for j in n:
    sum+=int(j)**i
    i+=1
print(sum==(int(n)))