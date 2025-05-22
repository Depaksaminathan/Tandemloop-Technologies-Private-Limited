input=int(input())
if input==0:
    print("Invalid Number")
else:
    for i in range(input):
        print(2 * i + 1, end=", " if i < input - 1 else "\n")