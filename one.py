try:
    # Ask the user for input and convert it to an integer
    number1 = int(input("Enter a number: "))
    number2 = int(input("Enter another number: "))
    
    # Attempt to divide the numbers
    result = number1 / number2

except ZeroDivisionError:
    # This runs if number2 is 0
    print("You cannot divide by zero!")

except ValueError:
    # This runs if the user enters something that isn't a whole number
    print("Please enter a valid number!")

else:
    # This runs ONLY if no errors occurred in the try block
    print("Division successful! Result is:", result)

finally:
    # This block always runs regardless of what happened above
    print("This block always runs.")
