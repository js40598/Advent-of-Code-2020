from count_trees import count_trees

with open('input.txt') as file:
    tab = []
    for line in file:
        tab.append(list(line.strip()))


slope = [1, 3]

print(count_trees(tab, slope))
