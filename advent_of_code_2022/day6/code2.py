from collections import deque

pos = 14

file = open('marker.txt', 'r')

while True:
    line = file.readline()
    queue = deque()

    for i in range(len(line)):
        if len(queue) < 14:
            queue.append(line[i])
            continue
        if len(queue) == len(set(queue)):
            break

        queue.popleft()
        queue.append(line[i])
        pos += 1

    if not line:
        break

print(pos)