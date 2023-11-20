def factorial(x):
    if x < 0:
        return("Error")
    elif x == 1 or x == 0:
        return 1
    else:
        return x*factorial(x-1)

x = int(input("Input an x and I will calculate x factorial. "))

print(factorial(x))
