number1 = float(input("enter first number: "))
number2 = float(input("enter second number: "))

sum = number1 + number2
difference = (max(number2,number1)) - min(number1,number2)
product = number2 * number1
division = (max(number2,number1)) / min(number1,number2)

print(f"sum is: {sum}")
print(f"Difference is: {difference}")
print(f"Product is: {product}")
print(f"Division is: {division}")