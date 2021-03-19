fibonacci_sequence = [1, 2, 3]

last_term = fibonacci_sequence[len(fibonacci_sequence) - 1]
pen_term = fibonacci_sequence[len(fibonacci_sequence) - 2]
new_term = last_term + pen_term

while new_term < 4000000:
    last_term = fibonacci_sequence[len(fibonacci_sequence) - 1]
    pen_term = fibonacci_sequence[len(fibonacci_sequence) - 2]
    new_term = last_term + pen_term

    if new_term > 4000000:
        break
    fibonacci_sequence.append(new_term)

even_fibonacci_sequence = []

for term in fibonacci_sequence:
    if term % 2 == 0:
        even_fibonacci_sequence.append(term)

print(even_fibonacci_sequence)
print(sum(even_fibonacci_sequence))