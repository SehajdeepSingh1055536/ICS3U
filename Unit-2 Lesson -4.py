import math
def factorial (n):
  result = 1
  for i in range(1, n+1):
    result = result * i
    
  return result
  
  
n = int(input("Enter a value for the upper limit, n:"))

print("factorial calculator:")
for i in range(n+1):
  print (f"{i}!= {factorial(i)}")
