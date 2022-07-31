# Write a Python function to sum all the numbers in a list.

# Sample List : (8, 2, 3, 0, 7)
# Expected Output : 20
                        
lst1 = []
r = int(input("Enter range:"))
for r in range(0, r):
    a = int(input())
    lst1.append(a)

def sum(lst, size):
    if size == 0:
        return 0
    else:
        return lst[size - 1] + sum(lst, size - 1)
total = sum(lst1, len(lst1))
print("Sum of all numbers in list are: ", total)