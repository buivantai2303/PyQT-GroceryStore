import math

if __name__ == '__main__':
    # a, b, c = int(input("Enter a, b, c: ")).split(",")
    a = int(input("Enter a: "))
    b = int(input("Enter b: "))
    c = int(input("Enter c: "))

    delta = (b * b - 4 * a * c)

    if delta > 0:
        print("Because delta > 0:")
        print("- x1 =", (b * (-1) + math.sqrt(delta)) / (2 * a))
        print("- x2 =", (b * (-1) - math.sqrt(delta)) / (2 * a))
    if delta < 0:
        print("- The equation has no solution because delta < 0")
    if delta == 0:
        print("Delta = 0, we have: ")
        print("- x1 = x2 = ", (b * -1) / (2 * a))
