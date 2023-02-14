#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Sep 20 12:46:46 2022

@author: raksha
"""

##Logic Gate Implementation


import numpy as np


class Logic_Gates:
    
    def __init__(self):
        pass
       
    #do_and function to perform AND operation and bias denoted as b 
    def do_and(self, x1, x2):
        x = np.array([x1,x2])
        w = np.array([0.5,0.5])
        b = -0.8                   
        y = np.sum(x*w) + b 
        return 1 if y>0 else 0
      
    #do_nand function to perform Nand operation 
    def do_nand(self, x1, x2):
        return 1 if self.do_and(x1,x2) == 0 else 0  
    
    #do_or function to perform OR operation and bias denoted as b
    def do_or(self, x1, x2):
        x = np.array([x1,x2])
        w = np.array([0.5,0.5])
        b = -0.2
        y = np.sum(x*w) + b
        return 1 if y > 0 else 0

    #do_nor function to perform NOR operation
    def do_nor(self, x1, x2):
        return 1 if self.do_or(x1,x2) == 0 else 0
    
    #do_xor function to perform NOR operation 
    def do_xor(self,x1,x2):
        y1 = self.do_or(x1,x2)
        y2 = self.do_nand(x1,x2)
        y = self.do_and(y1,y2)
        return y 


if __name__ == '__main__':
    Logic_Gates()
    print("logic_gate.py performs AND, NAND, OR, XOR operations when its been imported by module3.py")



