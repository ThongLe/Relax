__author__ = 'ThongLe'

def readFile(file):
    strList = []
    infile = open(file)
    for line in infile:
        strList.append(line)
    return strList

f = open('A. large_output.out', 'w')
testCases = readFile('A. A-large-practice.in')
for i, s in zip(range(int(testCases[0])), testCases[1:]):
  r = s[0]
  for c in s[1:]:
    if (r[0] > c):
      r += c
    else:
      r = c + r
  f.write('Case #' + str(i+1) + ': ' + r)
