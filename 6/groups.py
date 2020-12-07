def extract_groups(tab):
    groups = [[]]
    for line in tab:
        if line:
            groups[-1].append(line)
        else:
            groups.append([])

    return groups


def unique_correct_answers(group):
    answers = set()
    for person in group:
        for answer in person:
            answers.add(answer)
    return len(answers)


def correct_answers(group):
    answers = {}
    counter = 0
    for person in group:
        for answer in person:
            try:
                answers[answer] += 1
            except KeyError:
                answers[answer] = 1
    for key, value in answers.items():
        if value == len(group):
            counter += 1
    return counter