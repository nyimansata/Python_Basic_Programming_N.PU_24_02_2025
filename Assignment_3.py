# 1. Create an application to calculate the area of a square.
def calculate_square_area():
    side = float(input("Enter the length of a side of the square: "))
    area = side * side
    print(f"The area of the square is: {area} square units")

calculate_square_area()



# 2. Create an application to calculate the change based on the total purchase and the amount paid.
def calculate_change():
    total_purchase = float(input("Enter the total purchase amount: "))
    amount_paid = float(input("Enter the amount paid: "))

    if amount_paid < total_purchase:
        print("Insufficient amount paid. Please enter a valid amount.")
    else:
        change = amount_paid - total_purchase
        print(f"Your change is: {change:.2f} currency units")

calculate_change()



# 3. Create a program that asks the user to enter two numbers, then calculates and displays the results of addition, subtraction, multiplication, and division.
def calculator():
    num1 = float(input("Enter the first number: "))
    num2 = float(input("Enter the second number: "))

    addition = num1 + num2,
    subtraction = num1 - num2
    multiplication = num1 * num2
    division = num1 / num2


    print(f"\nResults:")
    print(f"Addition: {addition}")
    print(f"Subtraction: {subtraction}")
    print(f"Multiplication: {multiplication}")
    print(f"Division: {division}")


calculator()



# 4. Create an application to calculate the total payment after a 20% discount.
def calculate_discount():
    total_price = float(input("Enter the total price: "))

    discount = total_price * 0.20
    final_price = total_price - discount

    print(f"\nOriginal Price: {total_price:.2f} currency units")
    print(f"Discount (20%): {discount:.2f} currency units")
    print(f"Total Payment After Discount: {final_price:.2f} currency units")


calculate_discount()



# 5. Create an application to calculate the profit earned based on sheep sales, where the base price is 2,500,000 and the selling price is 3,000,000. Calculate the total capital spent and the profit obtained for the number of sheep entered.
def calculate_profit():
    base_price = 2500000
    selling_price = 3000000

    num_sheep = int(input("Enter the number of sheep sold: "))

    total_capital = num_sheep * base_price
    total_revenue = num_sheep * selling_price
    total_profit = total_revenue - total_capital

    print(f"\nTotal Capital Spent: {total_capital:,} currency units")
    print(f"Total Revenue: {total_revenue:,} currency units")
    print(f"Total Profit Earned: {total_profit:,} currency units")


calculate_profit()


# # 6 Create a program that swaps the values of two variables without using an additional variable (use x and y).
def swap_values():
    x = int(input("Enter value for x: "))
    y = int(input("Enter value for y: "))

    print(f"\nBefore swapping: x = {x}, y = {y}")

    x, y = y, x

    print(f"After swapping: x = {x}, y = {y}")

swap_values()



# 7. Calculate the average of three numbers.
def calculate_average():
    num1 = float(input("Enter the first number: "))
    num2 = float(input("Enter the second number: "))
    num3 = float(input("Enter the third number: "))

    average = (num1 + num2 + num3) / 3

    print(f"\nThe average of the three numbers is: {average:.2f}")

calculate_average()



# 8 Calculate the area and perimeter of a right-angled triangle.
import math

def calculate_triangle():
    base = float(input("Enter the base of the triangle: "))
    height = float(input("Enter the height of the triangle: "))

    hypotenuse = math.sqrt(base**2 + height**2)

    area = (base * height) / 2

    perimeter = base + height + hypotenuse

    print(f"\nArea of the triangle: {area:.2f} square units")
    print(f"Perimeter of the triangle: {perimeter:.2f} units")

calculate_triangle()
