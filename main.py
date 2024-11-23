def add(p, Q):
    return p+Q

def subtract(p, Q):
    return p-Q

def multiply(p, Q):
    return p* Q

def divide(p, Q):
    return p/ Q
# Now we will take inputs from the user
print("please select operation.")
print("a. Add")
print("b. Subtract")
print("c. multiply")
print("d. Divide")

choice = input("please enter choice (a/b/c/d):")

num_1 = int(input("please enter the first number:"))
num_2 = int(input("please enter the second number: "))

if choice == 'a':
    print(num_1, "+", num_2, "=", add(num_1, num_2))
elif choice == 'b':
    print(num_1, "-", num_2, "=", subtract(num_1, num_2))
elif choice == 'c':
    print(num_1, "*",  num_2, "=", multiply(num_1, num_2))
elif choice == 'd':
    print(num_1, "/",   num_2,  "=",  divide(num_1, num_2))
else:
     print("This is an invalid input")