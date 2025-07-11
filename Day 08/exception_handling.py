try:
    a = float(input("Enter a number: "))
    b = float(input("Enter another number: "))
    result = a / b
    with open("py.txt", "r") as file:
        content = file.read()
    print("File content:", content)

# Specific exception handling for division by zero and value errors
except ZeroDivisionError as zde:
    print("Error: Division by zero is not allowed.", zde)

except ValueError as ve:
    print("Invalid input! Please enter a valid number.", ve)

# General exception handling
except Exception as e:
    print("An unexpected error occurred:", e)

else:
    print("The result of the division is:", result)

finally:
    print("Execution completed. Thank you for using the program.")