# -*- coding: utf-8 -*-
"""
Created on Sat Aug 15 23:18:45 2020

Input should be a dictionary of the form
{[n, d]: [a, b, r, s]}
Should be run after the D_diag in scalar_diagonal_elements
Technically, more efficient to wrap this into that script.
However, this was written after that was already run. 
@author: Tim
"""

import collections
import json
from functools import reduce
from itertools import product

def compare(list1,list2):
    return collections.Counter(list1) == collections.Counter(list2)

def gcd(a,b):
    if b==0:
        return a
    else:
        return gcd(b,a%b)
#  return abs(a) if b==0 else gcd(b, a%b)
def gcd_vec(*args):
    return reduce(gcd, args)

n = 7
d = 2

D = [] # fill in
D_final = {}
D_final["(" + str(n) + "," + str(d) + ")"] = []
generators = {1: [1], 2: [1], 3: [2], 4: [3], 5: [2], 6: [5], 7: [3], 8: [3,5], 
              9: [2], 10: [3], 11: [2], 12: [5,7], 13: [2], 14: [3], 
              15: [2, 14], 16: [3, 15], 17: [3], 18: [5], 19: [2], 20: [3,19], 
              21: [2,20], 22: [7], 23: [5], 24: [5,7,13], 25: [2], 26: [7], 
              27: [2], 28: [3,13], 29: [2], 30: [7,11], 31: [3], 32: [3,31], 
              33: [2,10], 34: [3], 35: [2,6], 36: [5,19], 42: [5, 13], 
              48: [5, 7, 47], 54: [5], 56: [3, 13, 29], 63: [2, 5], 72: [5, 7, 19], 
              84: [5, 11, 13], 96: [5, 7, 31], 108: [5, 107], 126: [5, 13]}

k = 2*d*n
R = generators[k]

for [a, b, r, s] in D:
    flag = True
    for etas in product(range(n), repeat = 4):
        for deltas in product(range(d), repeat = 4):
            eta_one = 2*d*n*etas[0] - 2*d*(etas[1]+etas[3])*(a+b) + 2*a*d*etas[2]
            eta_two = 2*a*d*etas[1] + 2*b*d*(etas[0]+etas[3]) - 2*d*etas[2]*(a+b)
            eta_three = 2*a*d*etas[3] + 2*b*d*(etas[1]+etas[2]) - 2*d*etas[0]*(a+b)

            delta_one = 4*n*r*deltas[0] + (8*r+4*s)*n*deltas[1] + (d-2*r)*n*deltas[2] + (d-2*r-s)*n*deltas[3]
            delta_two = (d-2*r)*n*deltas[0] + (d-2*r-s)*n*deltas[1] + 4*n*r*deltas[2] + (8*r+4*s)*n*deltas[3]
            delta_three = (d-2*r)*n*deltas[0] + (d-2*r-s)*n*deltas[1]+ (d-2*r)*n*deltas[2] + (d-2*r-s)*n*deltas[3]

                
            A = eta_one + delta_one
            B = eta_two + delta_two
            C = eta_three + delta_three                
                    
            x = 2*A - (B + C)
            y = 2*A - (2*d*n + B + C)
            z = B + C  - (2*d*n + B + C)
            inv = [(x)%k, (-x)%k, (y)%k, (-y)%k, (z)%k, (-z)%k]
            for gen in R:
                r_inv = [(gen*w)%k for w in inv]
                if not compare(inv, r_inv):
                    flag = False
                    break        
            x = A + B - (2*d*n + A + B) 
            y = A + B - 2*C
            z = 2*n*d + A + B - 2*C
            for gen in R:
                r_inv = [(gen*w)%k for w in inv]
                if not compare(inv, r_inv):
                    flag = False
                    break 
            x = A + C - 2*B
            y  = A + C - (2*n*d + A + C)
            z = 2*B - (2*n*d + A + C)
            for gen in R:
                r_inv = [(gen*w)%k for w in inv]
                if not compare(inv, r_inv):
                    flag = False
                    break                 
    if flag:
        D_final["(" + str(n) + "," + str(d) + ")"].append([a, b, r, s])
        
print(D_final)
with open("D_final.json", 'a') as f:
    j = json.dumps(D_final)
    f.write(j)
        