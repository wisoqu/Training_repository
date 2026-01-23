def repeat(input_func):
    def go():
        input_func()
        input_func()
        input_func()
    return go()

@repeat
def hi():
    print('hello')