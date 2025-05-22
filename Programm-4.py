user_input = input("")

input_list = list(map(int, user_input.split(',')))
multiples_count = {}

for i in range(1, 10):
    count = 0
    for num in input_list:
        if num % i == 0:
            count += 1
    multiples_count[i] = count

print(multiples_count)