while True:
    n = int(input("Size: "))
    if n >= 1 and n <= 8:
        break

for i in range(n):
    for j in range(n - i - 1):
        print(" ", end="")
    for j in range(i + 1):
        print("#", end="")
    print()
