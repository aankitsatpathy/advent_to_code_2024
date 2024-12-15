def parse_file(file_path):
    with open(file_path, 'r') as file:
        lines = file.readlines()
    x = []
    y = []

    for line in lines:
        x1, y2 = line.split()
        x.append(int(x1))
        y.append(int(y2))
    return x, y

file_path = 'input_advent_d1p1.txt'
x, y = parse_file(file_path)

x.sort()
y.sort()

s = 0
for i in x:
    s += (i * y.count(i))

print(s)
# print(x)
# print(y)
