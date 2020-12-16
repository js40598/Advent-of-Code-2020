from tickets import read_data, get_valid_numbers

with open('input.txt') as file:
    tab = []
    for line in file:
        tab.append(line.strip())


def delete_invalid_tickets(valid_numbers, nearby_tickets):
    invalid_indexes = []
    for i in range(0, len(nearby_tickets)):
        for j in range(0, len(nearby_tickets[i])):
            if int(nearby_tickets[i][j]) not in valid_numbers:
                invalid_indexes.append(i)
    for index in invalid_indexes[::-1]:
        nearby_tickets.pop(index)
    return nearby_tickets


def get_possible_rules(rules, nearby_tickets):
    output_possible_rules = []
    for i in range(0, len(rules)):
        possible_rules = [key for key, value in rules.items()]
        for j in range(0, len(nearby_tickets)):
            new_possible_rules = []
            for rule in possible_rules:
                if rules[rule][0] <= nearby_tickets[j][i] <= rules[rule][1]:
                    new_possible_rules.append(rule)
                elif rules[rule][2] <= nearby_tickets[j][i] <= rules[rule][3]:
                    new_possible_rules.append(rule)
            possible_rules = new_possible_rules
        output_possible_rules.append([i, possible_rules])
    return output_possible_rules


def rule_indexes(possible_rules):
    assigned = []
    output_dictionary = {}
    for o in possible_rules:
        for rule in o[1]:
            if rule not in assigned:
                assigned.append(rule)
                output_dictionary[rule] = o[0]
    return output_dictionary


def multiply_departure_values(output_dictionary):
    multiplied = 1
    for key, value in output_dictionary.items():
        if key.split(' ')[0] == 'departure':
            multiplied = multiplied * int(my_ticket[value])
    return multiplied


rules, my_ticket, nearby_tickets = read_data(tab)
my_ticket = my_ticket[0]

valid_numbers = get_valid_numbers(rules)

nearby_tickets = delete_invalid_tickets(valid_numbers, nearby_tickets)

possible_rules = sorted(get_possible_rules(rules, nearby_tickets), key=lambda l: len(l[1]))

output_dictionary = rule_indexes(possible_rules)

print(multiply_departure_values(output_dictionary))
