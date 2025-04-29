def f1():
    x = 18
    def f2():
        print(x)
    return f2

myResult = f1()
myResult()

def chaicoder(num):
    def actual(x):
        return x ** num
    return actual

f = chaicoder(2)
g = chaicoder(3)

print(f(7))
print(g(7))