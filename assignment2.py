"""
assignment2.py

Allows a user to calculate solutions to equations.

Eric Sund
Septmber 29, 2015
"""

print("Welcome to Equation Calculator!")
equation = input("Please enter an equation: ")
first = equation[0]
operator = equation[2]
second = equation[4]

if operator == '+':
	print(int(first) + (second))
