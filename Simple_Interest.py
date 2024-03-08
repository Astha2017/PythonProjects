# Python3 program to find simple interest
# for given principal amount, time and
# rate of interest.
 
 
def simple_interest(p,t,r):
    print('The principal is', p)
    print('The time period is', t)
    print('The rate of interest is',r)
     
    si = (p * t * r)/100
     
    
    return si
     
# Driver code
p=11
t=7
r=9
print (simple_interest(p,t,r))
