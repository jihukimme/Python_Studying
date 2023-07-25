#파이썬 기본 문법 1




#실수형
print(5)
print(-10)
print(3.14)
print(1000)
print(5+3)
print(2*8)
print(3*(3+1))


#문자형
print('나비')
print("나비")
print("ㅋㅋㅋㅋㅋㅋㅋㅋㅋㅋㅋㅋㅋㅋㅋㅋㅋ")
print("ㅋ"*10)


# 참/거짓 == 불리안
print(5 > 10)
print(5 < 10)
print(True)
print(False)
print(not True)
print(not False)
print(not (5 > 10))


# 애완동물을 소개해 주세요 //변수활용
name = "연탄이"
animal = "강아지"
age = 4
hobby = "산책"
is_adult = age >= 3

print("우리집 " + animal + "의 이름은 " + name + "에요")
hobby = "공놀이"
print(name + "는" + str(age) + "살이며, " + hobby + "을 좋아해요")
#print(name,"는", age,"살이며, ",hobby,"을 좋아해요")
print(name + "는 어른일까요?" + str(is_adult))


#주석
''' 이렇게 하면 
여러 문장에 
주석이 처리 됨'''

# ctrl + /   == 여러문장에 한번에 주석
# ctrl + /   == 여러문장에 한번에 ctrl + / 



print(1+1)
print(3-2)
print(5*2)
print(6/3)

print(2**3) #2^3 = 8
print(5%3) #나머지 구하기
print(10%3) #1
print(5//3) #1
print(10//3) #3

print(10>3) #true
print(4>=7) #false
print(10<3) #false
print(5<=5) #true

print(3==3) #true
print(3+4 == 7) #true


print(1 != 3) #true
print(not(1 != 3)) #false

print((3>0) and (3<5)) #true
print((3>0) & (3<5)) #true

print((3>0) or (3>5)) #true
print((3>0) | (3>5)) #true

print(5>4>3) #true

number = 2 + 3 *4 #14
number = number + 2 # 16
number += 2 # 18
print(number)



#숫자처리함수
print(abs(-5)) #절대값 5
print(pow(4,2)) #4^2 = 4*4 = 16
print(max(5,12)) #12
print(min(5,12)) #5

print(round(3.14)) #3
print(round(4.99)) #5

    #math라이브러리에 있는 것을 이용하겠다..
from math import *
print(floor(4.99)) #내림 4
print(ceil(3.14)) #올림 4
print(sqrt(16)) #제곱근 4


#랜덤함수
from random import *
print(random()) #0.0이상 1.0미만 임의의 값 생성
print(random() * 10) #0.0~ 10.0 미만의 임의의 값 생성
print(int(random() * 10)) #0~10 미만의 임의의 값 생성
print(int(random()*10) + 1) #1~10이하의 값 생성

print(int(random()*45) + 1) #1~45이하의 임의의 값 생성
print(randrange(1,46)) #1~ 46 미만의 임의의 값 생성

print(randint(1,45)) #1~45 이하의 임의의 값 생성

date = randint(4,28)
print("스터디 모임 날짜는 매월 ",date,"일로 설정되었습니다.")


#문자열
sentence = '나는 소년입니다'
print(sentence)
sentence2 = "파이썬은 쉬워요"
print(sentence2)
sentence3 = """
나는 소년이고 
파이썬은 쉬워요
"""
print(sentence3)


#슬라이싱
jumin = "001215-1234567"
print("성별: " + jumin[7])
print("연: " + jumin[0:2]) #0번째 값 부터 2두번째 값 직전 값까지
print("월 :"+ jumin[2:4])
print("일 :"+jumin[4:6])

print("생년월일: "+jumin[:6]) #처음부터 6번째 직전 값까지
print("뒤 7자리 : "+ jumin[7:]) #7부터 끝까지
print("뒤 7자리 (뒤에서부터) : " + jumin[-7:]) #맨뒤에서 7번째부터 끝까지


#문자열 처리함수 
python = "Python is Amazing"
print(python.lower())
print(python.upper())
print(python[0].isupper())
print(len(python))

print(python.replace("Python", "Java"))

index = python.index("n")
print(index)
index = python.index("n", index + 1)
print(index)

print(python.find("n"))

print(python.count("n"))


#문자열 포맷
print("a"+"b")
print("a", "b")

    #방법1
print("나는 %d살입니다" % 20)
print("나는 %s를 좋아해요. " %"파이썬")
print("Apple은 %c로 시작해요." %"A")

    # %s
print("나는 %s색과 %s색을 좋아해요." %("파란", "빨간"))

    #방법2
print("나는 {}살입니다." .format(20))
print("나는 {}색과 {}색을 좋아해요." .format("파란", "빨간"))

    #방법3
print("나는 {age}살이며, {color}색을 좋아해요." .format(age = 20, color = "빨간"))

    #방법4 (v3.6이상~)
age = 20
color = "빨간"
print(f"나는 {age}살이며, {color}색을 좋아해요.")


#탈출문자
#\n : 줄바꿈
print("백문이 불여일견\n백견이 불여일타")
print("저는 '김지후'입니다.")
#\ : 문자로 인식
print("저는 \"김지후\"입니다.")
#\\ : 문장 내에서 \
print("\\\\")
#\r : 커서를 맨앞으로 이동
print("Red Apple\rPine")
#\b : 백스페이스(한 글자 삭제)
print("Redd\bApple")
#\t : 탭
print("Red\tApple")


#리스트 []
#지하철 칸별로 10명, 20명, 30명
subway1 = 10
subway2 = 20
subway3 = 30

subway = [10,20,30]
print(subway)

subway = ["유재석", "조세호", "박명수"]
print(subway)

    #조세호가 몇번째 칸에 타고 있는가?
print(subway.index("조세호"))
    #하하가 다음 정류장에서 다음칸에 탐
subway.append("하하")
print(subway)
    #정형돈이 유재석,조세호 사이에 탐
subway.insert(1, "정형돈")
print(subway)
    #지하철에 있는 사람을 한명씩 뒤에서 꺼냄
print(subway.pop())
print(subway)

    #같은 이름의 사람이 몇명 있는지 확인
subway.append("유재석")
print(subway)
print(subway.count("유재석"))


#정렬도 가능
num_list = [5,2,4,3,1]
num_list.sort()
print(num_list)

    #순서 뒤집기 가능
num_list.reverse()
print(num_list)

    #모두 지우기
num_list.clear()
print(num_list)

    #다양한 자료형과 함께 사용
num_list = [5,4,3,2,1]
mix_list = ["조세호", 20, True]
print(mix_list)

num_list.extend(mix_list)
print(num_list)


#사전
cabinet = {3:"유재석", 100:"김태호"}
print(cabinet[3])
print(cabinet[100])

print(cabinet.get(3))
print(cabinet.get(5, "사용가능"))

print(3 in cabinet) #true
print(5 in cabinet) #false

cabinet[5] = "김지후"
print(cabinet)
del cabinet[5]
print(cabinet)
print(cabinet.keys())
print(cabinet.values())

cabinet.clear()
print(cabinet)


#튜플
menu = ("돈까스", "치즈까스")
print(menu[0])
print(menu[1])

name ="김종국"
age = 20
hobby = "코딩"
print(name, age, hobby)

(name, age, hobby) = ("김종국", 20, "코딩")
print(name, age, hobby)


#집합(set) //중복 안됨, 순서 없음
my_set = {1,2,3,3,3}
print(my_set)

java = {"유재석", "김태호", "양세형"}
python = set(["유재석", "박명수"])

    #교집합 (java python 모두 할 수 있는 사람)
print(java & python)
print(java.intersection(python))

    #합집합
print(java | python)
print(java.union(python))

    #차집합(java 할 수 있지만 python은 모르는)
print(java - python)
print(java.difference(python))

python.add("김태호")
print(python)
python.remove("김태호")
print(python)



#자료구조의 변경
#커피숍
menu = {"커피", "우유", "주스"}
print(menu, type(menu))

menu = list(menu)
print(menu, type(menu))

menu = tuple(menu)
print(menu, type(menu))

menu = set(menu)
print(menu, type(menu))
print(menu)


#shuffle, sample, from random import *
from random import *
users = range(1,21) #1부터 20까지
print(type(users))
users = list(users)
print(type(users))

print(users)
shuffle(users) #무작위로 썪음

winners = sample(users, 4) #users 중 4명을 뽑음
print("치킨 당첨자: {0}" .format(winners[0]))
print("커피 당첨자: {0}" .format(winners[1:]))



#if
weather = "비"
#weather = input("오늘 날씨는 어때요? ") #input
if weather == "비" or weather == "눈":
    print("우산을 챙기세요")
elif weather == "미세먼지":
    print("마스크를 챙기세요")
else:
    print("준비물 필요 없어요")

temp = 10
#temp = int(input("기온은 어때요? "))
if 30 <= temp:
    print("너무 더워요. 나가지 마세요")
elif 10<=temp and temp <30:
    print("괜찮은 날씨에요")
elif 0 <= temp < 10:
    print("외투를 챙기세요")
else:
    print("너무 추워요")



#for
print("대기번호 : 1")
print("대기번호 : 2")
print("대기번호 : 3")
print("대기번호 : 4")

for waiting_nu in [1, 2, 3, 4]:
    print("대기번호 : {0}" .format(waiting_nu))

for wait_nu in range(1,5):
    print("대기번호 : {0}" .format(wait_nu))

starbucks = ["아이언맨", "토르", "그루트"]
for customers in starbucks:
    print("{0}, 커피가 준비되었습니다" .format(customers))



#while
customer = "토르"
index = 5
while index >= 1:
    print("{0}, 커피가 준비되었습니다. {1}번 남았어요." .format(customer, index))
    index -= 1
    if index == 0:
        print("커피는 폐기처분 되었습니다")


customer = "토르"
person = "unknown"

while person != customer:
    print("{0}, 커피가 준비 되었습니다" .format(customer))
    #person = input("이름이 어떻게 되세요? ")
    person = "토르"



#continue, break
absent = [2, 5] #결석
no_book = [7]
for student in range(1, 11): # 1~10번까지 출석번호
    if student in absent:
        continue
    elif student in no_book:
        print("오늘 수업 여기까지. {0}번은 교무실로 따라와" .format(student))
    print("{0}, 책을 읽어봐" .format(student))



#한줄 for문
#출석번호가 1 2 3 4, 앞에 100을 붙이기로 함 -> 101, 102, 103, 104
students = [1,2,3,4,5]
print(students)
students = [i + 100 for i in students]
print(students)

#학생 이름을 길이로 변환
students = ["iron man", "thor", "groot"]
students = [len(i) for i in students]
print(students)

#학생 이름을 대문자로 변환
students = ["iron man", "thor", "groot"]
students = [i.upper() for i in students]
print(students)


