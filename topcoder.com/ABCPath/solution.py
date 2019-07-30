class ABCPath:
  def __computeBoundaies(self, coord, points):
    u = coord[0] - (1 if coord[0] > 0 else 0)
    b = coord[0] + (1 if coord[0] < (len(points) - 1) else 0) + 1
    l = coord[1] - (1 if coord[1] > 0 else 0)
    r = coord[1] + (1 if coord[1] < (len(points[0]) - 1) else 0) + 1
    return (u, b, l, r)

  def traverse(self, searchChar, points, searchAreaBoundries=None):

    if searchAreaBoundries == None:
      u = 0
      b = len(points)
      l = 0
      r = len(points[0])
    else:
      (u, b, l, r) = searchAreaBoundries
    
    charLocations = [(i, j) for i in range(u, b) for j in range(l, r) if points[i][j] == searchChar]
    if len(charLocations) == 0:
      return ord(searchChar) - 65
    else:
      nextChar = chr(ord(searchChar) + 1)
      searchAreaBoundries
      results = list(map(lambda x: self.traverse(nextChar, points, self.__computeBoundaies(x, points)), charLocations))
      return max(results)

  def length(self, grid):
    points = [list(i) for i in grid]

    output = self.traverse('A', points)
    return output


if __name__ == '__main__':
  input1 = ("ABE", "CFG", "BDH", "ABC")
  input2 = ('A')
  input3 = ('BCDEFGHIJKLMNOPQRSTUVWXYZ')
  input4 = ( "C", "D", "B", "A" )
  input5 = ("KCBVNRXSPVEGUEUFCODMOAXZYWEEWNYAAXRBKGACSLKYRVRKIO", "DIMCZDMFLAKUUEPMPGRKXSUUDFYETKYQGQHNFFEXFPXNYEFYEX", "DMFRPZCBOWGGHYAPRMXKZPYCSLMWVGMINAVRYUHJKBBRONQEXX", "ORGCBHXWMTIKYNLFHYBVHLZFYRPOLLAMBOPMNODWZUBLSQSDZQ", "QQXUAIPSCEXZTTINEOFTJDAOBVLXZJLYOQREADUWWSRSSJXDBV", "PEDHBZOVMFQQDUCOWVXZELSEBAMBRIKBTJSVMLCAABHAQGBWRP", "FUSMGCSCDLYQNIXTSTPJGZKDIAZGHXIOVGAZHYTMIWAIKPMHTJ", "QMUEDLXSREWNSMEWWRAUBFANSTOOJGFECBIROYCQTVEYGWPMTU", "FFATSKGRQJRIQXGAPLTSXELIHXOPUXIDWZHWNYUMXQEOJIAJDH", "LPUTCFHYQIWIYCVOEYHGQGAYRBTRZINKBOJULGYCULRMEOAOFP", "YOBMTVIKVJOSGRLKTBHEJPKVYNLJQEWNWARPRMZLDPTAVFIDTE", "OOBFZFOXIOZFWNIMLKOTFHGKQAXFCRZHPMPKGZIDFNBGMEAXIJ", "VQQFYCNJDQGJPYBVGESDIAJOBOLFPAOVXKPOVODGPFIYGEWITS", "AGVBSRLBUYOULWGFOFFYAAONJTLUWRGTYWDIXDXTMDTUYESDPK", "AAJOYGCBYTMXQSYSPTBWCSVUMNPRGPOEAVVBGMNHBXCVIQQINJ", "SPEDOAHYIDYUJXGLWGVEBGQSNKCURWYDPNXBZCDKVNRVEMRRXC", "DVESXKXPJBPSJFSZTGTWGAGCXINUXTICUCWLIBCVYDYUPBUKTS", "LPOWAPFNDRJLBUZTHYVFHVUIPOMMPUZFYTVUVDQREFKVWBPQFS", "QEASCLDOHJFTWMUODRKVCOTMUJUNNUYXZEPRHYOPUIKNGXYGBF", "XQUPBSNYOXBPTLOYUJIHFUICVQNAWFMZAQZLTXKBPIAKXGBHXX")
  input6 = ( "EDCCBA", "EDCCBA")
  input7 = ( "AMNOPA", "ALEFQR", "KDABGS", "AJCHUT", "AAIWVA", "AZYXAA")
  abcPath = ABCPath()
  b = abcPath.length(input7)
  print(b)