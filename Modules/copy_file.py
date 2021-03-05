import copy

spam = ['A', 'B', 'C', 'D']

chees = copy.copy(spam)
chees[2] = 450
chees[3] = 'Liproll'

print(spam)

print(chees)
