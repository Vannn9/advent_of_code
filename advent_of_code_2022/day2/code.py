ans = 0

file = open('rps.txt', 'r')

while True:
    line = file.readline()

    if not line:
        break
    
    tmp = line[2]
    if tmp == 'X':
        ans += 1
    elif tmp == 'Y':
        ans += 2
    else:
        ans += 3

    tmp2 = line[0]
    if tmp2 == 'A' and tmp == 'Y' or tmp2 == 'B' and tmp == 'Z' or tmp2 == 'C' and tmp == 'X':
        ans += 6
    elif tmp2 == 'A' and tmp == 'X' or tmp2 == 'B' and tmp == 'Y' or tmp2 == 'C' and tmp == 'Z':
        ans += 3


file.close()
print(ans)