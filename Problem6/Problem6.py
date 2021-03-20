def square_add(range):
    sum = 0
    for i in range:
        sum += i**2
    return sum

def add_square(range):
    return sum(range) ** 2

nat_num_range = [int(x) for x in range(1,101)]

print(add_square(nat_num_range) - square_add(nat_num_range))