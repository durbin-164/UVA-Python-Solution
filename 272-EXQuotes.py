'''
Created on Jul 17, 2017

@author: rasel
'''

con =0

while True: 
    try:
        st = input()
    except:
        break
   # print(st)
    for i in range(len(st)):
       # print(st[i])
        if st[i]=='"':
           # print(i)
            if con % 2 == 0:
                print('``',end='')
               # i+=2
               # print(con)
                con+=1
            else :
                 print("''",end='')
                # i+=2
                 con+=1
        else:
           print(st[i],end='')
        
    print()
            
            
        
    
    #print(st)