"""
EquationCalculator.py
Calculating simple equations inputed by the user.
Andy Zeng; 301221527
Eric Sund; 301284359
September 30 2015
"""

import re

# Be polite and ask for their name.
gettingName = True
while gettingName:
    name = input("We would like to ensure quality customer service through addressing you by name.  What is your name?: ")
    if len(name) < 1:
        print("\nSeriously though, please enter your name! \n")
    else:
        print("\n" + name + "? What a fantastic name.  I should name every one of my children that.  Wow.\n")
        gettingName = False

# Get a valid input from your user
retry = 0
while retry == 0:
    #Go for the introductions!
    equation = input("""Welcome to the Equation Calculator, %s!
Accepted format is <operand><space><operator><space><operand>
Note that there must be a single space between the operator and each operand.
Also note, you must put a tildle in front of any number you want to be negative.
Please type in an equation to solve: """ %(name))

    equation = equation.strip()
    space = equation.find(" ")

    #if there is 1 operand
    try:
        equation = float(equation)
        print("\nYou have entered " + str(equation) + ".  Please include two operands and an operator.\n")

    #2 operands and no operator, or 1 operator and 1 operand
    except ValueError:
        #check for nothing entered
        if equation == "":
            print("\nYou entered nothing.  Please enter something.\n")
        #if there are letters
        elif len(re.findall("[A-Z]", equation)) >= 1 or len(re.findall("[a-z]", equation)) >= 1:
            print("\nYou entered " + equation + ".  I see some letters in there.  You probably entered a word.  Please don't do that, it's invalid.\n")
        #if there is 1 operator
        elif (len(equation) == 1) and ("-" in equation or "+" in equation or "*" in equation or "/" in equation):
            print("\nYou entered " + equation + ".  Please enter two operands.\n")
        #if there is 1 operator and 1 operand
        elif equation[space+1::] == "+" or equation[space+1::] == "-" or equation[space+1::] == "*" or equation[space+1::] == "/":
            print("\nYou entered " + equation + ".  Please enter one more operand.\n")

        #if there are 2 operands and no operator
        elif equation[space+1].isdigit(): #if there's no negative in front of the second operand
            try:
                float(equation[space+1::])
                print("\nYou entered " + equation + ".  Please enter an operator in between the operands.\n")
            except ValueError:
                print("")
        elif equation[space+1] == "-" and equation[space+2].isdigit(): #if there is a negative in front of the second operand
            try:
                float(equation[space+2::])
                print("\nYou entered " + equation + ".  Please enter an operator in between the operands.\n")
            except ValueError:
                print("")

        #good to go!
        else:
            operand1 = float(equation[:space])
            operand2 = float(equation[space+3:])
            operator = equation[space+1]
            #Evaluate the equation!
            #Since there is no easy way to convert strings into operators, we will use 4 conditional equations
            if operator == "+":
                result = operand1 + operand2
            elif operator == "-":
                result = operand1 - operand2
            elif operator == "*":
                result = operand1 * operand2
            elif operator == "/":
                result = operand1 / operand2
            else:
                print("If you are seeing this message, we've got a pretty big issue and we'll need to debug some more")

            #Return the result and wish them a beautiful day
            print("""
Alright %s,
I've worked very hard and solved your equation!
Here's my answer:
%s  =  %s
\nHave a beautiful day, you wonderful individual.\n""" %(name, equation, result))
