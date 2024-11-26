import time
import csv

def is_prime(num):
    if num > 1:
        for n in range(2, num):
            if (num % n) == 0:
                return False
        return True
    else:
        return False

fields = ["Values"]
rows = []

for i in range(0, 100):
    # Measure time
    start = time.perf_counter()
    is_prime(i)
    end = time.perf_counter()
    elapsed = round((end - start) * 1000, 2)

    rows.append([str(elapsed)])

# Open file for writing
with open("is_prime_1.csv", "w", newline='') as csvfile:
    csv_writer = csv.writer(csvfile)
    csv_writer.writerow(fields)
    csv_writer.writerows(rows)

# Open file for reading and print its contents
with open("is_prime_1.csv", "r") as file:
    print(file.read())

print("Done!")
#type: ignore