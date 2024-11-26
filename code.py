from timeit import default_timer as timer
from datetime import timedelta
import timeit
import time

def is_prime(num):
    if num> 1:
        for n in range(2,num):
            if (num % n) == 0:
                return False
        return True
    else:
        return False
    

for i in range(0, 100000):
    start = time.perf_counter()
    is_prime(i)
    end = time.perf_counter()
    print(end - start)

# type: ignore