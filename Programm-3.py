a = int(input("Enter a number: "))

if a % 2 == 0:
    count = a - 1
else:
    count = a

odd_numbers = []
for i in range(count):
    odd_numbers.append(str(2 * i + 1))

print(", ".join(odd_numbers))
