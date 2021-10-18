#input and output in python
'''
1. input can be taken from console, excel file, txt file, csv file 
'''
'''#input from console 
a=int( input("enter the number"))#converting one data to another data is type casting 
#type of a 
#input function always give a string 
print (type (a))
 
 2. conditional statement in python 
 a. if 
 b. elif
 c. ifelse
 '''
 
 #looping statement
''' the statement which need to be executed multiple times
 1.While
 2.for
 '''
 
 
'''#Print the number which is greater than 10 from n1 to n2
a1=int(input("enter the value of a1"))
a2=int(input("enter the value of a2"))
 #logic 
while (a1<=a2):
     if(a1>10):
         print(a1)
     a1=a1+1
     '''
    
#Forloop
'''for anyvariable in range(20):
    print (anyvariable)
    '''
    
'''for i in range (4,10,2):  #range function always accept intereger, [lowwer limit, upper limit, skip] 
    print (i)
    '''
    
#print the value from n1 to n2 using forlopp 
n1=int(input("enter the value of N1"))
n2=int(input("enter the value of N2"))
for  i in range(n1,n2):
    print(i)
    