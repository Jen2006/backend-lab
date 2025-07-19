#find the missing number
#using formula for sum of first n natural numbers

def miss(l):
    n=len(l)+1
    totalsum= n*(n+1)//2
    return totalsum - sum(l)

lst=[1,2,4,5]  
print(miss(lst))