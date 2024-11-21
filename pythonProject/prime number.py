num=int(input("enter the number"))
if num>1:
 for i in range (2,(num//2)+1):
     if (num % i)==0:

         break
     else:
         print(num, "is not a prime number")
 else:
     print("prime number")

