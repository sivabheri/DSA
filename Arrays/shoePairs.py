#python 3.7.1
from collections import Counter
def countPairs(shoes):
    
    mpp = Counter(shoes)
    
    count = 0
    
    for k,v in mpp.items():
        
        size,side = k.split()
        if side == 'L':
            
            v = f'{size} R'
            
            if v in mpp:
                count += min(mpp[k],mpp[v])
        else:
            v = f'{size} L'
            
            if v in mpp:
                count += min(mpp[k],mpp[v])
                
    return count//2
            
        

N = int(input())
shoes = []
for _ in range(N):
    shoes.append(input().strip())


#[7L, 8R, 7L, 6R, 7R,7L, 8R, 6L, 6R,6L]    
print(countPairs(shoes))

