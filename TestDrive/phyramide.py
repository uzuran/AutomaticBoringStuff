height = int(input('Enter number of height pyramid :'))

if height == 0:
    print('Please enter integer more then zero ')
elif height == 1:
    print('A')
else:
    x = 0
    z = height
    for i in range(height):
        x = x + 2
        z = z - 1
        print(z * str(' '), x * str('A'))
