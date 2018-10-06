# -*- coding: utf-8 -*-
"""
Created on Mon Apr  2 17:55:27 2018

@author: sdh
"""

#Helpful: https://realpython.com/instance-class-and-static-methods-demystified/

class MyClass:
    def method(self):
        return 'instance method called', self

    @classmethod
    def classmethod(cls):
        return 'class method called', cls
    #use class methods to modify all instances to be made thereafter. 

    @staticmethod
    def staticmethod():
        return 'static method called'