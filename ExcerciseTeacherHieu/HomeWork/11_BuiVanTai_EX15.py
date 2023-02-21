even_numbers = lambda lst: list(filter(lambda x: x % 2 == 0, lst))

input_lst = list(map(int, input("Enter a list of numbers: ").split()))
output_lst = even_numbers(input_lst)
print(output_lst)
