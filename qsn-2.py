#Calclate the m of nmber from 1 to 10 ing a while loop.

# Initialize variables
total = 0
number = 1

# Use a while loop to iterate from 1 to 10
while number <= 10:
    total = number + total # Add the current number to the total
    number = number + 1 # Increment the number for the next iteration

# Print the sum
print("The sum of numbers from 1 to 10 is:", total)
