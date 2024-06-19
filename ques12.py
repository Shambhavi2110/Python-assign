num = int(input("Enter a number: "))
sum = 0
while(num>0):
    lastDigit = int(num%10)
    sum = int(sum + lastDigit)
    num = int(num/10)
print(sum)

