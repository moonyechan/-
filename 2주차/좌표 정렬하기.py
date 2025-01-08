import sys

input = sys.stdin.readline

li = []

n = int(input())

for _ in range(n):
    x, y = map(int, input().split())
    li.append((x, y))
    print(li)

li.sort()

for x, y in li:
    print(x, y)
