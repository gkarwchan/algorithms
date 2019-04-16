def bonAppetit(bill, k, b):
  bill.pop(k)
  owning = b - (sum(bill) / 2)
  print('Bon Appetit' if owning == 0 else int(owning))