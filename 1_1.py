# -*- coding: utf-8 -*-
"""
Created on Tue Dec 25 16:11:08 2018

"""
'''class Rectangle:
    def __init__(self):
        self.width = 0
        self.height = 0
    def setsize(self, size):
        self.width, self.height = size
    def getsize(self):
        return self.width, self.height'''

def conflict(state, nextX):
    nextY = len(state)
    for i in range(nextY):
        if abs(state[i]-nextX) in (0, nextY-i):
            return True
    return False
    
def queens(num=8, state=()):
    for pos in range(num):
        if not conflict(state, pos):
            if len(state) == num-1:
                yield (pos,)
            else:
                for result in queens(num, state + (pos,)):
                    yield (pos,) + result

def prettyprint(solution):
    def line(pos, length=len(solution)):
        return '.'* (pos) + 'X' + '.'*(length-pos-1)
    for pos in solution:
        print(line(pos))
        

'''def flatten(nested):
    for sublist in nested:
        for element in sublist:
            yield element

def flatten(nested):
    try:
        #不要迭代类似于字符串的对象
        try: nested + ''
        except TypeError: pass
        else: raise TypeError
        for sublist in nested:
            for element in flatten(sublist):
                yield element
    except TypeError:
        yield nested






def flatten(nested):
    for sublist in nested:
        for element in sublist:
            yield element

nested = [[1, 2], [3, 4], [5]]
for num in flatten(nested):
    print(num)



class TestIterator:
    value = 0
    def __next__(self):
        self.value += 1
        if self.value > 10: raise StopIteration
        return self.value
    def __iter__(self):
        return self

class Fibs:
    def __init__(self):
        self.a = 0
        self.b = 1
    def __next__(self):
        self.a, self.b = self.b, self.a + self.b
        return self.a
    def __iter__(self):
        return self

class Myclass:
    
    @staticmethod
    def smeth():
        print("this is a static method")
    
    @classmethod
    def cmeth(cls):
        print("this is a class method")

class Rectangle:
    def __init__(self):
        self.width = 0
        self.height = 0
    def __setattr__(self, name, value):
        if name == 'size':
            self.width, self.height = value
        else:
            self.__dict[name]__ = value
    def __getattr__(self, name):
        if name == 'size':
            return self.width, self.height
        else:
            return AttributeError'''