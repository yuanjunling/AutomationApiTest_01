#生成器函数 ，函数里只要有yield关键字
def gen_func():
    yield 1
    yield 2
    yield 3
    #惰性求值

def func():
    return 1

if __name__ == "__main__":
    #生成器对象，python编译字节码的时候就产生了
    gen=gen_func()
    for value in gen:
        print(value)
    # re = func()
    # pass

def gen_fib(index):
    n,a,b=0,0,1
    while n<index:
        yield b
        a,b=b,a+b
        n += 1
if __name__ == '__main__':
    for data in gen_fib(3):
        print(data)

