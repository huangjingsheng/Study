
def do_foo():
    print("foo!")

def do_bar():
    print("bar!")
class Print():
    def do_foo(self,a):
        s =  5 + a
        print(a)
        return s
    def do_bar(self):
        print( "bar!")


    @staticmethod
    def static_foo():
        print("static foo!")

    @staticmethod
    def static_bar():
        print("static bar!")
def main():
    obj = Print()
    #func_name = "do_foo"
    #static_name = "static_foo"
    #eval(func_name)()
    #getattr(obj, func_name)()

    #getattr(Print, static_name)()

    func_name = "do_foo"
    static_name = "static_bar"
    #eval(func_name)()
    #getattr(obj, func_name)()
    #getattr(Print, static_name)()

    #拿到obj名称为func_name的函数赋值给f
    f = getattr(obj,func_name)
    s = f(5)
    print(s)


if __name__ == '__main__':
    main()
