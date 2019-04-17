'''
list列表生成式for的嵌套


对于字符串 'ABC' 和 '123'，可以使用两层循环，生成全排列：
>>> [m + n for m in 'ABC' for n in '123']
['A1', 'A2', 'A3', 'B1', 'B2', 'B3', 'C1', 'C2', 'C3']

翻译成循环代码就像下面这样：
L = []
for m in 'ABC':
    for n in '123':
        L.append(m + n)

'''

print([x*100+y*10+z for x in \
       range(10) for y in range(10) \
       for z in range(10) if x==z and x!=0])
