'''
Created on Jul 18, 2017

@author: rasel
'''

n = int(input())

for i in range(n):
    m, n = input().split()
    
    ans = int (int(m)/3)*int(int(n)/3)
    print(ans)
   