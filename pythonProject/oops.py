class Dog:
    # class attribute
    attr1="mammal"

    # Instance attribute
    def __init__(self, name):
        self.name = name

    def speak(self):
        print("My name is {}".format(self.name))


# Driver code
# Object instantiation
Rodger = Dog("Rodger")
Tommy = Dog("Tommy")

# Accessing class methods
Rodger.speak()
Tommy.speak()




#rows = int(input("Enter the number of rows: "))
#k = 2 * rows - 2
# for i in range(0, rows):
    # for j in range(0, k):
    #     print(end=" ")
 # k = k - 1
#     for j in range(0, i + 1):
#         print("* ", end="")
#     print("")
#k = rows - 2
#for i in range(rows, -1, -1):
     # for j in range(k, 0, -1):
    #     print(end=" ")
   # k = k + 1
  # for j in range(0, i + 1):
    #     print("* ", end="")
    # print("")



# rows=int(input("enter the number of rows"))
# k=2 * rows - 2
# for i in range (0,rows):
#     for j in range(0,k):
#         print(end="")
#     k=k-1
#     for j in range(0,i+1):
#         print("*",end="")
#     print("")
#     k=k-2
# for i in range(rows,-1,-1):
#     for j in range(k,0,-1):
#         print (end="")
#     k=k+1
#     for j in range(0,i+1):
#         print("*",end="")
#     print("")



# rows=10
# k= rows - 2
# for i in range(rows,-1,-1):
#   for j in range(k,0,-1):
#     print(end=" ")
#     k=k+1
# for j in range(0,i+1):
#     print("*",end="")
# print()
# k = k+1
# for j in range(0,i+1):
#   print("*",end="")
#   print()
# k= 2* rows  -2
# for i in range(0,k):
#   print(end="")
# k=k
# for j in range(0,i+1):
#     print("*",end="")
# print()


str1 = "12345678"   # here, we are declaring the string variable to store the string
x = ""
for i in str1:     # here, we are declaring the for loop to iterate through str1
    x += i     # here, we are incrementing the x value with the I value after each iteration
    print(x)
