# last 5 digits of fibonacci number with reccursive
def Last5ofFibRec(n):
  if n==0:
    return n
  elif n==1:
    return n
  else:
    return (Last5ofFibRec(n-1)+Last5ofFibRec(n-2))%100000  
print(Last5ofFibRec(40))   
