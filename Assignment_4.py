# #Create an application to determine whether a year is a leap year or not.
year = int(input('Enter your year: '))
def leap_year(year):
    if(year % 4  == 0 and year % 100 != 0) or (year % 400 == 0):
        return  True
    else:
        return False

if leap_year(year):
    print(f"{year} your year is leap")
else:
    print(f"{year} your year is not leap")



# #Create an application to determine the output: negative, positive, or zero.
def check_number(num):
    if num > 0:
        return "Positive"
    elif num < 0:
        return "Negative"
    else:
        return "Zero"

my_Number = float(input("Enter your number: "))
result = check_number(my_Number)

print(f"This is your number: {result}")




#Create an application to calculate the total amount to be paid based on the year-end discount:
#     If the total purchase is more than 100,000, you get a 10% discount.
#     If the total purchase is more than 50,000, you get a 5% discount.
#     If the total purchase is less than 50,000, there is no discount.
def calculate_discount(total_purchase):
    if total_purchase > 100000:
        discount = 0.10
    elif total_purchase > 50000:
        discount = 0.05
    else:
        discount = 0.00

    final_amount = total_purchase - (total_purchase * discount)
    return final_amount
total_purchase = float(input("Enter the total purchase amount: "))
print(f"Total amount after discount: {calculate_discount(total_purchase)}")




# Give the scores for three subjects: Math, Science, and English. You will pass if you meet the following criteria:
#     The average score is more than 75.
#     Only one subject is below 70.
#     You get a perfect score in any subject.
def check_pass_status(math, science, english):
    average_score = (math + science + english) / 3
    below_70 = sum(score < 70 for score in [math, science, english])
    perfect_score = any(score == 100 for score in [math, science, english])

    if average_score > 75 or (below_70 == 1 and average_score >= 70) or perfect_score:
        return "Pass"
    else:
        return "Fail"

math = float(input("Enter Math score: "))
science = float(input("Enter Science score: "))
english = float(input("Enter English score: "))

result = check_pass_status(math, science, english)
print(f"Pass Status: {result}")
