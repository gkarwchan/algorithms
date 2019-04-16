# First try: clear
'''
this is a clear algorithm, that is easy to understand and follow
'''
def dayOfProgrammer(year):
  lear_year = '12.09.{}'
  non_leap_year = '13.09.{}'
  if year == 1918:
    return '26.09.1918'
  if not year % 4 == 0:
    return non_leap_year.format(year)
  elif year % 400 == 0:
    return lear_year.format(year)
  elif year % 100 == 0 and year > 1918:
    return non_leap_year.format(year)
  else:
    return lear_year.format(year)

# Second try: condensed
'''
this is less clear than the one above, but more dendensed
'''

def dayOfProgrammer2(year):
  if year == 1918:
    return '26.09.1918'
  elif year % 4 == 0 and ((not year % 100 == 0) or year % 400 == 0 or year < 1918):
    return '12.09.{}'.format(year)
  else:
    return '13.09.{}'.format(year)