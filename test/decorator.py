# 一个decorator，并返回一个函数
def hello(fn):
    def wrappera():
        print "hello, %s" % fn.__name__
        fn()
        print "goodbye, %s" % fn.__name__
    return wrappera

@hello
def foo():
    print "i am foo"

''' # 多个decorator
@decorator_one
@decorator_two
def func():
    pass

# 相当于
func = decorator_one(decorator_two(func)) '''

def makeHtmlTag(tag, *args, **kwds):
    def real_decorator(fn):
        css_class = " class='{0}'".format(kwds["css_class"]) \
                                     if "css_class" in kwds else ""
        def wrapped(*args, **kwds):
            return "<"+tag+css_class+">" + fn(*args, **kwds) + "</"+tag+">"
        return wrapped
    return real_decorator
 
@makeHtmlTag(tag="b", css_class="bold_css")
@makeHtmlTag(tag="i", css_class="italic_css")
def hello1():
    return "hello world"
 

class myDecorator(object):
 
    def __init__(self, fn):
        print "inside myDecorator.__init__()"
        self.fn = fn
 
    def __call__(self):
        self.fn()
        print "inside myDecorator.__call__()"
 
@myDecorator
def aFunction():
    print "inside aFunction()"
 
print "Finished decorating aFunction()"
 
aFunction()


if __name__ == "__main__":
    #foo()
    print hello1()


# http://coolshell.cn/articles/11265.html