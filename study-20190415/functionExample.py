# 결과값을 돌려주는 함수 만들기
def add(num1, num2):
    return num1 + num2


print(add(1, 2))

# 한개 이상의 결과값을 돌려주는 함수 만들기
def add_mul(num1, num2):
    return num1 + num2, num1 * num2


print(add_mul(1, 2))  # 이렇게 출력하면 튜플로 Packing 되어 출력됨

my_add, my_mul = add_mul(1, 2)  # 이런 식으로 Unpacking 가능함
print(my_add)
print(my_mul)
