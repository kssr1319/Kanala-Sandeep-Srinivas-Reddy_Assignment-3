# Write a Python function that accepts a string and calculate the number of upper case letters and lower case letters.

# Sample String : 'The quick Brow Fox'
# Expected Output :
# No. of Upper case characters : 3
# No. of Lower case Characters : 12

def lcnt(string):
    count1=0
    for i in string:
        if(i.islower()):
            count1=count1+1
    return count1
def ucnt(string):
    count2=0
    for i in string:
        if(i.isupper()):
            count2=count2+1
    return count2
string=input("Enter string:")   
print("The number of lowercase characters is:", lcnt(string))
print("The number of uppercase characters is:", ucnt(string))