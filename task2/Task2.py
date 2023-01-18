import sys

InfoCircle = []
InfoPoints = []

with open(sys.argv[1]) as circle:
    for line in circle:
        InfoCircle.append([float(x) for x in line.split()])

with open(sys.argv[2]) as points:
    for line in points:
        InfoPoints.append([float(x) for x in line.split()])

xC = InfoCircle[0][0]
yC = InfoCircle[0][1]
rC = InfoCircle[1][0]

for i in range(len(InfoPoints)):
        xP = InfoPoints[i][0]
        yP = InfoPoints[i][1]
        cond1 = rC**2
        cond2 =((xP-xC)**2) + ((yP-yC)**2)
        if cond2 < cond1:
            print(1, end = '\n')

        elif cond2 == cond1:
            print(0, end = '\n')

        else:
            print(2, end = '\n')
