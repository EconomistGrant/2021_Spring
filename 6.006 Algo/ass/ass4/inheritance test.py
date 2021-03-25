# -*- coding: utf-8 -*-
"""
Created on Wed Mar 17 18:13:09 2021

@author: a
"""

class A:
    
    def f(self):
        self.g()
    def g(self):
        print('a')
class B(A):
    def g(self):
        print("b")
        
    

b = B()
b.f()