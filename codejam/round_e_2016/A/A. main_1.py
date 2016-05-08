__author__ = 'ThongLe'

def readFile(file):
    strList = []
    infile = open(file)
    for line in infile:
        strList.append(line.strip('\n '))
    return strList

f = open('A. large_output.out', 'w')
testCases = readFile('A-large-practice.in')
for i, s in enumerate(testCases[1:]):
    r = 1
    if (len(s) >= 2):
        if (s[0] <> s[1]):
            r *= 2
        if (s[-2] <> s[-1]):
            r *= 2
        for j in range(1, len(s)-1):
            r *= len(set(s[j-1:j+2]))

    f.write('Case #' + str(i+1) + ': ' + str(r % 1000000007) + '\n')
