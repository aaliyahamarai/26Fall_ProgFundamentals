# This function greets the user using their name
def greet_user(name):
    print(f"Hello, {name}! Welcome aboard.")
    
# Ask the user to enter their name
name = input("Enter your name")

#Call the function using the name entered by the user
greet_user(name)