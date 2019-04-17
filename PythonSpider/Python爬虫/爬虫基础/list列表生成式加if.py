'''
list列表生成式加if
'''

def toUppers(L):
    return [x.upper() for x in L if isinstance(x,str)]

print(toUppers(['Hello', 'world', 101]))
