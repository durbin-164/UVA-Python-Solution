'''
Created on Jul 19, 2017

@author: rasel
'''
test = int(input())
while test:
    test-=1
    n = int(input())
    
    mx = -123
    mn = 99999999999
    
    '''
    list = [int(x) for x in input().split()]
        
    mx = max(list)
    mn = min(list)
        
    ans = (mx-mn)*2
    print(ans)
   '''

    
    for x in input().split():
        x = int(x)
        mx = max(mx,x)
        mn = min(mn,x)
        
    ans = (mx-mn)*2
    print(ans)
    
    
    