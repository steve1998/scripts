# Simple calculator script in shell
# May be extended to support other features as well as other libraries

def add(addend1:float , addend2: float) -> float:
    """
        Summation between two addends.
    """
    return addend1 + addend2

def min(subtrahend: float, minuend: float) -> float:
    """
        Subtracts minued from subtrahend.
    """
    return subtrahend - minuend

# Multiply two numbers.
def multiply(multiplicand: float, multiplier:float) -> float:
    """
        Performs multiplication on the multiplicand and multiplier.
    """
    return multiplicand * multiplier

def divide(numerator: float, denominator:float) -> float:
    """
        Divides the numerator to the denominator.
    """
    return numerator / denominator

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

    print(f"The result is {result:.3f}")
    return 0

if __name__ == "__main__":
    main()