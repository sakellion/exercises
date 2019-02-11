import random
x= input('Put rows ')
y = input('Put columns ')
m = input('Put number of mines ')
while m >= x*y:
  m = input('Put number of mines ')
#for i in range(x):
#        print('x '*y)
a=[["1" for i in range(x)]  for j in range(y)]
listofnumbers1=[]
listofnumbers2=[]
#for i in range(0, x):
    #for j in range (0, y):
        #a.append(["1"] )
for i in range (m):
       listofnumbers1.append(random.randint(0, x-1))
       listofnumbers2.append(random.randint(0, y-1))

for j in range (m):
    a[listofnumbers1[j]][listofnumbers2[j]]="0"

for t in range(len(a)):
    print(a[t])
