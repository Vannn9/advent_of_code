ans = 0

file = open('rps.txt', 'r')

while True:
    line = file.readline()

    if not line:
        break
    
    tmp = line[0]
    tmp2 = line[2]

    if tmp2 == 'Z':
        if tmp == 'A':
            ans += 2
        elif tmp == 'B':
            ans += 3
        else:
            ans += 1
        ans += 6
    elif tmp2 == 'Y':
        if tmp == 'A':
            ans += 1
        elif tmp == 'B':
            ans += 2
        else:
            ans += 3
        ans += 3
    else:
        if tmp == 'A':
            ans += 3
        elif tmp == 'B':
            ans += 1
        else:
            ans += 2


file.close()
print(ans)