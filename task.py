# -*- coding: utf-8 -*-
"""
Created on Thu Oct  4 13:36:28 2018

@author: sdh
"""

class Task: # employs objects for multiple tasks 
    def __init__(self, **kwargs):
        self.cnt=0
        
    def do(self):	# method may be overwritten. 
        self.cnt = self.cnt +1
        result = 'done '+str(self.cnt)+' times'
        if self.cnt==1:
            result = 'done once'
        return result
        
class TimedTask(Task):
    def do(self): #overide	
        self.cnt = self.cnt +1
        return (self.cnt)
