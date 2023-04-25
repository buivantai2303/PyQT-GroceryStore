def read_polynomial():
    degree = int(input("Enter the degree of polynomial: "))
    poly = []
    for i in range(degree + 1):
        coef = int(input("Enter the coefficient of x^" + str(i) + ": "))
        poly.append(coef)
    return poly


def print_polynomial(poly):
    degree = len(poly) - 1
    poly_str = ""
    for i in range(degree + 1):
        if poly[i] != 0:
            if i == 0:
                poly_str += str(poly[i])
            elif i == 1:
                poly_str += str(poly[i]) + "x"
            else:
                poly_str += str(poly[i]) + "x^" + str(i)
            if i < degree:
                poly_str += " + "
    print(poly_str)


def evaluate_polynomial(poly, x):
    degree = len(poly) - 1
    value = 0
    for i in range(degree + 1):
        value += poly[i] * (x ** i)
    return value


def add_polynomials(poly1, poly2):
    degree1 = len(poly1) - 1
    degree2 = len(poly2) - 1
    if degree1 < degree2:
        poly1, poly2 = poly2, poly1
        degree1, degree2 = degree2, degree1
    result_poly = poly1.copy()
    for i in range(degree2 + 1):
        result_poly[i] += poly2[i]
    return result_poly


def subtract_polynomials(poly1, poly2):
    degree1 = len(poly1) - 1
    degree2 = len(poly2) - 1
    if degree1 < degree2:
        poly1, poly2 = poly2, poly1
        degree1, degree2 = degree2, degree1
    result_poly = poly1.copy()
    for i in range(degree2 + 1):
        result_poly[i] -= poly2[i]
    return result_poly


def multiply_polynomials(poly1, poly2):
    degree1 = len(poly1) - 1
    degree2 = len(poly2) - 1
    result_degree = degree1 + degree2
    result_poly = [0] * (result_degree + 1)
    for i in range(degree1 + 1):
        for j in range(degree2 + 1):
            result_poly[i + j] += poly1[i] * poly2[j]
    return result_poly


def display():
    poly1 = read_polynomial()
    print("First polynomial is:")
    print_polynomial(poly1)

    poly2 = read_polynomial()
    print("Second polynomial is:")
    print_polynomial(poly2)

    print("Sum of the polynomials is:")
    result_sum = add_polynomials(poly1, poly2)
    print_polynomial(result_sum)

    print("Difference of the polynomials is:")
    result_diff = subtract_polynomials(poly1, poly2)
    print_polynomial(result_diff)

    x = int(input("Enter the value of x to evaluate the polynomials: "))

    print("First polynomial evaluated at x is:")
    result_eval1 = evaluate_polynomial(poly1, x)
    print(result_eval1)

    print("Second polynomial evaluated at x is:")
    result_eval2 = evaluate_polynomial(poly2, x)
    print(result_eval2)

    print("Product of the polynomials is:")
    result_product = multiply_polynomials(poly1, poly2)
    print_polynomial(result_product)


display()
