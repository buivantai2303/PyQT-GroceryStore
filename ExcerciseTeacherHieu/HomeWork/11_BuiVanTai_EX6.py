n = int(input("Enter a natural number: "))

fib1, fib2 = 0, 1

print(fib1, fib2, end=" ")

for i in range(2, n):
    fib_next = fib1 + fib2
    print(fib_next, end=" ")
    fib1, fib2 = fib2, fib_next
