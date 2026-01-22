def add(numbers):
    """Add all numbers together and return the sum."""
    total = 0
    for num in numbers:
        total += num
    return total


def subtract(numbers):
    """Subtract all following numbers from the first number and return the result."""
    if len(numbers) == 0:
        return 0
    total = numbers[0]
    for num in numbers[1:]:
        total -= num
    return total


def multiply(numbers):
    """Multiply all numbers together and return the product."""
    total = 1
    for num in numbers:
        total *= num
    return total


def divide(numbers):
    """Divide the first number by all following numbers and return the result."""
    if len(numbers) == 0:
        return 0
    
    total = numbers[0]
    for num in numbers[1:]:
        if num == 0:
            print("Error: You can't divide by zero")
            return None
        total /= num
    return total


def main():
    """Main function to run the calculator program."""
    N = int(input("How many numbers you want to append to your list: "))

    numbers = []
    for i in range(N):
        user = int(input("Enter list of numbers you want to perform maths operations to:"))
        numbers.append(user)

    print("##_Maths Operations_##")
    math_operations = ["Add", "Subtract", "Multiply", "Divide"]
                
    for i, operation in enumerate(math_operations, start=1):
        print(f"{i}.{operation}")

    option = int(input("Enter a number of maths operation you want to perform:"))
    
    # Call the appropriate function based on user choice
    if option == 1:
        result = add(numbers)
        print(f"Result: {result}")
    elif option == 2:
        result = subtract(numbers)
        print(f"Result: {result}")
    elif option == 3:
        result = multiply(numbers)
        print(f"Result: {result}")
    elif option == 4:
        result = divide(numbers)
        if result is not None:
            print(f"Result: {result}")
    else:
        print("Invalid option! Please choose a number between 1 and 4.")


if __name__ == "__main__":
    main()

