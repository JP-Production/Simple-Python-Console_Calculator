# imports
import time

# Shows a little string when the script is executed
print("Welcome to my simple, python, console calculator. \nTo start just write: Calculator-Start or C-S for short | \nWrite /VOperators or /VO to get a list of valid Math Operations.\n")

# Some variable's
command = str(input('Hello, User. What is your desired command >> '))

# Gives you commands that can be written in the command prompt, power shell etc.
def choose_command():
    # Start the calculator
    if command == 'Calculator-Start' or command == 'C-S':
        number_one = float(input('Enter first number: '))
        operator = str(input('Enter Operation: '))
        number_two = float(input('Enter second number: '))
        calculate(number_one, operator, number_two)  
    # Show a list of valid operations         
    elif command == '/VOperators' or command == '/VO':
        print('Valid Operators:\n {\n +, \n *, \n -, \n / \n }')
    elif command == '/LOL':
        lol(1)

# Little secret if you dont look here ;)
def lol(amount):
    for n in range(amount):
        time.sleep(.5)
        print('lol')
        time.sleep(.5)
        print('this')
        time.sleep(.5)
        print('is')
        time.sleep(.5)
        print('a secret')
        time.sleep(1)
        print(':>')
        time.sleep(1)
        print("Okay not really if you looked at the code lol")


# Calculates math operations
def calculate(num1, op, num2):
    if op == '+':
        print('Result = ', num1+num2, end='')
    elif op == '-':
        print('Result = ', num1-num2, end='')
    elif op == '*':
        print('Result = ', num1*num2, end='')
    elif op == '/':
        print('Result = ', num1/num2, end='')
    else:
        print('Error: 101 Choosen operator is invalid. For a List of Operators type /VOperators')

# Calls the Choose Command function to execute commands like 'Calculator-Start'.
choose_command()
