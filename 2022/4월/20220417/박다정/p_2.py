import sys

input = sys.stdin.readline
n, m = map(int, input().rstrip().split(' '))
book_locations = list(map(int, input().rstrip().split(' ')))

left = []
right = []
answer = 0

for location in book_locations:
    if location > 0:
        right.append(location)
    else:
        left.append(location)

right.sort(reverse=True)
left.sort()
long_distance = []

if len(left) > 0:
    long_distance.append(abs(left[0]))

if len(right) > 0:
    long_distance.append(right[0])

answer = max(long_distance)
last = answer

for i in range(0, len(right), m):
    if last != right[i]:
        answer += right[i] * 2

for i in range(0, len(left), m):
    if last != abs(left[i]):
        answer += abs(left[i]) * 2

print(answer)
