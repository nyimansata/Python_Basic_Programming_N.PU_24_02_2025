# 1. Sum the Elements in a List or Array:
# a. Create a list containing 10 numbers (can be filled manually or via user input)
# b. Sum all the elements in the list
# c. Display the list and the total sum of its elements

sumArray = [2,3,4,5,6,7,8,9,1,20]

def list_of_arrays():
    total = sum(sumArray)
    return total

print("List:", sumArray)
print("Total sum:", list_of_arrays())

# 2. Add a New Value to a List:
# a. Create a list containing 5 fruit names
# b. Display all the contents of the list
# c. Display the fruit at index 2
# d. Add one new fruit name to the list
# e. Display the list after the addition
fruitList = ["apple", "banana", "cherry", "date", "elderberry"]
def fruit_list():
    print("List of fruits:", fruitList)
    print("Fruit at index 2:", fruitList[2])
    fruitList.append("orange")
    return fruitList
print("List after addition:", fruit_list())


# 3. Write a Python program that accepts numbers from the user (separated by spaces), then:
# a. Store the numbers in a list
# b. Calculate the total sum of all numbers in the list
# c. Display the average value of the list
# d. Find and display the largest and smallest values in the list
def user_input():
    user_input = input("Enter numbers separated by spaces: ")
    num_list = list(map(int, user_input.split()))
    total_sum = sum(num_list)
    average = total_sum / len(num_list)
    largest = max(num_list)
    smallest = min(num_list)
    return total_sum, average, largest, smallest
total_sum, average, largest, smallest = user_input()
print("Total sum:", total_sum)
print("Average:", average)
print("Largest value:", largest)
print("Smallest value:", smallest)

# 4. Write a Python program to calculate statistics from a list of numbers:
# a. Ask the user to input several numbers (minimum 5 numbers)
# b. Calculate and display the minimum, maximum, average, and median values
# c. Display the list sorted from smallest to largest
def statistics():
    user_input = input("Enter at least 5 numbers separated by spaces: ")
    num_list = list(map(int, user_input.split()))
    if len(num_list) < 5:
        print("Please enter at least 5 numbers.")
        return
    minimum = min(num_list)
    maximum = max(num_list)
    average = sum(num_list) / len(num_list)
    sorted_list = sorted(num_list)
    median = sorted_list[len(sorted_list) // 2] if len(sorted_list) % 2 != 0 else (sorted_list[len(sorted_list) // 2 - 1] + sorted_list[len(sorted_list) // 2]) / 2
    return minimum, maximum, average, median, sorted_list
minimum, maximum, average, median, sorted_list = statistics()
print("Minimum:", minimum)
print("Maximum:", maximum)
print("Average:", average)
print("Median:", median)
print("Sorted list:", sorted_list)


# 5. Write a Python program for a "Shopping List" that:
# a. Creates an empty list as the shopping list
# b. Asks the user to input 5 shopping items
# c. Displays the entire shopping list
# d. Asks the user to remove 1 item that has been purchased
# e. Displays the updated shopping list
def shopping_list():
    shopping_list = []
    for i in range(5):
        item = input("Enter shopping item {}: ".format(i + 1))
        shopping_list.append(item)
    print("Shopping list:", shopping_list)
    purchased_item = input("Enter the item you have purchased: ")
    if purchased_item in shopping_list:
        shopping_list.remove(purchased_item)
    else:
        print("Item not found in the list.")
    return shopping_list
print("Updated shopping list:", shopping_list())
