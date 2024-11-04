immutable_var = tuple_ = 1, 2, 'a', 'b'
print(immutable_var)

# immutable_var[0] = 60
# print(immutable_var) # данный кортеж не поддерживает обращения по элементам

mutable_list = ['tomato', 'watermelon', 'plum', 'corn', 'pumpkin']

mutable_list[0:5] = 1, 2, 'a', 'b', 'Modified'
print(mutable_list)
