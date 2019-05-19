# https://www.hackerrank.com/challenges/time-conversion/problem

def timeConversion(s):
    hour, min, half = s[0:2], s[2:8], s[-2:-1]
    if half == 'A':
        newHour = '00' if hour == '12' else hour
    else:
        newHour = hour if hour == '12' else str(int(hour) + 12)
    return newHour + min


if __name__ == '__main__':
    s = input()
    print(timeConversion(s))
    

