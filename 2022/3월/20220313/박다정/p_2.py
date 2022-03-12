import sys
import collections

input = sys.stdin.readline

n, m = map(int, input().rstrip().split(' '))
locations = list(map(int, input().rstrip().split(' ')))
queue = collections.deque([i for i in range(1, n + 1)])
result = 0


def rotate_to_left(n):
    for _ in range(n):
        tmp = queue.popleft()
        queue.append(tmp)


def rotate_to_right(n):
    for _ in range(n):
        tmp = queue.pop()
        queue.appendleft(tmp)


for location in locations:
    index = queue.index(location)
    left = index
    right = len(queue) - index

    if queue[0] == location:
        queue.popleft()
        continue

    if left < right:
        rotate_to_left(left)
        result += left
    else:
        rotate_to_right(right)
        result += right
    queue.popleft()
print(result)
