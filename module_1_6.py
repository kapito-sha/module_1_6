my_dict = {'Cherchik': '10 years old', 'Lunya': '8 years old', 'Dobik': '12 years old', 'Stella': '7 years old'}
print('my_dict:', my_dict)
print('Dobik:', my_dict.get('Dobik'), ', Glasha:', my_dict.get('Glasha'))
my_dict.update({'Glasha': 'died in 2010',
                'Sherya': '5 years old'})
removed = my_dict.pop('Dobik')
print('Removed value: ', removed)
print('my_dict updated:', my_dict)
my_set = {True, 5, (8, 7), 3.14, 'air', (8, 7), 3.14, 3.14, True, 'air', 0.3, 0.3}
print('my_set:', my_set)
my_set.update([29424829, 99])
my_set.discard(True)
print("my_set updated: ", my_set)




