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

invalid_indexes = []
for i in range(0, len(nearby_tickets)):
    for j in range(0, len(nearby_tickets[i])):
        if int(nearby_tickets[i][j]) not in valid_numbers:
            invalid_indexes.append(i)

print(len(nearby_tickets))
for index in invalid_indexes[::-1]:
    nearby_tickets.pop(index)

print(len(nearby_tickets))

dictionary = {}
print(rules)
for rule in rules:
    intervals = [rule[1][0].split('-'), rule[1][1].split('-')]
    s = set()
    for r in rule[1]:
        interval = r.split('-')
        for j in range(int(interval[0]), int(interval[1]) + 1):
            s.add(j)
    dictionary[rule[0]] = s
print(dictionary)

possible_rules_dict = {}
for i in range(0, len(rules)):
    possible_rules = [key for key, value in dictionary.items()]
    for j in range(0, len(nearby_tickets)):
        new_possible_rules = []
        for possible_rule in possible_rules:
            if int(nearby_tickets[j][i]) in dictionary[possible_rule]:
                new_possible_rules.append(possible_rule)
        possible_rules = new_possible_rules
    print(possible_rules)
    possible_rules_dict[i] = possible_rules

print(possible_rules_dict)
output = {}
outputs = []
for i in range(1, len(rules)):
    for key, value in possible_rules_dict.items():
        if len(possible_rules_dict[key]) == i:
            for possible_rule in possible_rules_dict[key]:
                if possible_rule not in outputs:
                    output[key] = possible_rule
                    outputs.append(possible_rule)
            del_key = key
    del possible_rules_dict[del_key]
print(possible_rules_dict)
print(output)

multiplied = 1
for key, value in output.items():
    if value.split(' ')[0] == 'departure':
        multiplied = multiplied * int(my_ticket[key])
print(multiplied)