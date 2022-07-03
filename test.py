import sys
input = sys.stdin.readline

N=int(input())
l=list(map(int,input().split()))

l_component=list(set(l))
l_component.sort()
l_dict={}
cnt=0
for i in l_component:
    l_dict[i]=cnt
    cnt+=1

for i in l:
    print(l_dict[i])


    




