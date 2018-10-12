import random

a={1:'r',2:'p',3:'s'}

while true
     p=input("your choise r/p/s: ")
     c=a[random.randint(1,3)]
     print(" you choise:",p,"computer chuses:",c,)

     if(p=='s' and c=='p'):
      	 print('i won!')
     elif(p=='r' and c=='s'):
         print('i won!')
     elif(p=='r' and c=='p'):
         print('i loose!')
     elif(p=='p' and c=='s'):
         print ('i loose!')
     elif(p=='s' and c=='r'):
         print('i loose!')
     elif(p=='p' and c=='r'):
         print('i won!')
     elif:
     	 print('draw!')