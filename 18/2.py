with open('input.txt') as file:
    tab = []
    for line in file:
        tab.append(line.strip())


def prepare_string(string):
    listed = list(string)
    for i in range(len(listed) - 1, 0, -1):
        if listed[i] == '+':
            if listed[i - 1] not in '()' and listed[i + 1] not in '()':
                listed[i - 1] = str(int(listed[i - 1]) + int(listed[i + 1]))
                listed.pop(i)
                listed.pop(i)
    return listed


def add_first(string):
    # 6*9)*(15*14)+6)+6*2
    if string.index(')') < string.index('*'):
        output = 1
        operator = '*'
        for i in range(0, len(string)):
            if string[i] == ')':
                return output, i + 1
            else:
                try:
                    output = output * int(string[i]) if operator == '*' else output + int(string[i])
                except UnboundLocalError:
                    output = int(string[i])


def count(string):
    counter = 0
    listed = prepare_string(string)

    output = 1
    i = 0
    while i < len(listed):
        if '+' in listed:
            for j in range(len(listed) - 1, 0, -1):
                if listed[j] == '+':
                    if str(listed[j - 1]) not in '()' and str(listed[j + 1]) not in '()':
                        listed[j - 1] = str(int(listed[j - 1]) + int(listed[j + 1]))
                        listed.pop(j)
                        listed.pop(j)
        if '(' in listed:
            begin = ''
            end = ''
            p_counter = 0
            done = False
            for j in range(0, len(listed)):
                if not done:
                    if listed[j] == '(':
                        if begin:
                            p_counter += 1
                        else:
                            begin = j
                    elif listed[j] == ')':
                        if p_counter > 0:
                            p_counter += -1
                        else:
                            end = j
                    if begin != '' and end != '':
                        listed[begin] = count(listed[begin + 1:end])
                        for _ in range(begin, end):
                            listed.pop(begin+1)
                        begin = False
                        end = False
                        done = True

        else:
            for j in range(0, len(listed)):
                if listed[j] != '*':
                    output = output * int(listed[j])
            return output
        i += 1
    if '+' in listed:
        for j in range(len(listed) - 1, 0, -1):
            if listed[j] == '+':
                if str(listed[j - 1]) not in '()' and str(listed[j + 1]) not in '()':
                    listed[j - 1] = str(int(listed[j - 1]) + int(listed[j + 1]))
                    listed.pop(j)
                    listed.pop(j)
        output = int(listed[0])
    if '*' in listed:
        for j in range(len(listed) - 1, 0, -1):
            if listed[j] == '*':
                if str(listed[j - 1]) not in '()' and str(listed[j + 1]) not in '()':
                    listed[j - 1] = str(int(listed[j - 1]) * int(listed[j + 1]))
                    listed.pop(j)
                    listed.pop(j)
        output = int(listed[0])
    return output

sum = 0
for i in range(0, len(tab)):
    tab[i] = tab[i].replace(' ', '')
    sum += count(tab[i])
    if count(tab[i]) == 1:
        print(tab[i])
print(sum)


