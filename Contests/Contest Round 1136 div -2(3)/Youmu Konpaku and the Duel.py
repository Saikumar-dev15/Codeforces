import sys 
n = sys.stdin.readline

def solve():
    youkai = int(input())
    best = youkai
    
    for k in range (1,1001):
        hp = youkai
        power = k+1
        moves = k
        
        while hp> 0 and moves < best:
            hp -= power
            
            if power > 1:
                power -= 1
            moves += 1
            
        if hp<= 0:
            best = min(moves, best)
            
    return best
            


n = int(input())
for _ in range (n):
    print(solve())