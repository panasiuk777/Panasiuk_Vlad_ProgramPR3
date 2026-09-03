name = "Vlad"
surname = "Panasiuk"
group = "IT31"
d = 27
c = 8

print(f"{name} {surname}, {group}")

n = d * c

print(f"n = {d} * {c} = {n}")

# Divisors
divisors = []
divisor_sum = 0

for i in range(1, n + 1):
    if n % i == 0:
        divisors.append(i)
        divisor_sum += i

print("Divisors:", *divisors)
print(f"Divisors count: {len(divisors)}, sum: {divisor_sum}")

# Check if n is prime
if n < 2:
    print(f"{n} is not prime")
else:
    for i in range(2, n):
        if n % i == 0:
            print(f"{n} is not prime")
            break
    else:
        print(f"{n} is prime")

# Prime numbers from 2 to n
primes = []

for number in range(2, n + 1):
    for i in range(2, number):
        if number % i == 0:
            break
    else:
        primes.append(number)

print("Primes up to n:", *primes)
print(f"Primes count: {len(primes)}")