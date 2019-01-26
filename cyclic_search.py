from functools import reduce
import collections

def gcd(a,b):
  if b==0:
    return a
  else:
    return gcd(b,a%b)
#  return abs(a) if b==0 else gcd(b, a%b)


def gcd_vec(*args):
  return reduce(gcd, args)

def remove_duplicates(list):
  cleaned_list = []
  for triple in list: # My list will be a list of triples
    if triple not in cleaned_list:
      cleaned_list.append(triple)
  return cleaned_list

compare = lambda x, y: collections.Counter(x) == collections.Counter(y)
# Stack Overflow 159720

k=2 # Initialize k
phi_k = 1 # Size of (Z/k)*
R = [2] # Store r, generators of (Z/k)*
solutions = []

for a in range(k):
  for b in range(k):
    for c in range(k):
      if gcd_vec(a,b,c,k) > 1:
        continue
    inv = [(a+c)%k,(b+c)%k,(-a-c)%k,(-b-c)%k,(a-b)%k,(b-a)%k]
    count = 0
    for i in range(phi_k):
      r_inv = [(R[i]*x)%k for x in inv]
      if compare(inv,r_inv):
        count += 1
    if count==phi_k:
      solutions.append(set([a,b,c]))


#Can I remove duplicates somehow? set_solutions = set(solutions)
                
            
            
