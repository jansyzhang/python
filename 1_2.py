# -*- coding: utf-8 -*-
"""
Created on Mon Jan 14 09:40:48 2019

"""

'''from heapq import heappush
from random import shuffle
data = range(10)
shuffle(list(data))
heap = []
for n in data:
    heappush(heap, n)
print(heap)
heappush(heap, 0.5)
print(heap)'''

'''from collections import deque
q = deque(range(5))
q.append(5) #不能直接写在print函数中，若写在print语句，则会输出none
q.appendleft(6)
print(q)
print(q.pop())
print(q.popleft())
q.extend([5])
q.extendleft([6])
print(q)
q.rotate(3) #将元素右移3位
print(q)
q.rotate(-1) #将元素左移1位
print(q)'''
import unittest