# Non-Divisible Subset

Given a set of distinct integers, print the size of a maximal subset of where the sum of any numbers in
is not evenly divisible by.
**Input Format**
The first line contains space-separated integers, and , the number of values in and the non factor.
The second line contains space-separated integers describing , the unique values of the set.
**Constraints**

All of the given numbers are distinct.
**Output Format**
Print the size of the largest possible subset ( ).
**Sample Input**

```
4 31 7 2 4
```
**Sample Output**

```
3
```
**Explanation**
The sums of all permutations of two elements from are:

```
1 + 7 = 81 + 2 = 3
1 + 4 = 57 + 2 = 9
7 + 4 = 112 + 4 = 6
```
We see that only will not ever sum to a multiple of.


