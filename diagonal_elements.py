import collections
import json
from functools import reduce

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

k = 12 # Initialize k
R = [5,7] # Manually store generators of (Z/k)*
solutions = []
for a in range(k):
    for b in range(k):  
        inv = [a,b,(-a)%k,(-b)%k,(a-b)%k,(b-a)%k]
        count = 0
        for r in R:
          r_inv = [(r*x)%k for x in inv]
          if compare(inv,r_inv):
            count += 1
        if count==len(R):
      # solutions.append(sort([a,b])) 
          solutions.append([a,b])       
# (1,2,2) = (2,1,1) but (1,2,2) != (1,2)      
file = open("elements.txt","a")
file.write(str(k) + '\n')
json.dump(solutions,file)
file.write('\n')
file.close()
print(solutions)            