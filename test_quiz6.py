

def Add(numbers):
    numbers = map(int, numbers.split(","))
    return (sum(numbers))

def test_input():
    assert Add("1,2,3") == 5

