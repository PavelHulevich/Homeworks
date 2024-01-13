string_in = '{}()[]{{(())}}[(])'
string_in = '([])[]{()}'
open_parenth = ['(', '[', '{']
close_parenth = [')', ']', '}']
pair_parenth = {'(': ')', '[': ']', '{': '}' }
string_list = list(string_in)
steck = '[('
i = 2
print(string_list[2], pair_parenth[steck[-1]])

# if string_list[2] == steck[-1]:
#     steck = steck[:-1]
