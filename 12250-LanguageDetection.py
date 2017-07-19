'''
Created on Jul 20, 2017

@author: rasel
'''


dic = {'HELLO':'ENGLISH','HOLA':'SPANISH','HALLO':'GERMAN','BONJOUR':'FRENCH','CIAO':'ITALIAN','ZDRAVSTVUJTE':'RUSSIAN'}
cas =1
while True:
    st = input()
    if st=='#':
        break
    
    xx = dic.get(st,'NA')
    
    print('Case ',cas,': ',sep='',end='')
    cas+=1
    
    
    if xx == 'NA':
        print('UNKNOWN')
    else :
         print(xx)
     
