# -*- coding: utf-8 -*-
"""
Created on Wed Sep 06 14:21:57 2017

@author: sdh
"""
fout = open('output.txt', 'w')
print fout
line1 = "line 1 text,\n"
fout.write(line1)
line2 = "line 2 text!\n"
fout.write(line2)
fout.close()