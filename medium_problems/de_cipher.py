import re
import string
from values import decoded_txt, original_txt

def to_regex(st):
    char_match = lambda mtc: '[a-z]' if mtc.group(0) >= 'a' else '[A-Z]'
    rp = re.compile('[A-Za-z]')
    a = re.sub(',', '[,(){}\[\]]', st)
    return rp.sub(char_match, a)

def findMatchedPair(encodpos=0, decodpos=0):
    r = re.compile(r'[A-Za-z "\',]{100,}\.')
    encode_matched = r.search(decoded_txt, pos=encodpos)
    if not encode_matched: return None
    regex_pattern = to_regex(encode_matched.group(0))
    r2 = re.compile(regex_pattern)
    decoded_match = r2.search(original_txt)
    if decoded_match:
      return (encode_matched.group(0), decoded_match.group(0), encode_matched.end(0), decoded_match.end(0))
    else:
      return None



def decode(cod, org, inputdict = {}):
  for a,b in zip(cod, org):
    if a not in [' ', '.', ',', '"', '\'']:
      if a in inputdict:
        if inputdict[a] != b: return None
      else:
        inputdict[a.lower()] = b.lower()
  return inputdict

def simpleApproach():
  start_pos, map_key = 0, {}
  while True:
    match_data = findMatchedPair(encodpos=start_pos)
    if match_data:
      start_pos = match_data[2]
      map_key = decode(match_data[0], match_data[1], map_key)
      if len(map_key) == 26: break
    else:
      break
  kk = {v:k  for k, v in map_key.items()}
  return ''.join(kk[i] for i in string.ascii_lowercase)




rslt = simpleApproach()
print(rslt)
# print(string.ascii_lowercase)
# jj = ''.join(rslt[i] if i in rslt else '-' for i in string.ascii_lowercase)
# print(jj)


