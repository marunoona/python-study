import random
import datetime
friends = ['은지', '미래', '한나', '명진', '세영']
# 리스트 중 아무거나 하나 고르기 예제
print(random.choice(friends))
friends.append('희진')
friends.append('승원')
friends.append('제현')
friends.append('과네')
print(random.choice(friends))
# 리스트 중 중복 없이 여러개 뽑아내기
print(random.sample(friends, 2))
# 로또 번호 추출기
print(random.sample(range(1, 46), 6))
# 범위를 지정해서 뽑기
print(random.randint(5, 9))

# 오늘 날짜 구하기~
print(datetime.datetime.now())