import calculator

def test_add():
    assert calculator.calculate(2, 3, "add") == 5.0

# Add more functional tests for subtract, multiply, and divide

def test_terminal_output(capsys):
    calculator.calculate(10, 2, "multiply")
    captured = capsys.readouterr()

    ##tests for printed output and will fail with a return statement and no print 
    assert captured.out == 'Result: 20.0\n'


#### Monkey Patch ####

#this function takes monkey patch parameter - which allows you to modify or "monkey patch" functions at runtime for testing
#can simulate user input

def test_argument_passing(monkeypatch):

    ##monkey patch setter method is used to modify something at runtime
    
    #Here it modifies sys.argv - this is a list in Python that capture command line argument input (user input)
   
    #it is placing the second argument into the command line when this runs
    #so basically it's simulating a user typing 'python calculator.py 6 2 divide'
    #this isnt going to work because we aren't collected input here, we're doing it in main
    monkeypatch.setattr("sys.argv", ["calculator.py", "6", "2", "divide"])

    #Here we tell the test program wh
    assert calculator.calculate(6, 2, "divide") == 3.0

# Add more tests to cover edge cases and negative scenarios

