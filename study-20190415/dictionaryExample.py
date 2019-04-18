my_dict = {}
my_dict[0] = 'a'
my_dict['a'] = 1
my_dict['b'] = 2
print(my_dict['b'])
my_dict['c'] = 3
del my_dict[0]
print(my_dict)

# 딕셔러니 메소드 사용하는 예제1
for std in my_dict.values():
    print(std)

for std in my_dict.keys():
    print(std)

for key, val in my_dict.items():
    print(key, val)
