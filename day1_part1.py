def parse_file(file_path):
    with open(file_path, 'r') as file:
        lines = file.readlines()
    x = []
    y = []

    for line in lines:
        x1, y2 = line.split()
        x.append(x1)
        y.append(y2)
    return x, y

file_path = 'input_advent_d1p1.txt'
x, y = parse_file(file_path)
x.sort()
y.sort()


distance = 0
for i in range(len(x)):
    a = int(x[i])
    b = int(y[i])
    distance += abs(b - a)
print(distance)
