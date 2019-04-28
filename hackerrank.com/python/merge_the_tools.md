# Merge the Tools!

Consider the following:
A string, , of length where.
An integer, , where is a factor of.
We can split into subsegments where each subsegment, , consists of a contiguous block of
characters in. Then, use each to create string such that:
The characters in are a subsequence of the characters in.
Any repeat occurrence of a character is removed from the string such that each character in
occurs exactly once. In other words, if the character at some index in occurs at a previous index
in , then do not include the character in string.
Given and , print lines where each line denotes string.

**Input Format**
The first line contains a single string denoting.
The second line contains an integer, , denoting the length of each subsegment.
**Constraints**

```
, where is the length of
```
It is guaranteed that is a multiple of.
**Output Format**
Print lines where each line contains string.

**Sample Input**

```
AABCAAADA 3
```
**Sample Output**

```
ABCA
AD
```
**Explanation**

String is split into equal parts of length. We convert each to by removing any
subsequent occurrences non-distinct characters in :
1.
2.
3.
We then print each on a new line.

