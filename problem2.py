#! python3

# Have the user enter a number 
# Determine if the number is an integer
# 1 mark

# Inputs:
# a number

# Outputs:
# "the number is an integer"
# "the number is not an integer"
import math

x = float(input("Enter a number = "))
if x % 1 == 0:
    print("The number is a integer")
else:
    print("The number is not an integer")