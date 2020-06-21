# 321810304042-python_assignment_3

#Bhavyasree N - 321810304042

# # ###   1.  Take two inputs from user and check whether they are equal or not ?

  #  METHOD_1 :
  	
a  =  10
b  =  10
print(a==b)

   #  METHOD_2 :
   	
a  =  10
print(a)
b  =  12
print(b)
print(a==b)

   #  METHOD_3 :
   	
print("Enter first number")
first  =  input()
print("Enter second number")
second  =  input()
print(first==second)

  #  METHOD_4 :
  	
str1  =  str(input(" Enter the first string : "))
str2  =  str(input(" Enter the second string : "))
if   str1 ==  str2 :
	  print(" Yes , both strings are equal ")
else : 
      print(" No, both strings are not equal ")





# # ###   2.  Take 3 inputs from user and check:
	
	###  all are equal (use and) :
		
   # METHOD_1 :
	
a  =  10
b  =  10
c  =  10
z  =  a == b and b == c and c == a
print("All are equal",z)	

   # METHOD_2 :
   	
print("first number")
first  =  input()
print("second number")
second  =  input()
print("third number")
third  =  input()
all  =  first == second and second == third and third == first
print("All are Equal",all)

    ###   any of two are equal (use or) :
    	
     # METHOD_1 :

a  =  10
b  =  12
c  =  10
z  =  a == b or b == c or c == a
print("Any of two are equal",z)

     # METHOD_2 :
     	
print("first number")
first  =  input()
print("second number")
second  =  input()
print("third number")
third  =  input()
any  =  first == second or second == third or third == first
print("Any of two are equal",any)

   ### Using both   'and'   and also   'or'   :
   	
str1  =  str(input(" Enter first string : "))
str2  =  str(input(" Enter second string : "))
str3  =  str(input(" Enter third string : "))
if ( str1 == str2 == str3 ) :
	print(" All strings are equal ")
elif ( str1 == str2  and ( str1 != str3  or  str2 != str3 )) :
	print(" First and Second Strings are equal ")
elif ( str1 == str3  and ( str1 != str2  or  str3 != str2 )) :
	print(" First and Third Strings are equal " )
elif ( str2 == str3  and ( str2 != str1  or  str3 != str1 )) :
	print(" Second and Third Strings are equal " )
else :
	print(" All strings are not equal ")	





# # ###    3.    Take two numbers and check whether the sum is greater than 5 , less than 5 or equal to 5 ?

 # METHOD_1 :
 	
a  =  10
b  =  5
c  =  a + b
print(c)
print(" c > 5 : ", c > 5)
print(" c == 5 : ", c == 5)
print(" c < 5 : ", c < 5)

 # METHOD_2 :

print("Enter first number")
first  =  int(input())
print("Enter second number")
second  =  int(input())
sum  =  first + second
print(sum)
print(" sum > 5 : ", sum > 5)
print(" sum == 5 : ", sum == 5)
print(" sum < 5 : ", sum < 5)

  # METHOD_3 :
  	
a =  int(input(" Enter first number : "))
b =  int(input(" Enter second number : ")) 
sum = a + b 
if sum > 5 :
   	print(" sum is greater than 5 ")
elif  sum < 5 :
   	print(" sum is less than 5 ")
else :
   	print(" sum is equal to 5 ")	





# # ###     4.     Suppose passing marks of a subject is 35.Take input of marks from user and check whether it is greater than passing marks or not ?

marks = float(input(" Enter marks of student "))
if marks  >=  35 :
	     print(" student has passed in the subject ")
else :
	     print(" student has failed in the subject ")





# # ###     5.     Write a python function to find the maximum of three numbers.

 # METHOD_1 :
 	
a =  int(input(" Enter first number : "))
b =  int(input(" Enter second number : "))
c  =  int(input(" Enter third number : "))
if a == b == c  :	
      print("All are equal...no maximum number ")
if ( a > b and a > c) :
      print(" Maximum number is : ",a)
elif ( b > c and b > a ) :
      print(" Maximum number is : ",b)
else :
      print(" Maximum number is :",c)
      
 # METHOD_2 :	
 
def maximum( a , b ,c ) :
	if a  >  b and a  >  c :
		print("maximum number = ",a)
	elif b  >  a and b  >  c :
		print("maximum number= ",b)
	elif a  ==  b:
		print(" a  ==  b ")
	elif a  ==  c:
		print(" a  ==  c ")
	elif b  ==  c:
		print(" b  ==  c")
	else:
		print("maximum number = ", c)
maximum( 10 , 20 , 30)






