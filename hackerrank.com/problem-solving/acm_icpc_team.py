# Web location
# https://www.hackerrank.com/challenges/acm-icpc-team/problem

def acmTeam(attendees):
    maxTopics = 0
    teams = 0
    for i in range(len(attendees)):
        for j in range(i + 1, len(attendees)):
            topics = bin(int(attendees[i], 2) | int(attendees[j], 2)).count('1')
            if topics > maxTopics:
                maxTopics = topics
                teams = 1
            elif topics == maxTopics:
                teams += 1
    return [maxTopics, teams]


    
    

if __name__ == '__main__':
    n, m = map(int, input().split())
    attendees = [input() for _ in range(n)]
    result = acmTeam(attendees)
    print('\n'.join(list(map(str, result))))

    
    