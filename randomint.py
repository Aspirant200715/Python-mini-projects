#random library import 
import random as r

x = int(input("Enter the number of times you want to play the game : "))
m = int(input("Enter the range of number you want the system to guess numbers from(upperlimit) : "))
l = int(input("Enter the range of number you want the sysytem to guess numbers from(lowerlimit) : "))
count=0
if x>=5:
 for i in range(x):
   k = input("Enter a number : ")
   if not k.isdigit(): #checks if number is input or not
    print("Provide valid number pls!!!")
    continue
   f = r.randint(l,m+1)  #random integer guessing 
  
   if (int(k)==f):
     print("YOU WON!!!!!!")
     count+=1
   elif(int(k)<f):
     print("Think of a larger number.")
   elif(int(k)>f):
     print("Think of a smaller number")
   else:
     print("Pls add a number between range")
if count==5:
    print("You Did it finally")
else:
   print("minimum 5 moves")


