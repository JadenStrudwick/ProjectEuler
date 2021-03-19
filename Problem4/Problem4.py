def palindrome_check(number):
    list = [int(x) for x in str(number)]
    reversed_list = list[::-1]

    if list == reversed_list:
        return True
    else:
        return False

palindromes = []

for i in range(100, 1000):
    for j in range(100, 1000):
        product = i*j
        if palindrome_check(product):
            palindromes.append(product)

print(max(palindromes))