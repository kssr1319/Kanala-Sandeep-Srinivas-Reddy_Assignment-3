# Write a Python program to reverse a string.

# Sample String : "1234abcd"
# Expected Output : "dcba4321"

def rev(s):
    str1 = ""
    for r in s:
        str1 = r + str1
    return str1
s = input("Enter any word:")
print("The given string is: ", s)
print("The reverse string is: ", rev(s))