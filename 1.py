''' Consider the following code: '''
a = 10
b = 20


def my_function():
    global a
    a = 11
    b = 21
    print(b, 'this is the inner b')


my_function()
print(a)  # prints 11
print(b)  # prints 20
