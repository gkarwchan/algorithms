# web location
# https://www.hackerrank.com/challenges/climbing-the-leaderboard/problem

def climbingLeaderboard(scores, alice):
    ranks = sorted(list(set(scores)), reverse=True)
    aliceRanks = []
    maxRight = len(ranks) - 1
    for aliceScore in alice:
        left = 0
        right = maxRight
        while right - left > 1:
            mid = (right - left) // 2
            if aliceScore > ranks[mid + left]:
              # move left
              right = mid + left
            else:
              left = mid + left
        if aliceScore >= ranks[left]:
          aliceRanks.append(left + 1)
        elif aliceScore < ranks[right]:
          aliceRanks.append(right + 2)
        else:
          aliceRanks.append(right + 1)
          
    return aliceRanks