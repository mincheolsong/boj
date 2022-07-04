import sys
input = sys.stdin.readline

N=int(input())
l=list()

for _ in range(N):
    command_sentence=list(input().split())

    if command_sentence[0]=='push':
        l.append(int(command_sentence[1]))
    elif command_sentence[0]=='pop':
        if len(l)==0:
            print(-1)
        else:
            print(l.pop())
    elif command_sentence[0]=='size':
        print(len(l))
    elif command_sentence[0]=='empty':
        if len(l)==0:
            print(1)
        else:
            print(0)
    elif command_sentence[0]=='top':
        if len(l)==0:
            print(-1)
        else:
            print(l[-1])




