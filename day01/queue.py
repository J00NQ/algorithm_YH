from collections import deque

queue = deque()
queue.append('A')
queue.append('B')
queue.append('C')
print(queue)

print(queue.popleft())
print(queue.popleft())
print(queue)