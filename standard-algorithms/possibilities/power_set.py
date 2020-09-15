import doctest
def power_set(input):
  """Return all possible options in a set
  """
  if len(input) == 1:
    return input
  else:
    item = input.pop(0)
    return [item] + [ [i] + [item] for i in input] + power_set(input)


if __name__ == '__main__':
  # doctest.testmod()
  print (power_set([1,2]))
  print (power_set([1,2,3]))
  print (power_set([1,2,3,4]))
