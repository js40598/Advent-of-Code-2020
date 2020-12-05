with open('input.txt') as file:
    tab = []
    for line in file:
        tab.append(line.strip())
highest_id = 0
for t in tab:
    rows = [i for i in range(0, 128)]
    columns = [i for i in range(0, 8)]
    searching_rows = rows[::]
    searching_columns = columns[::]
    for char in t[0:7]:
        if char == 'F':
            searching_rows = searching_rows[0:int(len(searching_rows)/2)]
        elif char == 'B':
            searching_rows = searching_rows[int(len(searching_rows)/2)::]

    for char in t[7::]:
        if char == 'L':
            searching_columns = searching_columns[0:int(len(searching_columns)/2)]
        elif char == 'R':
            searching_columns = searching_columns[int(len(searching_columns)/2)::]

    id = int(searching_rows[0]) * 8 + int(searching_columns[0])
    if id > highest_id:
        highest_id = id
print(highest_id)
