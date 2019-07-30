# ABC Path

### Problem Statement

You will be given a 2-dimensional grid of letters. Write a method to find the length of the longest path of consecutive letters, starting at 'A'. Paths can step from one letter in the grid to any adjacent letter (horizontally, vertically, or diagonally).

For example, in the following grid, there are several paths from 'A' to 'D', but none from 'A' to 'E':
```python
    { "ABE",
      "CFG",
      "BDH",
      "ABC" }
```

One such path is:

    A B .
    C . .
    . D .
    . . .
    (spaces are for clarity only)
so, for this grid, your method should return 4.

### Definition
Class: ABCPath
Method: length
Parameters: tuple (string)
Returns: integer
Method signature: def length(self, grid):
Limits
Time limit (s): 840.000
Memory limit (MB): 64
Notes
- The longest path may start at any 'A' character in the input.
Constraints
- grid will contain between 1 and 50 elements, inclusive.
- Each element of grid will be between 1 and 50 characters long, inclusive.
- Each element of grid will have the same length.
- grid will contain only uppercase letters ('A'-'Z').
Examples
0)
{ "ABE", "CFG", "BDH", "ABC" }
Returns: 4
This is the example from the problem statement.
1)
{ "A" }
Returns: 1
2)
{ "BCDEFGHIJKLMNOPQRSTUVWXYZ" }
Returns: 0
Paths must start with an 'A'.
3)
{ "C", "D", "B", "A" }
Returns: 2
4)
{ "KCBVNRXSPVEGUEUFCODMOAXZYWEEWNYAAXRBKGACSLKYRVRKIO", "DIMCZDMFLAKUUEPMPGRKXSUUDFYETKYQGQHNFFEXFPXNYEFYEX", "DMFRPZCBOWGGHYAPRMXKZPYCSLMWVGMINAVRYUHJKBBRONQEXX", "ORGCBHXWMTIKYNLFHYBVHLZFYRPOLLAMBOPMNODWZUBLSQSDZQ", "QQXUAIPSCEXZTTINEOFTJDAOBVLXZJLYOQREADUWWSRSSJXDBV", "PEDHBZOVMFQQDUCOWVXZELSEBAMBRIKBTJSVMLCAABHAQGBWRP", "FUSMGCSCDLYQNIXTSTPJGZKDIAZGHXIOVGAZHYTMIWAIKPMHTJ", "QMUEDLXSREWNSMEWWRAUBFANSTOOJGFECBIROYCQTVEYGWPMTU", "FFATSKGRQJRIQXGAPLTSXELIHXOPUXIDWZHWNYUMXQEOJIAJDH", "LPUTCFHYQIWIYCVOEYHGQGAYRBTRZINKBOJULGYCULRMEOAOFP", "YOBMTVIKVJOSGRLKTBHEJPKVYNLJQEWNWARPRMZLDPTAVFIDTE", "OOBFZFOXIOZFWNIMLKOTFHGKQAXFCRZHPMPKGZIDFNBGMEAXIJ", "VQQFYCNJDQGJPYBVGESDIAJOBOLFPAOVXKPOVODGPFIYGEWITS", "AGVBSRLBUYOULWGFOFFYAAONJTLUWRGTYWDIXDXTMDTUYESDPK", "AAJOYGCBYTMXQSYSPTBWCSVUMNPRGPOEAVVBGMNHBXCVIQQINJ", "SPEDOAHYIDYUJXGLWGVEBGQSNKCURWYDPNXBZCDKVNRVEMRRXC", "DVESXKXPJBPSJFSZTGTWGAGCXINUXTICUCWLIBCVYDYUPBUKTS", "LPOWAPFNDRJLBUZTHYVFHVUIPOMMPUZFYTVUVDQREFKVWBPQFS", "QEASCLDOHJFTWMUODRKVCOTMUJUNNUYXZEPRHYOPUIKNGXYGBF", "XQUPBSNYOXBPTLOYUJIHFUICVQNAWFMZAQZLTXKBPIAKXGBHXX" }
Returns: 19
5)
{ "EDCCBA", "EDCCBA" }
Returns: 3
6)
{ "AMNOPA", "ALEFQR", "KDABGS", "AJCHUT", "AAIWVA", "AZYXAA" }
Returns: 26
This problem statement is the exclusive and proprietary property of TopCoder, Inc. Any unauthorized use or reproduction of this information without the prior written consent of TopCoder, Inc. is strictly prohibited. (c)2003, TopCoder, Inc. All rights reserved.