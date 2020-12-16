from tickets import read_data, get_valid_numbers

with open('input.txt') as file:
    tab = []
    for line in file:
        tab.append(line.strip())


def sum_invalid_numbers(nearby_tickets, valid_numbers):
    sum = 0
    for ticket in nearby_tickets:
        for value in ticket:
            if int(value) not in valid_numbers:
                sum += int(value)
    return sum


rules, my_ticket, nearby_tickets = read_data(tab)

valid_numbers = get_valid_numbers(rules)

print(sum_invalid_numbers(nearby_tickets, valid_numbers))
