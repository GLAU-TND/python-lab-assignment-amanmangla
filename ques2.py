class MyException(Exception):
    def __init__(self, v):
        self.v = v


def exceptionhandling():
    a = 10
    try:
        a += 'abc'
    except TypeError as e:
        print(type(e).__name__, e)
    try:
        a.abcd()
    except AttributeError as e:
        print(type(e).__name__, e)
    try:
        int('sd')
    except ValueError as e:
        print(type(e).__name__, e)


exceptionhandling()