#first non repeating character
#using dictionary
#input:"aabbcdeff"

def firstchar(s):
    d = {}
    for i in s:
        d[i]=d.get(i,0)+1
    for i in s:
        if d[i]==1:
            return i
    return None

print(firstchar("jjewybxen"))    
            
