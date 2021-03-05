name = ''
while not name:
    print('Enter your name.')
    name = input()
print('How many guests will you have?')
numOfGuests = int(input())
if numOfGuests:
    print('Be shure to have enough room for your guests.')
print('Done')