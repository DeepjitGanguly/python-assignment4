#Cont the nmber of vowel in a tring ing a for loop.

# Define the input string
input_string = "Hello, World!"

# Initialize a variable to store the count of vowels
vowel_count = 0

# Define a set of vowels
vowels = {'a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U'}

# Iterate over each character in the input string using a for loop
for char in input_string:
    # Check if the character is a vowel
    if char in vowels:
        # If it's a vowel, increment the vowel count
        vowel_count += 1

# Print the count of vowels
print("Number of vowels in the string:", vowel_count)

