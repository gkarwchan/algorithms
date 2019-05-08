# https://www.hackerrank.com/challenges/find-a-string/problem

'''
First attempt. Clear
As not everything should be one linear, this is a clear solution
'''

def count_substring(string, sub_string):
    beg = 0
    count = 0
    while True:
        ind = string.find(sub_string, beg)
        if ind == -1:
            break
        count += 1
        beg = ind + 1
    return count


'''
But to show a one linear code and show the strength of Python
'''
def count_substring1(string, sub_string):
  return sum([1 for i in range(0, len(string) - len(sub_string) + 1) if string[i: i + len(sub_string)] == sub_string])