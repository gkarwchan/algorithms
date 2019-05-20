#!/bin/python3
def gradingStudents(grades):
      return [str(i) if i < 38 or i % 5 < 3 else str(i + 5 - i % 5) for i in grades]

if __name__ == '__main__':
      n = int(input())
      grades = [int(input()) for _ in range(n)]
      print('\n'.join(gradingStudents(grades)))

      # result = sorted(list(map(lambda x: ''.join(x), combinations(s, int(k)))))
      # print ('\n'.join(result))
      
      



