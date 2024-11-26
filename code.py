import time
#test

def isprime(num):
  for n in range(
    2, int(num**0.5)+1
  ):
    if num%n==0:
      return False
  return True

print("starting the calculation...")
print(" ")
z = 1
for x in range(0, 1000000):
    st = time.time()

    isprime(z)
    z += 1
    for n in range(
       2, int(z**0.5)+1
     ):
        if z%n==0:
          et = time.time()
          elapsed_time = round(et - st)
          print(z,   "time:", elapsed_time)
      
et = time.time()
elapsed_time = round(et - st)
print(z,   "time:", elapsed_time)


print(" ")
print("finished!")
