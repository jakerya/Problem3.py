# Initialize variables to store inputs, sum, and average
numbers = []
sum_of_numbers = 0

# Collecting five inputs from the user
for i in range(5):
    num = float(input(f"Enter number {i + 1}: "))
    numbers.append(num)
    sum_of_numbers += num

# Calculating the average
average = sum_of_numbers / 5

# Printing the sum and average
print(f"The sum of the numbers is: {sum_of_numbers}")
print(f"The average of the numbers is: {average}")
