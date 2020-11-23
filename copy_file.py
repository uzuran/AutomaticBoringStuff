import copy

spam = ['A', 'B', 'C', 'D']
chees = copy.copy(spam)
chees[2] = 450

print(spam)
print(chees)
