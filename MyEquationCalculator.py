"""
MyEquationCalculator.py
Calculating simple equations inputed by the user. 

Andy Zeng; 301221527
Eric Sund; 301284359
Sept 30, 2015
"""

# Be polite and ask for their name.
gettingName = True
while gettingName:
    name = input("We would like to ensure quality customer service through addressing you by name.  What is your name?: ")
    if len(name) < 1:
        print("Seriously though, please enter your name! \n")
    else:
        print("\n" + name + "? What a fantastic name.  I should name every one of my children that.  Wow.\n\n")
        gettingName = False
        
# Get a valid input from your user
retry = 0
while retry == 0:
    #Go for the introductions! 
    userinput = input("""Welcome to the Equation Calculator, %s!
Accepted format is <operand><space><operator><space><operand>
Note that there must be a single space between the operator and each operand.
Please type in an equation to solve: """ %(name))
    # Preserve userinput and manipulate variable equation
    equation = userinput
    # Ensure that they are using a valid operator in their input 
    if (equation.count("+") + equation.count("-") + equation.count("*") + equation.count("/") < 1):
        print("\nYou just entered " + userinput +  ".  Please include an operator. It must be either + (addition), - (subtraction), * (multiplication), or / (float division).  Remember that the equation format must be <operand><space><operator><space><operand> \n")
    # Ensure that they are using only one operator. 
    elif (equation.count("+") + equation.count("-") + equation.count("*") + equation.count("/") > 1):
        print("\nYou just entered " + userinput + ".  That's too complex for me! Please use only one operator. \n")
    #Check to ensure there is a space between the operator and the operands.
    elif (equation.count(" + ") + equation.count(" - ") + equation.count(" * ") + equation.count(" / ") < 1):
        print("\nYou just entered " + userinput + """.  Please make sure that you include a space between the operands and the operator.
Remember that the equation format must be <operand><space><operator><space><operand>
Note that there must be a single space between the operator and each operand.\n""")
    elif (equation.count(" ") > 2):
        print("\nYou just entered " + userinput + """.  You've got way too many spaces.
Remember that the equation format must be <operand><space><operator><space><operand>
Note that there must be a single space between the operator and each operand.\n""")
    # Good to go! 
    else:
        # Replace all spaces from the string
        equation = equation.replace(" ","")
        #Find the position of the operator; correct for string.find() returning -1 when unsuccessful 
        operatorpos = equation.find("+") + equation.find("-") + equation.find("*") + equation.find("/") + 3
        #Slice the string to get operand1
        operand1 = equation[:operatorpos] #slice is non-inclusive
        #Slice the string to get the operator
        operator = equation[operatorpos]
        #Slice the string to get operand2
        operatorright = operatorpos + 1
        operand2 = equation[operatorright:]
	#Ensure that operands are not empty
        if len(operand1) < 1 or len(operand2) < 1:
            print("\nYou just entered " + userinput + ".  Please make sure that you have entered in both operands! \n")
        else:
            #Ensure that operands are actually numbers
            #We use try because we are including floats. string.isdigit() will only return True for integers)
            try:
                operand1 = float(operand1)
                operand2 = float(operand2)
                retry = 1
            except ValueError:
                print("\nYou just entered " + userinput + ".  Please make sure you are actually entering numbers as your operands! \n")

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
    exit()

#Return the result and wish them a beautiful day
print("""
Alright %s,
I've worked very hard and solved your equation!
Here's my answer:
%s  =  %s
Have a beautiful day, you wonderful individual.""" %(name, userinput, result))




#In the case of operand operator:
#Please add an operand to your operator. 
