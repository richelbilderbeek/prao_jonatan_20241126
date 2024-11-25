# Report

## Goal

To get [a Big O speed profile](https://uppmax.github.io/programming_formalisms/optimisation/big_o)
of two ways to calculate if a number
is prime. 

Use these two function:

```
def is_prime_1(num):
  for n in range(
    2, int(num**0.5)+1
  ):
    if num%n==0:
      return False
  return True

def is_prime_2(num):
    if num> 1:
        for n in range(2,num):
            if (num % n) == 0:
                return False
        return True
    else:
        return False
```

Expected output:

Function|Value|Is prime?|Time to determine this
--------|-----|---------|----------------------
1       |2    |Y        |
