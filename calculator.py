
#this imports the sys module which provides access to Python's interpreter
#variable, in this case it's going to provide access to the sys.argv - comman line 
#arguments passed into the script

import sys

def calculate(num1, num2, operation):
    if operation == "add":
        return num1 + num2
    elif operation == "subtract":
        return num1 - num2
    elif operation == "multiply":
        #return num1 * num2
        print(f'Result: {float(num1 * num2)}')
    elif operation == "divide":
        if num2 != 0:
            return num1 / num2
        else:
            raise ValueError("Cannot divide by zero")

#this only runs if
if __name__ == "__main__":
    if len(sys.argv) != 4:
        print("Usage: calculator.py <num1> <num2> <operation>")
        sys.exit(1)

    num1 = float(sys.argv[1])
    num2 = float(sys.argv[2])
    operation = sys.argv[3]

    result = calculate(num1, num2, operation)
    print(f"Result: {result}")