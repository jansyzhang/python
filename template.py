# -*- coding: utf-8 -*-
"""
Created on Tue Jan 15 15:32:05 2019

"""

import fileinput, re

#匹配括号中的字段
field_pat = re.compile(r'\[(.+?)\]')

#将变量收集到这里
scope = {}

#用于re.sub中
def replacement(match):
    code = match.group(1)
    try:
        #如果字段可以求值，则返回
        return str(eval(code, scope))
    except SyntaxError:
        #否则执行相同作用域内的赋值语句
        exec (code, scope)
        return ''
        
#将所有文本以一个字符串的形式获取
lines = []
for line in fileinput.input():
    lines.append(line)
text = ''.join(lines)

#将field模式的所有匹配项都替换掉
print(field_pat.sub(replacement, text))