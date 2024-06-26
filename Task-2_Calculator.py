def add(x, y):        #add function
    return x + y

def sub(x, y):   #subtraction function
    return x - y

def mul(x, y):   #multiplication function
    return x * y

def div(x, y):     #division function
    return x / y

print("Select the operation.")   #choices
print("1.Add")
print("2.Subtract")
print("3.Multiply")
print("4.Divide")

while True:
    choices = input("Enter your choice(1/2/3/4): ")
    if choices in ('1', '2', '3', '4'):
        try:            #exception
            n1 = float(input("Enter the first number: "))
            n2 = float(input("Enter the second number: "))
        except ValueError:
            print("Invalid input. Please enter a valid number.")
            continue
        if choices == '1':
            print(n1, "+", n2, "=", add(n1, n2))
        elif choices == '2':
            print(n1, "-", n2, "=", sub(n1, n2))
        elif choices == '3':
            print(n1, "*", n2, "=", mul(n1, n2))
        elif choices == '4':
            print(n1, "/", n2, "=", div(n1, n2))
        
        next_cal = input("Let's do next calculation? (yes/no): ")
        if next_cal == "no":
          break
    else:
        print("Invalid Input!!")