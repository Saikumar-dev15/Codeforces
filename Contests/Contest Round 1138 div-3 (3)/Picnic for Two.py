import sys
input = sys.stdin.readline

def solve():
    l,a,b = map(int, input().split())
    
    a_position = set()
    b_position = set()
    
    i =0
    while True:
        val = (i * a) % l

        if val in a_position:
            break

        a_position.add(val)
        i += 1
        
    while True:
        val = (i * b) % l

        if val in b_position:
            break
        
        b_position.add(val)
        i += 1
        
    greater = 1 if len(a_position) > len(b_position) else 0
    result =0 
    
    if greater == 1:
        for num in b_position :
            if num in a_position:
                result += 1
                
    else :
        for num in a_position:
            if num in b_position:
                result +=1 
                
    return result 
    
    


n = int(input())
for _ in range (n):
    print(solve())