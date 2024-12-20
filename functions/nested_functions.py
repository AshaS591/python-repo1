def outer():
    def inner():
        print('This is inner function...')
    return inner
var=outer()
var()