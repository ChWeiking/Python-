'''
可变参数

如果想让一个函数能接受任意个参数，我们就可以定义一个可变参数：
def fn(*args):
    print(args)
可变参数也不是很神秘，Python解释器会把
传入的一组参数组装成一个tuple传递给可变参数，
因此，在函数内部，直接把变量 args 看成一个 tuple 就好了


'''
def average(*args):
    sum = 0.0
    if len(args) == 0:
        return sum
    for x in args:
        sum = sum + x
    return sum / len(args)
print(average())
print(average(1, 2))
print(average(1, 2, 2, 3, 4))
