
#for i in range(10,1,+1):
# for j in range(i+1):
  #  print('*', end =" ")
#print()
#for i in range(10):
 #for j in range(i+1):
  #print("*", end =" ")
 #print()

#for i in range(20):
  #for j in range(i+1):
    #print(j,end =" ")
  #print()

#for i in range(10,50):
 # for j in range(10,20):
    #if j<i:
       # print(i+1, end=" ")
    #else:
      #print(j+1,end=" ")
  #print()

for i in range(10):
 for j in range(10-i):
   print(" ",end =" ")
 for k in range (i+1):
     print("*", end= "   ")
 print()

word="python"
x=" "
for i in word:
    x+=i
    print(x)

rows=6
for i in range(0, rows):
 for j in range(rows-1,i,-1):
  print(j, '', end='')
 for l in range (i):
     print('    ',end='')
 for k in range(i + 1, rows):
  print(k,'',end='')
 print('\n')


rows = 6
for i in range(0, rows):
    for j in range(rows - 1, i, -1):
        print(j, '', end='')
    for l in range(i):
        print('    ', end='')
    for k in range(i + 1, rows):
        print(k, '', end='')
    print('\n')





