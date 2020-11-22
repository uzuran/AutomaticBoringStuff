while True:
    print('Who are you?')
    name = input()
    if name != 'Artom':
        continue
    print('Hello ' + name + ' What is the password?')
    password = input()
    if password == 'swordfish':
        print('Thank you ' + name + ' Password is correct!')
        break
    else:
        print("Passwor is wrong!")
        continue