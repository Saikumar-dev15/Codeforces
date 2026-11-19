import sys
input = sys.stdin.readline

def Evanescent():
    t = int(input())
    s = input().strip()
    
    runs = 1
    
    for i in range (1, t):
        if s[i] != s[i-1]:
            runs += 1
    
    best =0
    for i in range(1, t-1):
        if s[i] != s[i-1] and s[i] != s[i+1]:
           if s[i-1] == s[i+1]:
               best = max(best, 2)
               
           else:
               best = max(best, 1)
               
    return runs - best
        

n = int(input())
for _ in range (n):
    print(Evanescent())
    