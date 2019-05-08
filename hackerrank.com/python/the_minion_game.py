https://www.hackerrank.com/challenges/the-minion-game/problem

'''
First attempt
'''

def minion_game(string):
    vowels = 'AEIOU'
    stuart = 0
    kevin = 0
    for i in range(len(string)):
        if string[i] in vowels:
            kevin += len(string) - i
        else:
            stuart += len(string) - i
    result = 'Kevin {}'.format(kevin) if kevin > stuart else 'Stuart {}'.format(stuart) if stuart > kevin else 'Draw'
    print (result)



'''
Second attempt
taking into account 
sum numbers from 1 to n = n (n+1) / 2

'''
def minion_game1(string):
    length = len(string)
    vowels = 'AEIOU'
    kevin = sum([length - i for i in range(length) if string[i] in vowels])
    stuart = int((length * (length + 1) / 2) - kevin)
    result = 'Kevin {}'.format(kevin) if kevin > stuart else 'Stuart {}'.format(stuart) if stuart > kevin else 'Draw'
    print (result)



if __name__ == '__main__':
    s = input()
    minion_game(s)