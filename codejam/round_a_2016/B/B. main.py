__author__ = 'ThongLe'
import string

def readFile(file):
    strList = []
    infile = open(file)
    for line in infile:
        strList.append(line)

    testCases = []
    t = int(strList[0])

    k = 1
    for i in range(t):
        n = int(strList[k])
        l = []
        for j in range(1, n * 2):
            l.append([int(_) for _ in strList[k + j].strip('\n ').split(" ")])
        testCases.append((n, l))
        k += n * 2
    return testCases

namefile = 'B-large-practice'
testCases = readFile(namefile + '.in')
# for i, s in zip(range(int(testCases[0])), testCases[1:]):
#   r = s[0]
#   for c in s[1:]:
#     if (r[0] > c):
#       r += c
#     else:
#       r = c + r
#   f.write('Case #' + str(i+1) + ': ' + r)

f = open(namefile + '.out', 'w')
for i, t in zip(range(len(testCases)), testCases):
    l = []
    d = {}

    for row in t[1]:
        for ent in row:
            if (ent in d):
                d[ent] += 1
            else:
                d[ent] = 1

    for key, value in d.items():
        if (value % 2 == 1):
            l.append(key)

    l.sort()

    f.write('Case #' + str(i+1) + ': ' + string.join([str(_) for _ in l]) + '\n')