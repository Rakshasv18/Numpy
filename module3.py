#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Sep 20 15:48:36 2022

@author: raksha
"""

#Perform Logic Gate Operations by using Logic_Gates class of logic_gate.py

from logic_gate import Logic_Gates

gate = Logic_Gates()

#Create Truth table
xs = [(0,0), (0,1), (1,0), (1,1)]


# calculate y for AND operation of all values in truth table 
for x in xs:
    res = gate.do_and(x[0], x[1])
    print("AND operation with {} and {}, we will have {}".format(x[0],x[1],res))
    
# calculate y for NAND operation of all values in truth table 
for x in xs:
    ans = gate.do_nand(x[0], x[1])
    print("NAND operation with {} and {}, we will have {}".format(x[0],x[1],ans))
    
    
# calculate y for OR operation of all values in truth table     
for x in xs:
    result = gate.do_or(x[0], x[1])
    print("OR operation with {} and {}, we will have {}".format(x[0],x[1],result))


# calculate y for NOR operation of all values in truth table 

for x in xs:
    results = gate.do_nor(x[0], x[1])
    print("NOR operation with {} and {}, we will have {}".format(x[0],x[1],results))
    

# calculate y for XOR operation of all values in truth table 
for x in xs:
    results_xor = gate.do_xor(x[0], x[1])
    print("XOR operation with {} and {}, we will have {}".format(x[0],x[1],results_xor))

