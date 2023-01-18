import sys

n = int(sys.argv[1])
m = int(sys.argv[2])
CircleMass = list(range(1, n+1))
StartM = 1
Way = list()
count = 1
while not (count == 1 and StartM == m):
    if StartM == 1:
        Way.append(count)
    if StartM == m:
        StartM = 1
        continue
    if count == n:
        count = 1
        StartM += 1
        continue
    count += 1
    StartM += 1
print(Way)

