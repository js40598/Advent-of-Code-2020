with open('input.txt') as file:
    tab = []
    for line in file:
        tab.append(line.strip())


def count(string):
    counter = 0
    for i in range(0, len(string)):
        if counter <= 0:
            if string[i] in '+*':
                operator = string[i]
            elif string[i] == '(':
                parenthesis_output, counter = count(string[i + 1::])
                try:
                    if operator == '*':
                        output = output * parenthesis_output
                    else:
                        output += parenthesis_output
                except UnboundLocalError:
                    output = parenthesis_output
            elif string[i] == ')':
                return output, i+1
            else:
                try:
                    output = output * int(string[i]) if operator == '*' else output + int(string[i])
                except UnboundLocalError:
                    output = int(string[i])
        else:
            counter += -1
    return output, i+1

sum = 0
for i in range(0, len(tab)):
    tab[i] = tab[i].replace(' ', '')
    sum += count(tab[i])[0]
print(sum)


