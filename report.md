# Report

## Goal

To get [a Big O speed profile](https://uppmax.github.io/programming_formalisms/optimisation/big_o)
to calculate if a number is prime:

```python
def is_prime(num):
    if num> 1:
        for n in range(2,num):
            if (num % n) == 0:
                return False
        return True
    else:
        return False
```

Output should show, per input value (i.e. the number to be
determined to be prime), how long it takes.

Here is an example, with runtime in nanoseconds:

```
input_value,runtime
1,0
2,1
3,1
4,1
5,2
6,1
7,3
8,1
9,2
10,1
11,4
12,1
13,5
14,1
15,3
```

A problem may be that the times get too low to be measured at the start:

```
input_value,runtime
1,0
2,0
3,0
4,0
5,0
6,0
7,0
8,0
9,0
10,0
11,0
12,0
13,0
14,0
15,0
```

This is not a problem: higher values will be non-zero.

Done? Then save this to a text file called `is_prime_1.csv` instead.

Done: then do the same for the function belowd, save to `is_prime_2.csv` instead:

```python
def is_prime_2(num):
  for n in range(
    2, int(num**0.5)+1
  ):
    if num%n==0:
      return False
  return True
```

Done: make a plot of these values :-)

Today I got to feel what it is like to work at BMC. I coded a program comparing the time to calculate prime numbers with two methods. I also got to know what Richel does for a living. He explained what people do at BMC and showed me around in the building.
