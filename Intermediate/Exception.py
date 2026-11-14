#Exception Handeling

x = -5
if x<0:
    raise Exception("x should be positive")

assert (x >= 0), "x is not positive"     #assertioin error if false


try:
    a = 5/0

except ZeroDivisionError as e:
    print(e)
except TypeError as e:
    print(e)
except Exception as e:
    print("an error happened")
    print(e)
else:
    print("Every thing is fine")
finally:
    print("Cleaning up ...")


#defining exceptions
class ValueTooHighError(Exception):
    pass

class ValueTooSmallError(Exception):
    def __init__(self, message, value):
        self.message = message
        self.value = value

def testvalue(x):
    if x > 100:
        raise ValueTooHighError("value is too high")
    if x < 5:
        raise ValueTooSmallError("Value is too small", x)
try:
    testvalue(200)
except ValueTooHighError as e:
    print(e)
except ValueTooSmallError as e:
    print(e.message, e.value)
