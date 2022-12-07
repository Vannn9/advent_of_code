ans = 0

file = open('assignments.txt', 'r')

while True:
    line = file.readline()

    if not line:
        break
    
    oo, ot, to, tt = '', '', '', ''
    pos = 0
    for i in line:
        if i != '-' and pos == 0:
            oo += i
            continue
        if pos == 0 and i == '-':
            pos += 1
        if i != ',' and pos == 1:
            ot += i
            continue
        if pos == 1 and i == ',':
            pos += 1
        if i != '-' and pos == 2:
            to += i
            continue
        if pos == 2 and i == '-':
            pos += 1
        if pos == 3:
            tt += i
    oo = int(oo)
    ot = int(ot[1:])
    to = int(to[1:])
    tt = int(tt[1:])
    
    if (oo <= to <= ot) or (oo <= tt <= ot) or (to <= oo <= tt) or (to <= ot <= tt):
        ans += 1
        


file.close()
print(ans)