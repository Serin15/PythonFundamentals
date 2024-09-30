#You can handle errors in Python using try, except, and finally.

try:
    x = int(input("Enter a number: "))
    print(10 / x)
except ZeroDivisionError:
    print("You cannot divide by zero!")
except ValueError:
    print("Please enter a valid number!")
finally:
    print("This will always execute.")
