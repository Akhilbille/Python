def countDer(n):
     
    
    if (n == 1): return 0
    if (n == 2): return 1
     
    
    return(n - 1)*(countDer(n - 1)+countDer(n - 2))
 

n = 3
print("Count of Derangements is ", countDer(n))
