import heapq

file = open('code_file.txt', 'r')

minHeap = [0, 0, 0]
heapq.heapify(minHeap)

tmp = 0
while True:
    line = file.readline()
    
    if not line:
        break
    
    if not line.strip():
        heapq.heappushpop(minHeap, tmp)
        tmp = 0
        continue
    
    tmp += int(line.strip())
    
file.close()
print(sum(minHeap))