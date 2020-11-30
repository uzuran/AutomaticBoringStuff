def list_to_string(some_of_list):
    str1 = ', '
    return (str1.join(some_of_list))

some_of_list = ['apples','bananas','tofu','cats']

print(list_to_string(some_of_list))