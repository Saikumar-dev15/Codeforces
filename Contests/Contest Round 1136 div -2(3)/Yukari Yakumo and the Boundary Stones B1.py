import sys
n = sys.stdin.readline

def solve():
    x0,y0,r = map(int, input().split())
    s = input().strip()
                
    states = {(x0 ,y0)}
    best = x0 +y0 
            
    for ch in s:
        new_states = set()
        
        for a,b in states:
            if ch == '+':
                if a>0 :
                    new_states.add((a-1, b+1))
                if b>0:
                    new_states.add((a, b+1))
            else:
                if a> 0:
                    new_states.add((a-1, b))
                if b>0:
                    new_states.add((a+1,b-1))
        states = new_states
        for a,b in states:
            best = max(best, a+b)
            
    return best 


n = int(input())
for _ in range (n):
    print(solve())