#Function - Function is a group of instruction executed to perform particular task. 
'''
1. Function must be defined with key word def
2. Function won't execute automatically
3. We need to call the function
4. We can pass the valaue form the function
5. Variable can be accessed only inside the function(Global variavle)
6. Funtion return the value (it is Optional)
'''

''''def Addtwonumber(): #won't execute
    
    a=int(input("Enter first number:- "))
    b=int(input("Enter Second number:- "))
    c=a+b
    print(c)
Addtwonumber()  #calling function'''
def add(p,q):
    c=p+q
    #Return the results
    return c
    
a=int(input("Enter first number:- "))
b=int(input("Enter Second number:- "))
results=add(a,b)
print(results)















