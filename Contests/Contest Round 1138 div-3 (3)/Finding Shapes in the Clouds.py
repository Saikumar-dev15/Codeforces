import sys
input = sys.stdin.readline

def solve():
    t = int(input())
    s = str(input().strip())
    
    if t % 2 ==1:
        return "No"
    
    for i in range (t-1):
        if s[i] == s[i+1]:
            return "yes"
    return "NO"
        

n = int(input())
for _ in range(n):
    print(solve())