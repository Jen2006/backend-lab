#detect loop in a Dict-like list

def detect(d):
    visited=set()
    key=next(iter(d))
    while key in d:
        if key is visited:
            return True
        visited.add(key)
        key=d[key]
    return False 
print(detect({1:2, 2:3, 3:4, 4:2}))
    
        




