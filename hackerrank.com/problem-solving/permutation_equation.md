# Sequence Equation

Given a sequence of integers, where each element is distinct and satisfies. For
_each_ where , find any integer such that and print the value of on a new line.
For example, assume the sequence. Each value of between and , the length of the sequence, is
analyzed as follows:
1. , so
2. , so
3. , so
4. , so
5. , so

The values for are.
**Function Description**
Complete the _permutationEquation_ function in the editor below. It should return an array of integers that represent the
values of.
permutationEquation has the following parameter(s):
_p_ : an array of integers
**Input Format**
The first line contains an integer , the number of elements in the sequence.
The second line contains space-separated integers where.
**Constraints**

, where.
Each element in the sequence is distinct.
**Output Format**

For each from to , print an integer denoting any valid satisfying the equation on a new line.
**Sample Input 0**

(^3) 2 3 1
**Sample Output 0**
(^23)
1
**Explanation 0**
Given the values of , , and , we calculate and print the following values for each from to
:


1. , so we print the value of on a new line.
2. , so we print the value of on a new line.
3. , so we print the value of on a new line.
**Sample Input 1**

(^5) 4 3 5 1 2
**Sample Output 1**
(^13)
(^54)
2


