#string is a collection two or more character 
'''
1. A String can be encolsed in single, double, thriple code
2. A string can be accessed using the index 
3. Index can be postive can be negative
4. A string can itreated using forloop 
'''
'''s="Sayed"
#print(type(s))
#print(s[-6])
s2="Sibgath"
s3=s+s2
print(s3)'''

#In reat two string from the user , print the string by combaning the last letter of both string. 
'''str1=input("enter the first string:-")
str2=input("enter the second string:-")
laststr1=str1[-1]
laststr2=str2[-1]
finalstring=laststr1+laststr2
print(finalstring)'''

#Accessing the a string character 
'''s1="Sayed Sibgath"
for i in s1:
    print(i)'''
    
#Count the number of vovel in your name 
'''s1="Sayed Sibgath"
count=0
for i in s1:
    if i=="a"or i=="e" or i=="i" or i=="o"or i=="u":
       count=count+1
print(count)'''

'''s1="Sayed Sibgath"
#length of a string 
length=len(s1)
#print(length)
count=0
for i in range(length):
    if s1[i]=="a" or s1[i]=="e" or s1[i]=="i" or s1[i]=="o" or s1[i]=="u":
        count=count+1
print(count)'''

# A string slicing 
'''s1="Sayed Sibgath"
slice1 =s1[5:9]
print (slice1)'''


# Write a programme to print first half of string 
s=input("enter the string:-")
length=len(s)
mid=int(length/2)
#print (mid)
sliceans=s[2:]
print(sliceans)

