birthdays = {'Jirka': 'April 1', 'Bob': 'October 7', 'Carol': 'June 25'}

while True:
    print('Enter a name: (blank to quit)')
    name = input()
    if name == '':
        break

    if name in birthdays:
        print(birthdays[name] + ' is the birthday of ' + name)
    else:
        print('I do not have birthday information  for ' + name)
        print('What is their birthday?')
        birth_Day = input()
        birthdays[name] = birth_Day
        print('Birthday database update!')
