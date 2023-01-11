class Person:
    # 생성자 매서드
    def __init__(self, name):
        self.name = name
        
    def greeting(self):
        return f'안녕.. 난 {self.name}'
    
    # 소멸자 메서드
    def __del__(self):
        ('ㅠㅠ')
        
# 인스턴스 생성
p1 = Person('아이유')
print(p1.greeting())

p2 = Person('뉴진스')
print(p2.greeting())
# print(Person.greeting(p2))

# Person('아이유')
# 파이썬 내부적으로 함수를 실행
# Person.__init__(xxxx, '아이유')

