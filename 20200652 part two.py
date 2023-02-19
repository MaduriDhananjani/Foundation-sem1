import math
#inputs

a=int(input("enter the Enter the coefficient of x**2 : "))
b=int(input("Enter the coefficient of x : "))
c=int(input("Enter the Enter the constant value :"))

#process

root = (b**2-4*a*c)

#output

if root>0:
   x_1 = int(((-b) + math.sqrt(root)) / (2 * a))
   x_2  = int(((-b) - math.sqrt(root)) / (2 * a))
   print('The roots of ','x**2', '+', b, 'x', '+', c, '= 0 are',x_2,'and',x_1)
   print("The discriminant is greater than zero -> There are two real distinct roots")
elif root==0:
     x_3 = int(((-b) / (2 * a)))
     print('The roots of ','x**2', '+', b, 'x', '+', c, '= 0 are',x_3,'and',x_3)
     print("The discriminant is zero -> There are two real identical roots")
elif root<0:
     print("The discriminant is less than zero -> There are no real roots")
     
 
