from collections import deque, Counter
from string import ascii_lowercase
import sys
import math
import itertools
input = sys.stdin.readline

n,m=map(int,input().split())

def f(n,i):
    cnt=0
    while n//i:
        cnt+=n//i
        n=n//i
    return cnt


answer=min(f(n,2)-(f(m,2)+f(n-m,2)),f(n,5)-(f(m,5)+f(n-m,5)))

print(answer)





