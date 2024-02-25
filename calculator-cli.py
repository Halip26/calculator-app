# Key things about functions:
# 1. Functions are reusable
# 2. Functions can take input
# 3. Functions can return output
# 4. Functions can be named
import time


def addition(aku, kamu):
    return aku + kamu


def substraction(aku, kamu):
    return aku - kamu


def multiplication(aku, kamu):
    return aku * kamu


def division(aku, kamu):
    return aku / kamu


while True:
    print("\n-- Welcome to CLI calculator --")
    a = int(input("Enter the first number: "))
    b = int(input("Enter the second number: "))

    print("-" * 45)

    print("Press 1 for addition")
    print("Press 2 for substraction")
    print("Press 3 for multiplication")
    print("Press 4 for division")
    print("Press 5 for exit/quit")

    print("-" * 45)

    user_choice = int(input("Enter your choice: "))

    if user_choice == 1:
        result = addition(a, b)
        time.sleep(0.5)
        print(f"The result is {result}")
    elif user_choice == 2:
        time.sleep(0.5)
        result = substraction(a, b)
        print(f"The result is {result}")
    elif user_choice == 3:
        time.sleep(0.5)
        result = multiplication(a, b)
        print(f"The result is {result}")
    elif user_choice == 4:
        time.sleep(0.5)
        result = division(a, b)
        print(f"The result is {result}")
    elif user_choice == 5:
        time.sleep(0.5)
        print("You have exited the calculator, Bye!")
        break
    else:
        time.sleep(0.5)
        print("Invalid input, try again!")
