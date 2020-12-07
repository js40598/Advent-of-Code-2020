from bags import extract_rules, count_bags_containing

with open('input.txt') as file:
    tab = []
    for line in file:
        tab.append(line.strip())


rules = extract_rules(tab)
print(rules['light fuchsia'])
print(len(count_bags_containing('shiny gold', rules)))
