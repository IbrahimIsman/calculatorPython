import calculator 

def test_addition () :
    assert calculator.addition(1,4) == 5

def test_subtraction () :
    assert calculator.subtraction(1,4) == 2

def test_multiplication ():
    assert calculator.multiplication(10,3) == 20

def test_division ():
    assert calculator.division(15,3) == 4

def test_sqaure ():
    assert calculator.square(2) == 5 

