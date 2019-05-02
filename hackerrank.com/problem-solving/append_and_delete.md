# Append and Delete

You have a string, , of lowercase English alphabetic letters. You can perform two types of operations on
:
1. Append a lowercase English alphabetic letter to the end of the string.
2. Deleteempty string. the last character in the string. Performing this operation on an empty string results in an

Given an integer, , and two strings, and , determine whether or not you can convert to by
performing exactly of the above operations on. If it's possible, print Yes; otherwise, print No.
**Input Format**
The first line contains a string, , denoting the initial string.
The second line contains a string, , denoting the desired final string. The third line contains an integer, ,
denoting the desired number of operations.
**Constraints**

and consist of lowercase English alphabetic letters.
**Output Format**
Print Yes if you can obtain string by performing exactly operations on ; otherwise, print No.
**Sample Input 0**

```
hackerhappyhackerrank
9
```
**Sample Output 0**

```
Yes
```
**Explanation 0**
We perform delete operations to reduce string to hacker. Next, we perform append operations (i.e.,
r, a, n, and k), to get hackerrank. Because we were able to convert to by performing exactly
operations, we print Yes.
**Sample Input 1**

```
abaaba
7
```
**Sample Output 1**

```
Yes
```

**Explanation 1**
We perform delete operations to reduce string to the empty string (recall that, though the string will
be empty after deletions, we can still perform a delete operation on an empty string to get the empty
string). Next, we perform append operations (i.e., a, b, and a). Because we were able to convert to
by performing exactly operations, we print Yes.
**Sample Input 2**

```
ashleyash
2
```
**Sample Output 2**

```
No
```
**Explanation 2**
To convert ashley to ash a minimum of steps are needed. Hence we print No as answer.


