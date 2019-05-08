# Web location
# https://www.hackerrank.com/challenges/the-time-in-words/problem

def timeInWords(hours, minutes):
    numbers = ['', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine',
        'ten', 'eleven', 'twelve', 'thirteen', 'fourteen', 'quarter', 'sixteen', 'seventeen', 
        'eighteen', 'nighteen']
    tens = ['', '', 'twenty', 'thirty', 'fourty', 'fifty']
    if minutes == 0:
        return numbers[hours] + " o' clock"
    if minutes > 30:
        hours += 1
        indication = 'to'
        minutes = 60 - minutes
    else:
        indication = 'past'
    if minutes < 20:
        minuteText = numbers[minutes]
    elif minutes == 30:
        minuteText = 'half'
    else:
        minuteText = tens[minutes // 10] + (' ' if minutes % 10 > 0 else '') + numbers[minutes % 10]
    
    minuteWord = ' minute ' if minutes == 1 else ' minutes '
        
    text = minuteText + (minuteWord if minutes != 15 and minutes != 30 else ' ') + indication + ' ' + numbers[hours]
    return text


if __name__ == '__main__':
    hours = int(input())
    minutes = int(input())
    text = timeInWords(hours, minutes)
    print (text)
