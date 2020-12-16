def format_rules(rules):
    output = {}
    for rule in rules:
        r = rule.split(': ')
        values = r[1].split(' or ')
        output[r[0]] = []
        for value in values:
            for v in value.split('-'):
                output[r[0]].append(int(v))
    return output


def format_ticket(ticket):
    output = []
    for value in ticket.split(','):
        output.append(int(value))
    return output


def format_tickets(tickets):
    output = []
    for ticket in tickets:
        output.append(format_ticket(ticket))
    return output


def read_data(tab):
    data = [[]]
    for line in tab:
        if line:
            data[-1].append(line)
        else:
            data.append([])
    rules = format_rules(data[0])
    my_ticket = format_tickets(data[1][1::])
    nearby_tickets = format_tickets(data[2][1::])
    return rules, my_ticket, nearby_tickets


def get_valid_numbers(rules):
    valid_numbers = set()
    for key, value in rules.items():
        for i in range(rules[key][0], rules[key][1]+1):
            valid_numbers.add(i)
        for i in range(rules[key][2], rules[key][3]+1):
            valid_numbers.add(i)
    return valid_numbers