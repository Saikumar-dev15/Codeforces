import sys 
input = sys.stdin.readline

def solve():
    n, k , p = map(int, input().split())
    joy_points = list(map(int , input().split()))
    joy_points.sort(reverse=True)
    
    joy = 0
    
    while len(joy_points) >= k:
        c =0 
        for _ in range(k):
                c += joy_points.pop()

        if c <= p :
            joy += p

        else :
            joy += c
            break

    return joy + sum(joy_points)
        

n = int(input())
for _ in range (n):
    print(solve())