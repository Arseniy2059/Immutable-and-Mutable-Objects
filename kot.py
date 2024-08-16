immutable_var = tuple_ = 1,2,3,4,5, 5.5
print(immutable_var)

immutable_var
print(immutable_var) # данный кортеж не поддерживает обращения по элементам

mutable_list = ["tomato", "watermelon", "plum"]
print(mutable_list[0:3])

mutable_list[0:3] = "banana", "pumpkin", "beet"
print(mutable_list)