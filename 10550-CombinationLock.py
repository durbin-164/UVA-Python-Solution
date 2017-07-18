'''
Created on Jul 19, 2017

@author: rasel

Due to this picture, the clockwise dial will have counter-clockwise effect and
 the counter-clockwise dial will have clockwise effect.

'''
from builtins import int

while True:
    a,b,c,d = input().split()
    a = int(a)
    b = int(b)
    c = int(c)
    d = int(d)
    
    if a==0 and b ==0 and c == 0 and d == 0:
        break
    
    ans = int(720+360)
     
    if a>=b:
        ans+=(a-b)*9
        
    else :
        ans+= ((40-b)+a)*9
    if c>=b:
        
        ans+=(c-b)*9
    else:
        ans+=((40-b)+c)*9
    if c>=d:
        ans+=(c-d)*9
    else:
        ans+=((40-d)+c)*9
    
    print(ans)
    
    
    
    