# Viral Advertising

HackerLand Enterprise is adopting a new viral advertising strategy. When they launch a new product, they
advertise it to exactly people on social media.

On the first day, half of those people (i.e., ) like the advertisement and each person
shares it with of their friends; the remaining people (i.e., ) delete the advertisement
because it doesn't interest them. So, at the beginning of the second day,
people receive the advertisement.
On the second day, half of the people who received the advertisement share it with new friends. So, at
the beginning of the third day, people receive the advertisement. The
diagram below depicts the advertisement's virality over the first three days (green denotes a person that
likes the advertisement and red denotes a person that disliked and deleted it):

Assume that at the beginning of the day, people received the advertisement, people like
and share it with new friends, and people dislike and delete it. At the beginning of the
day, people receive the advertisement.
Given an integer, , find and print the total number of people who liked HackerLand Enterprise's
advertisement during the first days. It is guaranteed that no two people have any friends in common
and, after a person shares the advertisement with a friend, the friend always sees it the next day.
**Input Format**
A single integer, , denoting a number of days.
**Constraints**

**Output Format**
Print the number of people who liked the advertisement during the first days.
**Sample Input**

```
3
```
**Sample Output**

```
9
```
**Explanation**
This example is depicted by the diagram at the top of the challenge. people liked the advertisement on
the first day, people liked the advertisement on the second day and people liked the advertisement


on the third day, so the answer is.


