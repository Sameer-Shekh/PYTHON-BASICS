# username = "sameer in global scope"

# def func():
#     # username = "chai in local scope"
#     print(username)

# print(username)
# func()


x = 99
# def func2(y):
#     z = x + y 
#     return z

# result  = func2(1)
# print(result)


# def func3():
#     global x
#     x = 12
#     # x = 88

# func3()
# print(x) # 99



def f1():
    # x = 88 
    def f2():
        print(x) # 88 not 99 if declared in f1 other wise it will take global x
    return f2

my_res = f1()
my_res()



def chai(num):
    def actual(x):
        return x ** num
    return actual

f = chai(2)
g = chai(3)

print(f(3))
print(g(3))