'''
raw字符串与多行字符串

如果一个字符串包含很多需要转义的字符，
对每一个字符都进行转义会很麻烦。
为了避免这种情况，我们可以在字符串前面加个前缀 r ，
表示这是一个 raw 字符串，里面的字符就不需要转义了。例如：
r'\(~_~)/ \(~_~)/'

但是r'...'表示法不能表示多行字符串，也不能表示包含'和 "的字符串

'''


print(r'''
"To be, or not to be": that is the question.
Whether it's nobler in the mind to suffer.
''')
