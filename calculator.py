print("CALCULATOR")


num1=int(input("enter your first number here: "))
num2=int(input("enter your second number here: "))

print("press 1 for addition \npress 2 for subtraction \npress 3 for multiplication \npress 4 for division")
choice=int(input("Enter your choice here from 1-4:"))

if choice == 1:
    print("The addition of two numbers is", num1+num2)
elif choice == 2:
    print("The subtraction of two numbers is", num1-num2)
elif choice == 3:
    print("The multiplication of two numbers is", num1 * num2)
elif choice == 4:
    print("The division of two numbers is", num1/num2)
else:
    print("Invalid Input")
