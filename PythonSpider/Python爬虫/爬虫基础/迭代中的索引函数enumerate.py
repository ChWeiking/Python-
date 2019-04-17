'''
对于有序集合，元素确实是有索引的。有的时候，我们确实想在 for 循环中拿到索引，怎么办？

方法是使用 enumerate() 函数：


'''

L = ['Adam', 'Lisa', 'Bart', 'Paul']
for index,name in enumerate(L):
    print(index,"-",name)
