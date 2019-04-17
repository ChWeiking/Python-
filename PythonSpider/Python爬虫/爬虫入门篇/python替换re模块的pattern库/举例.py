'''
Re模块的7个工具方法，例如match，search等等，不过调用方式都是 re.match，re.search的方式，
其实还有另外一种调用方式，可以通过pattern.match，pattern.search调用，这样调用便不用将pattern作为第一个参数传入了

 match(string[, pos[, endpos]]) | re.match(pattern, string[, flags])
 search(string[, pos[, endpos]]) | re.search(pattern, string[, flags])
 split(string[, maxsplit]) | re.split(pattern, string[, maxsplit])
 findall(string[, pos[, endpos]]) | re.findall(pattern, string[, flags])
 finditer(string[, pos[, endpos]]) | re.finditer(pattern, string[, flags])
 sub(repl, string[, count]) | re.sub(pattern, repl, string[, count])
 subn(repl, string[, count]) |re.sub(pattern, repl, string[, count])

'''

from pattern import *
m=match(r'world','hello world!')
print(m.group())

