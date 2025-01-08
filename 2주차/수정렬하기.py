import sys

input = sys.stdin.readline

n = int(input())

li = []
for i in range(n):
    li.append(int(input()))

li.sort()
for a in li:
    print(a)
        
