def numbers(input, turns):
    dictionary = {}
    turn = 1
    while turn <= turns:
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
                last_spoken = dictionary[last_spoken][1] - dictionary[last_spoken][0]
                try:
                    dictionary[last_spoken][0] = dictionary[last_spoken][1]
                    dictionary[last_spoken][1] = turn
                except IndexError:
                    dictionary[last_spoken].append(turn)
                except KeyError:
                    dictionary[last_spoken] = [turn]
            except KeyError:
                last_spoken = 0
                try:
                    dictionary[0] = [0]
                    dictionary[0][1] = turn
                except KeyError:
                    last_spoken = 0
            except IndexError:
                last_spoken = 0
                try:
                    dictionary[0][0] = dictionary[0][1]
                    dictionary[0][1] = turn
                except KeyError:
                    dictionary[0] = turn
                except IndexError:
                    dictionary[0].append(turn)
        turn += 1
    return last_spoken