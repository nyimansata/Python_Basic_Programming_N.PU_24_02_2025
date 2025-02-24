# # Assignment 1: Complex Conditions with Logical Operators
a = int(input("Enter the first integer (a): "))
b = int(input("Enter the second integer (b): "))
c = int(input("Enter the third integer (c): "))

firstCondition = (a > b or b > c),
secondCondition = (a % 2 == 0 and c % 2 != 0),
thirdCondition = (b != c)

if firstCondition and secondCondition and thirdCondition:
    print("Conditions met")
else:
    print("Conditions not met")


# Assignment 2: Type Checking with Logical Operations
def check_input_types(input1, input2, input3):
    if isinstance(input1, str) and isinstance(input2, int) and isinstance(input3, float):
        return "Valid input types"
    else:
        return "Invalid input types"


print(check_input_types("Hello", 10, 3.14))  # Valid

# Assignment 3: Logical Operators with Boolean Values and Type Casting
x = input("Enter the first value (x): ")
y = input("Enter the second value (y): ")

x_bool = bool(x)
y_bool = bool(y)

print(f"x AND y: {x_bool and y_bool}")
print(f"x OR y: {x_bool or y_bool}")
print(f"NOT x: {not x_bool}")
print(f"x XOR y: {(x_bool or y_bool) and not (x_bool and y_bool)}")