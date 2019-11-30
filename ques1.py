class MyException(Exception):
    def __init__(self,v):
        self.v=v
def xyz():
    a=int(input())
    b=int(input())
    sum=a+b
    if sum<150:
        raise MyException('Custom Exception Occurred')
xyz()