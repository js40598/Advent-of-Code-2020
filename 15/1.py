input = [2,0,1,7,4,14,18]

dictionary = {}
turn = 1
while turn <= 2020:
    if turn <= len(input):
        try:
            if len(dictionary[input[turn-1]]) == 2:
                dictionary[input[turn-1]].pop(0)
                dictionary[input[turn-1]].append(turn)
            elif len(dictionary[input[turn-1]]) == 1:
                dictionary[input[turn-1]].append(turn)
        except KeyError:
            dictionary[input[turn-1]] = [turn]
        last_spoken = input[turn-1]
    else:
        try:
            if len(dictionary[last_spoken]) == 2:
                last_spoken = dictionary[last_spoken][1] - dictionary[last_spoken][0]
                try:
                    if len(dictionary[last_spoken]) == 2:
                        dictionary[last_spoken].pop(0)
                        dictionary[last_spoken].append(turn)
                    elif len(dictionary[last_spoken]) == 1:
                        dictionary[last_spoken].append(turn)
                except KeyError:
                    dictionary[last_spoken] = [turn]
            elif len(dictionary[last_spoken]) == 1:
                last_spoken = 0
                try:
                    if len(dictionary[last_spoken]) == 2:
                        dictionary[last_spoken].pop(0)
                        dictionary[last_spoken].append(turn)
                    elif len(dictionary[last_spoken]) == 1:
                        dictionary[last_spoken].append(turn)
                except KeyError:
                    dictionary[last_spoken] = [turn]
        except KeyError:
            dictionary[last_spoken] = [turn]
            last_spoken = 0
    print(last_spoken)
    turn += 1

print(last_spoken)
