def validate_password(password):
    c = 0
    password = password.split(' ')
    password[0] = password[0].split('-')
    password[1] = password[1][0]
    for letter in password[2]:
        if letter == password[1]:
            c += 1
    if int(password[0][0]) <= c <= int(password[0][1]):
        return True
    return False


with open('input.txt') as file:
    counter = 0
    for line in file:
        if validate_password(line.strip()):
            counter += 1


print(counter)
