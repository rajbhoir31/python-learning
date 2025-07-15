# try:
#     num = int(input("Enter a number: "))
#     result = 10 / num
#     print("Result:", result)
# except ValueError:
#     print("Please enter a valid number!")
# except ZeroDivisionError:
#     print("You can't divide by zero.")




# try:
#     num = int(input("Enter a number: "))
# except ValueError:
#     print("Not a number!")
# else:
#     print("Square is:", num ** 2)
# finally:
#     print("This always runs.")



try:
    age = int(input("Enter your age: "))
    if age < 0:
        raise ValueError("Age can't be negative")
except ValueError as e:
    print("Error:", e)
else:
    print("Thank you, age recorded.")
finally:
    print("Validation done.")
