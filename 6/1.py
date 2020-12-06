with open('input.txt') as file:
    groups = []
    init = True
    for line in file:
        if init:
            groups.append([line.strip()])
            init = False
        else:
            if not line.strip():
                groups.append([])
            else:
                groups[-1].append(line.strip())

counter = 0
for group in groups:
    group_answers = set()
    for person in group:
        for answer in person:
            group_answers.add(answer)
    counter += len(group_answers)

print(counter)
