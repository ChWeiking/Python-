'''
re.finditer(pattern, string[, flags])

搜索string，返回一个顺序访问每一个匹配结果（Match对象）的迭代器。

'''

import re
pattern=re.compile(r'\d+')
for m in re.finditer(pattern,'one1two2three3fore4'):
    print(m.group(),end=" ")
### 输出 ###
# 1 2 3 4
