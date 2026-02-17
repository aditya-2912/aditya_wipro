def div(a,b):
    if b == 0:
        raise ZeroDivisionError
    else:
        return a/b

assert div(2,0) == 2