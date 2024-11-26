import time
import csv
import matplotlib.pyplot as plt

def is_prime(num):
    if num > 1:
        for n in range(2, num):
            if (num % n) == 0:
                return False
        return True
    else:
        return False
    
def is_prime_2(num):
  for n in range(
    2, int(num**0.5)+1
  ):
    if num%n==0:
      return False
  return True

def calculate_prime(method1):
  values = []
  
  for i in range(0, 10000):
      start = time.perf_counter()

      if(method1):
        is_prime(i)
      else:
         is_prime_2(i)

      end = time.perf_counter()
      elapsed = (end - start) * 1000 #Time in ms
      values.append(elapsed)

  plt.plot(list(range(0, 10000)), values)
  plt.xlabel("Numbers")
  plt.ylabel("Time(in ms)")
  if(method1):
     plt.title("Method 1")
  else:
     plt.title("Method 2")

  plt.show()

calculate_prime(True)
calculate_prime(False)

#type: ignore