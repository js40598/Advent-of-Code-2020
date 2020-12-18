with open('input.txt') as file:
    tab = []
    for line in file:
        tab.append(line.strip())


def extract_parentheses(string):
    inside_parentheses = 0
    current_parentheses = [[]]
    for char in string:
        if char not in '()':
            current_parentheses[-1].append(char)
        elif char == '(':
            if inside_parentheses == 0:
                current_parentheses.append([])
            else:
                current_parentheses[-1].append(char)
            inside_parentheses += 1
        elif char == ')':
            if inside_parentheses == 1:
                current_parentheses.append([])
            else:
                current_parentheses[-1].append(char)
            inside_parentheses += -1
    for i in range(0, len(current_parentheses)):
        current_parentheses[i] = ''.join(current_parentheses[i])
    for i in range(0, len(current_parentheses)):
        if '(' in current_parentheses[i]:
            current_parentheses[i] = extract_parentheses(current_parentheses[i])
    return current_parentheses


def multiply_parentheses(parentheses):
    to_pop = []
    for i in range(0, len(parentheses)):
        if type(parentheses[i]) == list:
            for j in range(len(parentheses[i])-1, -1, -1):
                if parentheses[i][j] == '':
                    parentheses[i].pop(j)
            parentheses[i] = multiply_parentheses(parentheses[i])
        elif type(parentheses[i]) == str:
            if parentheses[i] == '*':
                pass
            else:
                if parentheses[i] not in [[''], '']:
                    if parentheses[i][0] == '+':
                        parentheses[i] = parentheses[i][1::]
                    multiplies = parentheses[i].split('+')
                    for j in range(0, len(multiplies)):
                        if multiplies != ['']:
                            m = 1
                            for number in multiplies[j].split('*'):
                                if number:
                                    m = m * int(number)
                            multiplies[j] = m
                        else:
                            to_pop.append(i)
                    parentheses[i] = multiplies
                else:
                    to_pop.append(i)
    for tp in to_pop[::-1]:
        parentheses.pop(tp)
    return parentheses


def sum_parentheses(parentheses):
    print(parentheses)
    sums = []
    for i in range(len(parentheses)):
        print(parentheses[i])
        if type(parentheses[i]) == int:
            sums.append(parentheses[i])
        elif '*' in parentheses[i]:
            m_index = parentheses[i].index('*')
            s = sum_parentheses(parentheses[i][m_index-1])
            s = s * sum_parentheses(parentheses[i][m_index+1])
            parentheses[i].pop(m_index+1)
            parentheses[i].pop(m_index)
            parentheses[i][m_index-1] = s
            print(parentheses[i], 'iii')
            sums.append(sum_parentheses(parentheses[i]))
        else:
            try:
                sums.append(sum(parentheses[i]))
            except:
                sums.append(sum_parentheses(parentheses[i]))
    print('sums: ', sums)
    return sum(sums)



for i in range(0, len(tab)):
    tab[i] = tab[i].replace(' ', '')

parentheses = []
for i in range(0, len(tab)):
    if '(' in tab[i]:
        parentheses.append(extract_parentheses(tab[i]))


for i in range(0, len(parentheses)):
    parentheses[i] = multiply_parentheses(parentheses[i])

for i in range(0, len(parentheses)):
    parentheses[i] = sum_parentheses(parentheses[i])

print(parentheses)

