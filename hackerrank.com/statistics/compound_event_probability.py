from fractions import Fraction

x = [4, 3]
y = [5, 4]
z = [4, 4]

P_red_x = x[0] / sum(x)
P_red_y = y[0] / sum(y)
P_red_z = z[0] / sum(z)

p = (P_red_x * P_red_y * (1 - P_red_z)) + (P_red_x * (1 - P_red_y) * P_red_z) + ((1 - P_red_x) * P_red_y * P_red_z)
p_frac = Fraction(p).limit_denominator() # Fraction form

print(f"The probability of drawing 2 reds and one black is {p}, or {p_frac}.")

##################################################################################

'''
Another version
'''

import itertools
from fractions import Fraction

X = ["b","b","b","r","r","r","r"]
Y = ["b","b","b","b","r","r","r","r","r"]
Z = ["b","b","b","b","r","r","r","r"]

# Here the itertools.product will give the Cartesian product of x,y,z as a list of tuples
r = [(i)for i in itertools.product(X,Y,Z)]
# Then count when the entry has two red
# 1 - first alternative:
e = list(map(lambda x : x.count('r') == 2 and x.count('b') == 1,r))
# 2 - second alternative
e = [i.count('r') == 2 for i in r]
result = Fraction(e.count(True),len(e))

print ('the probability is: {}'.format(result))

'''
Using arithmatic
'''

import itertools
from fractions import Fraction
b, r = [1], [0]
X = b*3 + r*4
Y = b*4 + r*5
Z = b*4 + r*4

r = [(i)for i in itertools.product(X,Y,Z)]
e = list(map(lambda x : sum(x) == 1,r))
result = Fraction(e.count(True),len(e))
