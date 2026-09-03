name = "Vlad"
surname = "Panasiuk"
group = "IT31"
d = 27
c = 8

print(f"{name} {surname}, {group}")

# for version
count = 0
total = 0
product = 1
even = 0
odd = 0

print(f"Numbers from {d} to 31:", end=" ")

for i in range(d, 32):
    print(i, end=" ")
    count += 1
    total += i
    product *= i

    if i % 2 == 0:
        even += 1
    else:
        odd += 1

average = total / count

print()
print(f"Count: {count}")
print(f"Sum: {total}")
print(f"Product: {product}")
print(f"Average: {average:.2f}")
print(f"Even: {even}, odd: {odd}")

# while version
count = 0
total = 0
product = 1
even = 0
odd = 0
i = d

while i <= 31:
    count += 1
    total += i
    product *= i

    if i % 2 == 0:
        even += 1
    else:
        odd += 1

    i += 1

average = total / count

print()
print("# while version")
print(f"Count: {count}")
print(f"Sum: {total}")
print(f"Product: {product}")
print(f"Average: {average:.2f}")
print(f"Even: {even}, odd: {odd}")

# Countdown
print("Countdown:", end=" ")

for i in range(c, 0, -1):
    print(i, end=" ")

print()