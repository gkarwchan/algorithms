# Drawing Book

Brie’s Drawing teacher asks her class to open their -page book to page number. Brie can either start
turning pages from the front of the book (i.e., page number ) or from the back of the book (i.e., page
number ), and she always turns pages one-by-one (as opposed to skipping through multiple pages at
once). When she opens the book, page is always on the right side:

Each page in the book has two sides, front and back, except for the last page which may only have a front
side depending on the total number of pages of the book (see the Explanation sections below for
additional diagrams).
Given and , find and print the minimum number of pages Brie must turn in order to arrive at page.
**Input Format**
The first line contains an integer, , denoting the number of pages in the book.
The second line contains an integer, , denoting the page that Brie's teacher wants her to turn to.
**Constraints**

**Output Format**
Print an integer denoting the minimum number of pages Brie must turn to get to page.
**Sample Input 0**

(^62)
**Sample Output 0**
1
**Explanation 0**
If Brie starts turning from page , she only needs to turn page:
If Brie starts turning from page , she needs to turn pages:


Because we want to print the minumum number of page turns, we print as our answer.
**Sample Input 1**

(^54)
**Sample Output 1**
0
**Explanation 1**
If Brie starts turning from page , she needs to turn pages:
If Brie starts turning from page , she doesn't need to turn any pages:
Because we want to print the minimum number of page turns, we print as our answer.


