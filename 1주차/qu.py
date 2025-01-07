import sys

input = sys.stdin.readline

n = int(input())

qu = []

for i in range(n):
    command = input().split()
    
    if command[0] == "push":
       qu.append(command[1])
       
    elif command[0] == "pop":
        if qu:
           print(qu.pop(0))
        else:
           print(-1)
        
    elif command[0] == "size":
            print(len(qu))
    elif command[0] == "empty":
        if qu: 
            print(0)
        else:  
            print(1)
    elif command[0] == "front":
        if qu:  
            print(qu[0])  
        else:  
            print(-1)
    elif command[0] == "back":
        if qu:  
            print(qu[-1]) 
        else:  
            print(-1)
