#파이썬 기본 문법 2




#함수
def open_account():
    print("새로운 계좌가 생성되었습니다")

open_account()

def deposit(balance, money): #입금
    print("입금이 완료되었습니다. 잔액은 {0}원 입니다." .format(balance + money))
    return balance + money

def withdraw(balance, money): #출금
    if balance >= money:
        print("출금이 완료되었습니다. 잔액은 {0}원 입니다".format(balance - money))
        return balance - money
    else:
        print("출금이 완료되지 않았습니다. 잔액은 {0}원 입니다.".format(balance))
        return balance

def withdraw_night(balance, money): #저녁에 출금
    commission = 100
    return commission, balance - money - commission

balance = 0 #잔액
balance = deposit(balance, 1000)
print(balance)
commission, balance = withdraw_night(balance, 500)
print("수수료는 {0}원이며, 잔액은 {1}원 입니다".format(commission, balance))



#기본값
def profile(name, age = 17, main_lang = "파이썬"):
    print("이름: {0}\t나이: {1}\t주 사용 언어: {2}".format(name, age, main_lang))

profile("유재석", 20, "파이썬")
profile("김태호", 25, "자바")
profile("박명수")
    #같은 학교 같은 학년 같은 반 같은 수업



#키워드 값
def profile(name, age, main_lang):
    print(name, age, main_lang)

profile(name="유재석", main_lang = "파이썬", age = 20)
profile(main_lang = "자바", age=25, name = "김태호")



#가변인자
# def profile(name, age, lang1, lang2, lang3, lang4, lang5):
#     print("이름: {0}\t나이: {1}\t".format(name, age), end=" ")
#     print(lang1, lang2, lang3, lang4, lang5)
def profile(name, age, *language):
    print("이름: {0}\t나이: {1}\t".format(name, age), end=" ")
    for lang in language:
        print(lang, end=" ")
    print()

profile("유재석", 20, "python", "java", "c", "c++", "c#", "javascript")
profile("김태호", 25, "kotlin", "swift")



#지역변수 전역변수
    #전역변수
gun = 10

def checkpoint(soldiers): #경계근무
    global gun #전역 공간에 있는 gun 사용
    gun = gun - soldiers
    print("[함수 내] 남은 총: {0}".format(gun))

print("전체 총: {0}".format(gun))
checkpoint(2) #2명이 경계근무 나감
print("남은 총: {0}".format(gun))


    #지역변수
def checkpoint_ret(gun, soldiers):
    gun = gun - soldiers
    print("[함수 내] 남은 총: {0}" .format(gun))
    return gun

print("전체 총: {0}" .format(gun))
#checkpoint(2) #2명이 경계근무 나감
gun = checkpoint_ret(gun, 2)
print("남은 총: {0}" .format(gun))



#표준입출력
print("python", "java", "javascript", sep=" vs ")
print("python", "java", sep = ", ", end = "?" )
print("무엇이 더 재밌을까요?")

import sys
print("python", "java", file=sys.stdout) #표준출력으로 출력
print("python", "java", file=sys.stderr) #표준에러로 출력

scores = {"수학":0, "영어":50, "코딩":100}
for subject, score in scores.items():
    print(subject, score)
    print(subject.ljust(8), str(score).rjust(4), sep=":")

#은행 대기 순번표
#001, 002, 003, ...
for num in range(1,21):
    print("대기번호 : " +str(num).zfill(3))

# answer = input("아무값이나 입력하세요 : ")
# print(type(answer))
# print("입력하신 값은 "+answer+"입니다")



#빈자리는 빈공간으로 두고, 오른쪽으로 정렬을 하되, 총 10자리 공간을 확보
print("{0: >10}" .format(500))
#양수일 땐 +로 표시, 음수일 땐 -로 표시
print("{0: >+10}".format(500))
print("{0: >+10}".format(-500))
#왼쪽 정렬하고, 빈칸으로 _로 채움
print("{0:_<10}" .format(500))
#3자리 마다 콤마를 찍어주기
print("{0:,}" .format(10000000000000))
#3자리 마다 콤마를 찍어주고, +-기호 붙이기
print("{0:+,}" .format(10000000000000))
#소수점 출력
print("{0:f}".format(5/3))
#소수점을 특정 자리수까지만 표시
print("{0:.2f}".format(5/3))



#파일 입출력
# score_file = open("score.txt", "w", encoding = "utf8")
# print("수학 : 0", file=score_file)
# print("영어 : 50", file=score_file)
# score_file.close()
# # w:쓰기   a:덮어쓰기
# score_file = open("score.txt", "a", encoding = "utf8")
# score_file.write("과학 : 80")
# score_file.write("\n코딩 : 100")
# score_file.close()

# score_file = open("score.txt", "r", encoding="utf8")
# print(score_file.read())
# score_file.close()

# score_file = open("score.txt", "r", encoding="utf8")
# print(score_file.readline(), end="") #줄별로 읽기, 한줄 읽고 커서는 다음 줄로 이동
# print(score_file.readline(),end="")
# print(score_file.readline(),end="")
# print(score_file.readline(),end="")
# score_file.close()

# score_file = open("score.txt", "r", encoding = "utf8")
# while True:
#     line = score_file.readline()
#     if not line:
#         break
#     print(line)
# score_file.close()

# score_file = open("score.txt", "r", encoding = "utf8")
# lines = score_file.readlines() #list형태로 저장
# for line in lines:
#     print(line, end="")

# score_file.close()




#pickle 
#데이터를 파일형태로 저장해서.. 데이터를 .. 코드에서 
# import pickle
# profile_file = open("profile.pickle", "wb")
# profile = {"이름":"박명수", "나이":30, "취미":["축구", "골프", "코딩"]}
# print(profile)
# pickle.dump(profile, profile_file)
# profile_file.close()

# profile_file = open("profile.pickle", "rb")
# profile = pickle.load(profile_file) #file에 있는 정보를 profile에 불러오기
# print(profile)
# profile_file.close()




# #with
# import pickle
# with open("profile.pickle", "rb") as profile_file:
#     print(pickle.load(profile_file))


# with open("study.txt", "w", encoding="utf8") as study_file:
#     study_file.write("파이썬을 열심히 공부하고 있어요")

# with open("study.txt", "r", encoding="utf8") as study_file:
#     print(study_file.read())