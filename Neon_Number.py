num = int(input())
sqr = num*num
sumOfDigit = 0
while sqr>0:
    a=sqr%10
    sumOfDigit =sumOfDigit+a
    sqr = sqr//10

if (num == sumOfDigit):
    print("Neon Number")
else:
    print("Not Neon Number")