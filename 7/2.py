from bags import extract_rules

with open('input.txt') as file:
    tab = []
    for line in file:
        tab.append(line.strip())


def count_required_bags(pattern, rules):
    output = 0
    try:
        rule = rules[pattern]
    except KeyError:
        return 1

    for value in rule:
        print(value)
        try:
            output += int(value[0])
            rec = count_required_bags(value[1], rules)
            output += rec * int(value[0])
        except ValueError:
            output += 0

    return output


rules = extract_rules(tab)
print(count_required_bags('shiny gold', rules))

