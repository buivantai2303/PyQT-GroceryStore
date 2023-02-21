#
#
# if __name__ == '__main__':
#     Value = input("Enter your value: ")
#     if Value == Value[::-1]:
#         print("The entered Strrr is symmetrical")
#     else:
#         print("The entered Strrr is not symmetrical")
#     if Value == Value[::-1]:
#         print("The entered Strrr is palindrome")
#     else:
#         print("The entered Strrr is not palindrome")


def check_symmetry_palindrome(Strrr):
    length = len(Strrr)

    if length % 2 != 0:
        return "The entered Strrr is not symmetrical and palindrome"

    half_length = length // 2
    first_half = Strrr[:half_length]
    second_half = Strrr[half_length:]

    if first_half == second_half:
        if first_half == second_half[::-1]:
            return "The entered Strrr is symmetrical and palindrome"
        else:
            return "The entered Strrr is symmetrical but not palindrome"
    else:
        return "The entered Strrr is not symmetrical and palindrome"


Strrr = input("Enter your Strrr: ")
print(check_symmetry_palindrome(Strrr))