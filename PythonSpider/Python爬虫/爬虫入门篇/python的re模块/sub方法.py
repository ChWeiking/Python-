'''
re.sub(pattern, repl, string[, count])

使用repl替换string中每一个匹配的子串后返回替换后的字符串。
 当repl是一个字符串时，可以使用\id或\g、\g引用分组，但不能使用编号0。
 当repl是一个方法时，这个方法应当只接受一个参数（Match对象），并返回一个字符串用于替换（返回的字符串中不能再引用分组）。
 count用于指定最多替换次数，不指定时全部替换。

'''
import re

pattern = re.compile(r'(\w+) (\w+)')
s = 'i say, hello world!'
print(re.sub(pattern, r'\2 \1', s))
def func(m):
    return m.group(1).title() + ' ' + m.group(2).title()
print(re.sub(pattern, func, s))

### output ###
# say i, world hello!
# I Say, Hello World!

