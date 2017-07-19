'''
Created on Jul 20, 2017

@author: rasel
'''

test = int(input())

while test>0:
    test-=1
    n = int(input())
    
    ans = int(n*567)
    ans=int(ans/9)
    ans +=7492
    ans*=235
    ans = int(ans/47)
    ans-=498
    
   
    
    if ans<0:
        ans*=-1
   # print(ans)
    
    ans = int(ans/10)
    ans=ans%10
    
    print(ans)