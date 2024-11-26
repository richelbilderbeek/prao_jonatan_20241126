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
  times = []
  numbers = []

  for i in range(0, 10000):
      start = time.perf_counter()

      if(method1):
        is_prime(i)
      else:
         is_prime_2(i)

      end = time.perf_counter()
      elapsed = (end - start) * 1000 #Time in ms
      times.append(elapsed)
      numbers.append(i)

  plt.plot(numbers, times)
  plt.xlabel("X-axis")
  plt.ylabel("Y-axis")

  plt.show()

calculate_prime(True)
calculate_prime(False)



print("Done!")
#type: ignore