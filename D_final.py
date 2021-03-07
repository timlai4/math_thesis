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
import pickle
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

with open('D_diag.pickle', 'rb') as f:
    D = pickle.load(f)

generators = {1: [1], 2: [1], 3: [2], 4: [3], 5: [2], 6: [5], 7: [3], 8: [3,5], 
              9: [2], 10: [3], 11: [2], 12: [5,7], 13: [2], 14: [3], 
              15: [2, 14], 16: [3, 15], 17: [3], 18: [5], 19: [2], 20: [3,19], 
              21: [2,20], 22: [7], 23: [5], 24: [5,7,13], 25: [2], 26: [7], 
              27: [2], 28: [3,13], 29: [2], 30: [7,11], 31: [3], 32: [3,31], 
              33: [2,10], 34: [3], 35: [2,6], 36: [5,19], 42: [5, 13], 
              48: [5, 7, 47], 54: [5], 56: [3, 13, 29], 63: [2, 5], 72: [5, 7, 19], 
              84: [5, 11, 13], 96: [5, 7, 31], 108: [5, 107], 126: [5, 13],
              144: [5, 7, 13], 162: [5], 216: [5, 7, 13], 252: [5, 11, 13], 
              288: [5, 7, 13], 324: [5, 7], 378: [5, 11, 13], 432: [5, 11, 13], 
              504: [5, 11, 13, 17], 648: [5, 7, 13], 756: [5, 11, 13], 
              40: [3, 11, 39], 60: [7, 11, 19], 64: [3, 63], 90: [7, 11],
              80: [3, 7, 79], 112: [3, 5, 111], 120: [7, 11, 19, 29], 
              128: [3, 127], 168: [5, 11, 13, 17], 180: [7, 11, 13], 
              192: [5, 7, 13], 140: [3, 11, 19], 196: [3, 5], 210: [11, 13, 19],
              224: [3, 5, 11], 270: [7, 11], 240: [7, 11, 13, 17], 
              336: [5, 11, 13, 17], 360: [7, 11, 13, 17], 384: [5, 7, 13],
              540: [7, 11, 13], 576: [5, 7, 13], 420: [11, 13, 17, 19],
              588: [5, 11, 13], 630: [11, 13, 19], 672: [5, 11, 13, 17]}

D_final = {}

for n, d in D:
    k = 4*d*n
    R = generators[k]
    D_final["(" + str(n) + "," + str(d) + ")"] = []
    for [a, b, r, s] in D[(n, d)]:
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
    
                x = 2*d*n + A - (d*n - A)
                y = 2*d*n + A - (3*d*n  - A)
                z = d*n - A  - (3*d*n - A)
                inv1 = [(x)%k, (-x)%k, (y)%k, (-y)%k, (z)%k, (-z)%k]
                x = d*n - B - (2*d*n + B)
                y = d*n - B - (3*d*n - B)
                z = 2*d*n + B - (3*d*n - B)
                inv2 = [(x)%k, (-x)%k, (y)%k, (-y)%k, (z)%k, (-z)%k]
                x = d*n - C - (3*d*n - C)
                y = d*n - C - (2*d*n + C)
                z = 3*d*n - C - (2*d*n + C)
                inv3 = [(x)%k, (-x)%k, (y)%k, (-y)%k, (z)%k, (-z)%k]
                for gen in R:
                    r_inv1 = [(gen*w)%k for w in inv1]
                    r_inv2 = [(gen*w)%k for w in inv2]
                    r_inv3 = [(gen*w)%k for w in inv3]
                    if not (compare(inv1, r_inv1) and compare(inv2, r_inv2) and compare(inv3, r_inv3)):
                        flag = False
                        break
                    
                A = eta_one + delta_one
                B = eta_two + delta_two
                C = eta_three + delta_three                
                                  
        if flag:
            D_final["(" + str(n) + "," + str(d) + ")"].append([a, b, r, s])
        
print(D_final)
with open("D_final.json", 'a') as f:
    j = json.dumps(D_final)
    f.write(j)
        