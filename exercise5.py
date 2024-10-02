# Get input string from the user
input_string = input("Enter a string: ")

# Remove spaces and convert to lowercase for accurate comparison
cleaned_string = input_string.replace(" ", "").lower()

# Check if the string is the same forward and backward
if cleaned_string == cleaned_string[::-1]:
    print(input_string, "is a palindrome.")
else:
    print(input_string, "is not a palindrome.")