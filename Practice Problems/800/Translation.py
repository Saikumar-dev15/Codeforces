def Translation():
    s = input().strip()
    t = input().strip()
    
    if s == t[::-1]:
        print("Yes") 
        
    else:
        print("No")
    
Translation()
        
