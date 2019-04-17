'''
迭代字典的值
python2.x才有用 itervalues() 方法替代 values() 方法，迭代效果完全一样：
'''

d = { 'Adam': 95, 'Lisa': 85, 'Bart': 59 }
for v in d.values():
    print(v)
    
