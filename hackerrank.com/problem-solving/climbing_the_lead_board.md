# Climbing the

# Leaderboard

Alice is playing an arcade game and wants to climb to the top of the leaderboard and wants to track her ranking. The
game uses Dense Ranking, so its leaderboard works like this:
The player with the highest score is ranked number on the leaderboard.
Players who have equal scores receive the same ranking number, and the next player(s) receive the immediatelyfollowing ranking number.

For example, the four players on the leaderboard have high scores of , , , and. Those players will have
ranks , , , and , respectively. If Alice's scores are , and , her rankings after each game are , and
.
**Function Description**
Complete the _climbingLeaderboard_ function in the editor below. It should return an integer array where each element
represents Alice's rank after the game.
climbingLeaderboard has the following parameter(s):
_scores_ : an array of integers that represent leaderboard scores
_alice_ : an array of integers that represent Alice's scores
**Input Format**
The first line contains an integer , the number of players on the leaderboard.
The next line contains space-separated integers , the leaderboard scores in decreasing order.
The next line contains an integer, , denoting the number games Alice plays.
The last line contains space-separated integers , the game scores.
**Constraints**

for
for
The existing leaderboard, , is in _descending_ order.
Alice's scores, , are in _ascending_ order.
**Subtask**
For of the maximum score:

**Output Format**

Print integers. The integer should indicate Alice's rank after playing the game.
**Sample Input 0**


(^7) 100 100 50 40 40 20 10
(^4) 5 25 50 120
**Sample Output 0**
(^64)
(^21)
**Explanation 0**
Alice starts playing with players already on the leaderboard, which looks like this:
After Alice finishes game , her score is and her ranking is :
After Alice finishes game , her score is and her ranking is :
After Alice finishes game , her score is and her ranking is tied with Caroline at :


## After Alice finishes game , her score is and her ranking is :

- Sample Input
   -
   -
- Sample Output
   -
   -
   -


