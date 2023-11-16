def fn():
    n=int(input("enter any number"))
    return lambda a:a*n
s1=fn()
print(s1(4))
