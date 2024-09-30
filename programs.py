"""Create a program that defines variables of different data types (int, float, string, list, tuple, dictionary) and
prints their values and types."""
print()
age=25
print("age:",age,", Type of age ",age,type(age))

marks=99.8
print("marks:",marks,", Type of marks ",marks,type(marks))

name="Muskan"
print("name:",name,", Type of name",name,type(name) )

colors=["red","blue","black","green","yellow"]
print(colors, ", Type of colors" ,type(colors))

person={
    "name":"Muskan",
    "course":"BCA",
    "age":"19"
}
print(person,", type of ", person ,type(person))

range1=(10,20)
print(range1,", type of", range, type(range))

"""Write a program that takes a user input string and applies various string methods (e.g., upper(), lower(), title(), replace(),
split(), and find()). Print the results of each method."""

str1="muskan_gaur"

print(str1.upper())
print(str1.lower())
print(str1.title())
print(str1.replace("gaur","developer"))
print(str1.split("_"))
print(str1.find("a"))

"""Create a simple calculator program that takes two numbers and an operator (+, -, *, /) 
as input from the user, performs the operation, and prints the result."""

def add(a,b):
    return a+b
def subtract(a,b):
    return a-b
def multiply(a,b):
    return a*b
def divide(a,b):
    return a/b

def calculator():
    print("select the operator")
    print("1.Addition")
    print("2.Subtraction")
    print("3.Multiply")
    print("4.Divide")

while True:
        choice = input("Enter choice (1/2/3/4 ): ")
        
        if choice in ['1', '2', '3', '4']:
            try:
                num1 = float(input("Enter First Number: "))
                num2 = float(input("Enter Second Number: "))
            except ValueError:
                print("Invalid Input! Please enter numeric values.")
                continue

            if choice == '1':
                print(f"{num1} + {num2} = {add(num1, num2)}")
            elif choice == '2':
                print(f"{num1} - {num2} = {subtract(num1, num2)}")
            elif choice == '3':
                print(f"{num1} * {num2} = {multiply(num1, num2)}")
            elif choice == '4':
                print(f"{num1} / {num2} = {divide(num1, num2)}")
        else:
            print("Invalid Input! Please select a valid operation.")

        next_calculation = input("Do you want to perform another calculation? (yes/no): ")
        if next_calculation.lower() != 'yes':
            break

"""
Write a program that checks if a number entered by the user is even or odd, and prints the result.
 Extend it to check if the number is positive, negative, or zero."""
number =int(input("Enter any number"))
if number!=0 and number.is_integer():
    if(number%2==0):
        print(number,"is even")
    else:
        print(number,"is odd")
else:
    if number!=0 :
        print("the no. is not an integer")


if(number<0 ):
    print(number,"is negative")
elif(number>0):
    print(number,"is positive")
else:
        print(number,"is zero")


# Create a program that prints the multiplication table for a number provided by the user (from 1 to 10).
num = int(input("Enter any number: "))
for i in range(1, 11):
    print(num, "X", i, "=", num * i)


""" Write a program that repeatedly asks the user to input a number until they input a number greater than 100. 
 Print the total sum of all entered numbers."""

number=int(input("enter any number:"))

sum_of_numbers = 0  

while True:
    number = int(input("Enter any number: "))  
    if number > 100:
        break  
    sum_of_numbers += number  

print("Sum of all entered values:", sum_of_numbers)  
