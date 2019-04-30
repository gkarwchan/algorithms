def saveThePrisoner(n, m, s):
    lastIndex = (s + m -1) % n
    return n if lastIndex == 0 else lastIndex