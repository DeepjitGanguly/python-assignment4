#Print a pattern ing neted loop.

# Define the number of rows in the triangle
num_rows = 5

# Outer loop for the rows
for i in range(num_rows):
    # Inner loop for printing stars in each row
    for j in range(i + 1):
        print("*", end=" ")
    # Move to the next line after printing stars for the current row
    print()
