import doctest
from typing import List
from math import prod

def split_parts(arr):
    """Return data
    >>> split_parts([5,8,6,4])
    [[5, 8, 6, 4]]
    >>> split_parts([5,8,0,6,4])
    [[5, 8], [6, 4]]
    >>> split_parts([1,8,0,6,4,0,8])
    [[1, 8], [6, 4], [8]]
    >>> split_parts([1,8,-3,0,0,6,4,0,8])
    [[1, 8, -3], [6, 4], [8]]
    >>> split_parts([0,1,8,-3,0,0,6,4,0,8, 0])
    [[1, 8, -3], [6, 4], [8]]
    """
    parts = [[]]
    for x in arr:
      if x == 0:
        parts.append([])
      else:
        parts[-1].append(x)
    return list(filter(lambda x: x, parts))

def prod_arr(arr):
    """Return the product of an array
    >>> prod_arr([3,4,6,7])
    504
    >>> prod_arr([3,4,-3, -5, 6,7])
    7560
    >>> prod_arr([3,4,-3, 6,7])
    42
    >>> prod_arr([3,4,-3, 6,7, -9, 3])
    40824
    >>> prod_arr([3,4,-3, 6,7, -9, 3, -7, 1])
    40824
    >>> prod_arr([3,4,-3, 6,7, -9, 3, -100, 5])
    567000
    >>> prod_arr([-3, 3, -7, 15])
    945
    >>> prod_arr([-3, 3, -6, -7, 15])
    1890
    >>> prod_arr([-3, 0])
    0
    >>> prod_arr([-3])
    -3
    >>> prod_arr([-3,-5,-1])
    15
    """
    if len(arr) == 1: return arr[0]
    if len(arr) == 0: return arr[0]
    negs = [i for i, x in enumerate(arr) if x < 0]
    if len(negs) % 2 == 0:
        return prod(arr)
    else:
        bf = arr[:negs[-1]]
        af = arr[negs[0]+1:]
        val = max(prod(bf) , prod(af)) if len(bf) > 0 and len(af) > 0 else prod(bf) if len(bf) > 0 else prod(af)
        return val
        
def prod_sub(arr: List[int]) -> int:
    """Return the max of product of sub-array
    >>> prod_sub([-2,0])
    0
    """
    parts = split_parts(arr)
    vals = [prod_arr(x) for x in parts]
    if len(parts) > 1 or 0 in arr:
            vals.append(0)
    return max(vals)
    
if __name__ == '__main__':
    doctest.testmod()
    # print(split_parts([5,8,6,4]))
    # print (name_value(["codewars","abc","xyz"])