def addition(add1, add2):
    add3 = add1 + add2
    return add3
def subtraction(sub1, sub2):
    sub3 = sub1 - sub2
    return sub3
def multiplication(mul1, mul2):
    mul3 = mul1 * mul2
    return mul3
def division(div1, div2):
    div3 = div1 / div2
    return div3
def modulus(mod1, mod2):
    mod3 = mod1 % mod2
    return mod3
def power(pow1, pow2):
    pow3 = pow1 ** pow2
    return pow3
def increment(a):
    return a + 1
def decrement(a):
    return a - 1
def op(fun, a):
    val = fun(a)
    return val
def nain():
    def inner(a, b):
        return a + b
    return inner
def dain():
    def inner(a, b):
        return a / b
    return inner
def sain():
    def inner(a, b):
        return a - b
    return inner
def aain():
    def inner(a, b):
        return a * b
    return inner