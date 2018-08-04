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

    while check:
        choice = input("Choose an arithmetic operation (add, min, multiply, divide): ")
        if choice == "add" or choice == "min" or choice == "multiply" or choice == "divide":
           break
        else:
            print("Please enter a valid arithmetic operation!")

    if choice == "add":
        res = add(x, y)
    elif choice == "min":
        res = min(x, y)
    elif choice == "multiply":
        res = multiply(x, y)
    elif choice == "divide":
        res = divide(x, y)
    else:
        print("You didn't type anything in!")
        return 0

    print("The result is", res)
    return 0

if __name__ == "__main__":
    main()