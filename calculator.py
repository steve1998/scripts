# Simple calculator script in shell
# May be extended to support other features as well as other libraries

# Add two numbers together.
def add(x, y):
    return x + y

# Subtract two numbers.
def min(x, y):
    return x - y

# Multiply two numbers.
def multiply(x, y):
    return x * y

# Divide two numbers.
def divide(x, y):
    return x / y

def main():
    check = True

    while True:
        try:
            x = float(input("Enter 1st number: "))
            y = float(input("Enter 2nd number: "))
        except ValueError:
            print("Please enter a valid input!")
        else:
            break

    result = 0.0

    while check:
        choice = input("Choose an arithmetic operation (add, min, multiply, divide): ")
    
        if choice == "add":
            result = add(x, y)
            check = False
        elif choice == "min":
            result = min(x, y)
            check = False
        elif choice == "multiply":
            result = multiply(x, y)
            check = False
        elif choice == "divide":
            result = divide(x, y)
            check = False
        else:
            print("Please enter a valid arithmetic operation!")

    print("The result is", result)
    return 0

if __name__ == "__main__":
    main()