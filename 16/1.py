with open('input.txt') as file:
    tab = [[]]
    for line in file:
        if line.strip():
            tab[-1].append(line.strip())
        else:
            tab.append([])

rules = [line.split(': ') for line in tab[0]]
my_ticket = tab[1][1].split(',')
nearby_tickets = [ticket.split(',') for ticket in tab[2][1::]]

valid_numbers = set()
for i in range(0, len(rules)):
    rules[i][1] = rules[i][1].split(' or ')
    for r in rules[i][1]:
        interval = r.split('-')
        for j in range(int(interval[0]), int(interval[1])+1):
            valid_numbers.add(j)
print(len(valid_numbers))

sum = 0
for ticket in nearby_tickets:
    for value in ticket:
        if int(value) not in valid_numbers:
            sum += int(value)
print(sum)