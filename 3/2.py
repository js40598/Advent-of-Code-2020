from count_trees import count_trees

with open('input.txt') as file:
    tab = []
    for line in file:
        tab.append(list(line.strip()))


slopes = [[1, 1],
          [1, 3],
          [1, 5],
          [1, 7],
          [2, 1]]

output = 1
for slope in slopes:
    output = output * count_trees(tab, slope)

print(output)
