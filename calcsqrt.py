#! /usr/bin/env python3

# Cathal Donohoe
# Calculate the square root of a number.

def sqrt(x):
    # Initial guess for square root
    if x<0:
        print("Error: negative value")
        retunr -1
    else:
        print("Here we go")

    z = x/2.0
    
    #Continuously improve guess

    while abs(x -(z*z)) > 0.00000001:
        z = z - (((z*z) - x) / (2*z))
     
    return z

myval = 63.0
print("The square root of", myval, "is", sqrt(myval))


