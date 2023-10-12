
# Function for Addition
def add(x, y):
    return x + y

# Function for Subtraction
def subtract(x, y):
    return x - y

# Function for Multiplication
def multiply(x, y):
    return x * y

# Function for Division
def divide(x, y):
    return x / y


print("Select operation.")
print("1.Add")
print("2.Subtract")
print("3.Multiply")
print("4.Divide")

while True:
    # User options
    options = input("Enter an option to Calculate (1/2/3/4): ")

    # check if choice is one of the four options
    if options in ('1', '2', '3', '4'):
        
        num1 = int(input("Enter first number: "))
        num2 = int(input("Enter second number: "))

        if options == '1':
            print(num1, "+", num2, "=", add(num1, num2))

        elif options == '2':
            print(num1, "-", num2, "=", subtract(num1, num2))

        elif options == '3':
            print(num1, "X", num2, "=", multiply(num1, num2))

        elif options == '4':
            print(num1, "/", num2, "=", divide(num1, num2))
        
      
    else:
        print("Choose an option to Calculate")