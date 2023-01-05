# 모듈을 가져오는 것!

import random

print(random.choice(['햄버거', '국밥', '초밥']))

num_lotto = []

for i in range(1,46):
    num_lotto.append(i)
    
print(random.sample(range(1,46),6))

# shuffle 
# 리스트 안의 값을 무작위로 섞는다.