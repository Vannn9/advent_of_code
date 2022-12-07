stack = [[], ['T', 'P', 'Z', 'C', 'S', 'L', 'Q', 'N'], ['L', 'P', 'T', 'V', 'H', 'C', 'G'], ['D', 'C', 'Z', 'F'], ['G', 'W', 'T', 'D', 'L', 'M', 'V', 'C'], ['P', 'W', 'C'], ['P', 'F', 'J', 'D', 'C', 'T', 'S', 'Z'], ['V', 'W', 'G', 'B', 'D'], ['N', 'J', 'S', 'Q', 'H', 'W'], ['R', 'C', 'Q', 'F', 'S', 'L', 'V']]
ans = []

file = open('moves.txt', 'r')

while True:
    line = file.readline()


    if not line:
        break

    words = line.split(' ')
    words2 = []
    words2.append(int(words[1]))
    words2.append(int(words[3]))
    words2.append(int(words[5]))
    
    for i in range(words2[0]):
        stack[words2[2]].append(stack[words2[1]].pop())


file.close()
for i in range(1, len(stack)):
    ans.append(stack[i][-1])
print(''.join(ans))