from collections import deque, Counter
from string import ascii_lowercase
import sys


input = sys.stdin.readline

T=int(input())

def gcd(a,b):
    if b==0:
        return a
    c=a%b
    return gcd(b,c)

for _ in range(T):
    a,b=map(int,input().split())
    gcd_answer=gcd(a,b)
    print(gcd_answer*(a//gcd_answer)*(b//gcd_answer))
