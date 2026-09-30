# This function determines whether a number is even or odd
def check_number(number):
    if number % 2 == 0:
        return "even"
    else:
        return "odd"
    
# Ask the user to enter a whole number
number = int(input("Enter a whole number: "))

# Call the function and store the returned result
result = check_number(number)

# Display whether the number is even or odd
print(f"{number} is an {result} number.")