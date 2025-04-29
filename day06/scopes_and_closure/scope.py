username = "chaiaurcode"

def func():
    # username = "chai"
    print(username)

print(username)
func()


x = 99
def func2(y):
    z = x + y
    return z

print(func2(1))


def func3():
    global x 
    x = 88

func3()
print(x)