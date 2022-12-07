file = open('code_file.txt', 'r')
ans = 0
tmp = 0
while True:
    line = file.readline()
    
    if not line:
        break
    
    if not line.strip():
        tmp = 0
        continue
    
    tmp += int(line.strip())

    ans = max(ans, tmp)

    
file.close()
print(ans)