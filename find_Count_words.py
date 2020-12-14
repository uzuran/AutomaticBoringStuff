import re
import string
frequency = {}
document_text = open('', 'r', encoding='utf8')
text_string = document_text.read().lower()
match_pattern = re.findall(r'\b[a-z]{3,15}\b', text_string)

for word in match_pattern:
    count = frequency.get(word, 0)
    frequency[word] = count + 1

frequency_list = frequency.keys()

for word in frequency_list:
    print(word, frequency[word])
