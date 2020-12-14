import pprint

message = 'It was bright cold day in April, ' \
          'and the clock were striking thirteen.'
count = {}

for character in message:
    count.setdefault(character, 0)
    count[character] = count[character] + 1

pprint.pprint(count)