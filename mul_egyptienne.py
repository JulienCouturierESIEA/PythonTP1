number1 = int(input())
number2 = int(input())
result = 0

while(number1 != 0):
    if(number1%2 == 1):
        result += number2
    number2 += number2
    number1 //= 2
print(result)