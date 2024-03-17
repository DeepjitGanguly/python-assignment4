#Generate a mltiplication table ing neted loop.

# Define the range for the multiplication table (e.g., from 1 to 10)
start = 1
end = 10

# Outer loop for the multiplicand (left column)
for i in range(start, end + 1):
    # Inner loop for the multiplier (top row)
    for j in range(start, end + 1):
        # Calculate the product of the current multiplicand and multiplier
        product = i * j
        # Print the product with proper formatting
        # Use end="\t" to add a tab after each product for better alignment
        print(f"{i} x {j} = {product}", end="\t")
    # Move to the next line after printing all products for the current multiplicand
    print()
