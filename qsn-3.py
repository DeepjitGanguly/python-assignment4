#Calclate the factorial of a nmber ing a for loop.

# Define the number for which we want to calculate the factorial
number = 5

# Initialize the factorial value to 1
factorial_value = 1

# Iterate from 1 to the given number (inclusive) using a for loop
for i in range(1, number + 1):
    # Multiply the current factorial value by the current number (i)
    factorial_value *= i

# Print the factorial value
print("Factorial of", number, "is:", factorial_value)
