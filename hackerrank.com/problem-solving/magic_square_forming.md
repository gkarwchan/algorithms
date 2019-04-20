# Forming a Magic

# Square

We define a magic square to be an matrix of distinct positive integers from to where the sum
of any row, column, or diagonal of length is always equal to the same number: the magic constant.
You will be given a matrix of integers in the inclusive range. We can convert any digit to
any other digit in the range at cost of. Given , convert it into a magic square at minimal
cost. Print this cost on a new line.
**Note:** The resulting magic square must contain distinct integers in the inclusive range.
For example, we start with the following matrix :

(^51  35  )
6 4 2
We can convert it to the following magic square:
(^81  35  )
6 7 2
This took three replacements at a cost of.
**Input Format**
Each of the lines contains three space-separated integers of row.
**Constraints
Output Format**
Print an integer denoting the minimum cost of turning matrix into a magic square.
**Sample Input 0**
4 9 23 5 7
8 1 5
**Sample Output 0**
1
**Explanation 0**
If we change the bottom right value, , from to at a cost of , becomes a magic
square at the minimum possible cost.
**Sample Input 1**
4 8 24 5 7
6 1 6


**Sample Output 1**

```
4
```
**Explanation 1**
Using 0-based indexing, if we make
-> at a cost of
-> at a cost of
-> at a cost of ,
then the total cost will be.


