for x in range(7):
  print ('---------------------------')
  for y in range(7):
    print ('  *********************')
    for z in range(7):
      print (x, y, z)
      if z == 3:
        break
    print ('  *********************')
  print ('---------------------------')
  