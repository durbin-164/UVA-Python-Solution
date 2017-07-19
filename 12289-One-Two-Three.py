'''
Created on Jul 20, 2017

@author: rasel
'''
test = int(input())

while test>0:
    test-=1
    
    st = input()
   # print(st)
    if len(st)==5:
        print(3)
    else:
        if(st[0]=='o' and (st[1]=='n'or st[2]=='e'))or (st[1]=='n' and (st[0]=='o'or st[2]=='e')) or (st[2]=='e' and (st[0]=='0'or st[1]=='n')):
            print(1)
        else:
            print(2)