from queue import Queue
import sys
input = sys.stdin.readline

n=int(input())
queue=Queue()

for i in range(n):
    command=input().split()
    if command[0]=='push':
        queue.put(int(command[1]))
        if queue.qsize()==1:
            front=int(command[1])
        end=int(command[1])
    elif command[0]=='pop' and queue.qsize()>0:
        print(queue.get())
    elif command[0]=='pop' and queue.qsize()==0:
        print(-1)
    elif command[0]=='size':
        print(queue.qsize())
    elif command[0]=='empty':
        if queue.empty():
            print(1)
        else:
            print(0)
    elif command[0]=='front':
        if queue.qsize()>0:
            print(front)
        else:
            print(-1)
    elif command[0]=='back':
        if queue.qsize()>0:
            print(end)
        else:
            print(-1)



