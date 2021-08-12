n = int(input("Enter number of terms "))
n1, n2 = 0, 1
count = 0
odd=0
even=0
addition=[]
if n <= 0:
   print("Enter a valid number")
elif n==1:
    fibb=[n1]
    addition=[0]
else:
   print("Fibonacci sequence:")
   fibb=[n1,n2]
   addition=[0,4]
   while count < n-2:
       nth = n1 + n2
       n1 = n2
       n2 = nth
       count += 1
       fibb.append(nth)
       if (nth%2==0):
           even=even+1
           addition.append(nth+4)
        
       else:
           odd=odd+1
           addition.append(nth+3)
print(fibb)
print(fibb[::-1])
if(n==2):
    odd=1
print "Number of odd numbers:", odd
print "Number of even numbers:", even
print "After addition:" , addition
