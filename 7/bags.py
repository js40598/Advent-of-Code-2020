def extract_rules(tab):
    rules = {}
    for rule in tab:
        r = rule.split(' contain ')
        contains = [[c.split(' ')[0:-1][0], ' '.join(c.split(' ')[0:-1][1::])] for c in r[1].split(', ')]
        rules[' '.join(r[0].split(' ')[0:-1])] = contains
    return rules


def count_bags_containing(pattern, rules):
    output = set()
    for key, values in rules.items():
        for value in values:
            if pattern == value[1]:
                output.add(key)
                rec = count_bags_containing(key, rules)
                if rec:
                    for r in rec:
                        output.add(r)
    if len(output) > 0:
        return output
    else:
        return False
