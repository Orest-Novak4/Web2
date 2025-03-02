left, right = [], []

with open('input_1.txt', 'r') as file:
    for line in file:
        l, r = map(int, line.split())
        left.append(l)
        right.append(r)

total = sum(abs(l - r) for l, r in zip(sorted(left), sorted(right)))

print(total)
