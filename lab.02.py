with open('input_2.txt') as file:
    sequences = [list(map(int, line.split())) for line in file]

counter = sum(
    all(a < b for a, b in zip(seq, seq[1:])) or all(a > b for a, b in zip(seq, seq[1:]))
    and all(1 <= abs(a - b) <= 3 for a, b in zip(seq, seq[1:]))
    for seq in sequences
)

print(counter)
