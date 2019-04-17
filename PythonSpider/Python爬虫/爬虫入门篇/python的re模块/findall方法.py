'''
搜索string，以列表形式返回全部能匹配的子串。
'''
import re
pattern=re.compile(r'\d+')
print(re.findall(pattern,'one1two2three3fore4'))
### 输出 ###
# ['1', '2', '3', '4']
