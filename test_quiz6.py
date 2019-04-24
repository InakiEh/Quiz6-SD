

def Add(numbers):
    numberslist = map(int, numbers.split(","))
    return numbers

def test_input():
    assert Add("1,2,3") == "1,2,3"






