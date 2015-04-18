def A(func):
    print "decorator"
    return func


def B(func):
    def __B():
        print "de2"
        func()
        print "de2"
    return __B


def C(func):
    def __C(*args, **kwargs):
        print "de3"
        func(*args, **kwargs)
        print "de3"

    return __C


def D(arg):
    # start first
    print "start =", arg

    def __D(func):
        def __X(*args, **kwargs):
            print arg
            func(*args, **kwargs)
            print arg
        return __X
    return __D
