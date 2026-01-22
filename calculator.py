

N = int(input("How many numbers you want to append to your list: "))

numebrs = []
for i in range(N):
    user = int(input("Enter list of numbers you want to perform maths operations to:"))
    numebrs.append(user)

print("##_Maths Operations_##")
math_operations = ["Add", "Subtract", "Multiply", "Divide"]
            
for i, operation in enumerate(math_operations, start=1):
    print(f"{i}.{operation}")


option = int(input("Enter a number of maths operation you want to perform:"))
def add():

    if option == 1:
        total = 0 # start counting from zero
        for num in numebrs:
            total += num
        print(total)
add()

def subtract():
    if option == 2:
        total = numebrs[0] # start subtracting from the starting number in the list which is in index zero(first number minus the following numbers)
        for num in numebrs[1:]: 
            total -= num
        print(total)
subtract()

def multiply():
    if option == 3:
        total = 1 # start multiply at 1 because any number multiplied by zero is zero
        for num in numebrs:
            total *= num
        print(total)
multiply()

def divide():
    if option == 4:
        total = numebrs[0] # first number divided by the following numbers
        for num in range(1, len(numebrs)):
            divider = numebrs[num]
            if divider == 0:
                return "You can't divide by zero"
            total //= divider
        print(total)
divide()

