# prompts user to enter a string
b = input("Enter a string: ")

upper = ""
lower = ""

# method to seperate lower & uppercase letters
for one in b:
    if one.isupper():
        upper += one
    elif one.islower():
        lower += one

# method combines the lower & uppercase back to one string
result = lower + upper

# use the print method to print the result
print(result)