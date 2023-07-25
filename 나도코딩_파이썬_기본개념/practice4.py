#모듈과 패키지 활용해보기




# #예외처리 1
# try:
#     print("나누기 전용 계산기입니다")
#     num1 = int(input("첫번째 숫자를 입력하세요: "))
#     num2 = int(input("두번째 숫자를 입력하세요: "))
#     print("{0} / {1} = {2} " .format(num1, num2, int(num1/num2)))
# except ValueError:
#     print("에러! 잘못된 값을 입력하였습니다. ")
# except ZeroDivisionError as err:
#     print(err)



# #예외처리 2
# try:
#     print("나누기 전용 계산기입니다")
#     nums = []
#     nums.append(int(input("첫번째 숫자를 입력하세요: ")))
#     nums.append(int(input("두번째 숫자를 입력하세요: ")))
#     #nums.append(int(nums[0]/nums[1]))
#     print("{0} / {1} = {2} " .format(nums[0], nums[1], nums[2]))
# except ValueError:
#     print("에러! 잘못된 값을 입력하였습니다. ")
# except ZeroDivisionError as err:
#     print(err)
# except Exception as err:
#     print("에러가 발생했습니다.")
#     print(err)
# except:
#     print("원인 모를 에러 발생")




# #에러 발생시키기
# try:
#     print("한 자리 숫자 나누기 전용 계산기입니다.")
#     num1 = int(input("첫 번째 숫자를 입력하세요: "))
#     num2 = int(input("두 번째 숫자를 입력하세요: "))
#     if num1 >= 10 or num2 >= 10:
#         raise ValueError
#     print("{0} / {1} = {2}" .format(num1, num2, int(num1/num2)))
# except ValueError:
#     print("잘못된 값을 입력하였습니다. 한 자리 숫자만 입력하세요.")



# #사용자 정의 예외 처리
# class BigNumberError(Exception):
#     def __init(self, msg):
#         self.msg = msg
    
#     def __str__(self):
#         return self.msg

# try:
#     print("한 자리 숫자 나누기 전용 계산기입니다.")
#     num1 = int(input("첫 번째 숫자를 입력하세요: "))
#     num2 = int(input("두 번째 숫자를 입력하세요: "))
#     if num1 >= 10 or num2 >= 10:
#         raise BigNumberError("입력값: {0}, {1}" .format(num1, num2))
#     print("{0} / {1} = {2}" .format(num1, num2, int(num1/num2)))
# except ValueError:
#     print("잘못된 값을 입력하였습니다. 한 자리 숫자만 입력하세요.")
# except BigNumberError as err:
#     print("에러가 발생하였습니다. 한 자리 숫자만 입력하세요")
#     print(err)




# #finally
# class BigNumberError(Exception):
#     def __init(self, msg):
#         self.msg = msg
    
#     def __str__(self):
#         return self.msg

# try:
#     print("한 자리 숫자 나누기 전용 계산기입니다.")
#     num1 = int(input("첫 번째 숫자를 입력하세요: "))
#     num2 = int(input("두 번째 숫자를 입력하세요: "))
#     if num1 >= 10 or num2 >= 10:
#         raise BigNumberError("입력값: {0}, {1}" .format(num1, num2))
#     print("{0} / {1} = {2}" .format(num1, num2, int(num1/num2)))
# except ValueError:
#     print("잘못된 값을 입력하였습니다. 한 자리 숫자만 입력하세요.")
# except BigNumberError as err:
#     print("에러가 발생하였습니다. 한 자리 숫자만 입력하세요")
#     print(err)
# finally:
#     print("계산기를 이용해 주셔서 감사합니다")




#모듈
#극장에 있다. 현금만 받는다. 잔돈을 안바꿔준다. 

# #일반가격
# def price(people):
#     print("{0}명 가격은 {1}원입니다." .format(prople, people*10000))

# #조조할인 가격
# def price_morning(people):
#     print("{0}명 조조할인 가격은 {1}원 입니다." .format(people, people*6000))

# #군인할인 가격
# def price_soldier(people):
#     print("{0}명 군인 할인 가격은 {1}원 입니다." .format(people, people*4000))

# import theater_module_in_practice4
# theater_module_in_practice4.price(3)
# theater_module_in_practice4.price_morning(4)
# theater_module_in_practice4.price_soldier(5)

# import theater_module_in_practice4 as mv
# mv.price(3)
# mv.price_morning(4)
# mv.price_soldier(5)

# from theater_module_in_practice4 import *
# #from random import *
# price(3)
# price_morning(4)
# price_soldier(5)

# from theater_module_in_practice4 import price_morning, price
# price(5)
# price_morning(6)

# from theater_module_in_practice4 import price_soldier as price
# price(5)





#패키지// 모듈을 모아놓은 집합
#신규 여행사 프로젝트를 담당하게 됐다. 태국,베트남 패키지 여행상품을 제공한다. 패키지 내용을 파이썬 내용의 패키지로 만들어라

# import travel_in_practice4.thailand_in_practice4
# trip_to = travel_in_practice4.thailand_in_practice4.ThailandPackage()
# trip_to.detail()

# from travel_in_practice4.thailand_in_practice4 import ThailandPackage
# trip_to = ThailandPackage()
# trip_to.detail()

# from travel_in_practice4 import vietnam_in_practice4
# trip_to = vietnam_in_practice4.VietnamPackage()
# trip_to.detail()



# # #__all__
# # # from random import *
# # # from travel_in_practice4 import *오류가 발생한다. //실제로는 개발자가 공개범위를 설정해주어야 한다. // -> __init__.py에서 설정해주도록 하자
# # from travel_in_practice4 import *
# # trip_to = vietnam_in_practice4.VietnamPackage()
# # trip_to = thailand4_in_practice4.ThailandPackage()
# # trip_to.detail()

# from travel_in_practice4 import *
# from travel_in_practice4.thailand_in_practice4 import ThailandPackage
# trip_to = ThailandPackage()
# trip_to.detail()




# #패키지, 모듈 위치 확인
# import inspect
# import random

# from travel_in_practice4.thailand_in_practice4 import ThailandPackage
# print(inspect.getfile(random))
# print(inspect.getfile(ThailandPackage))





#pip install
#pip로 패키지 설치하기
#google접속 -> pypi입력 -> 제일 상단에 뜨는 사이트 접속 ->browsw project -> topic(다양한 주제로 프로젝트 분류 되어있음)
#beautifulsoup(웹스크리핑에 유명한..)
#터미널을 통해서 pip명령을 실행하고 .. 할 수 있음.







# #내장함수

# #input : 사용자 입력을 받는 함수

# #dir : 어떤 객체를 넘겨 줬을 때 그 객체가 어떤 변수와 함수를 가지고 있는지 알려주는 함수
# import random
# print(dir())
# import pickle
# print(dir())
# list = [1, 2, 3]
# print(dir(list))
# name = "jim"
# print(dir(name))





#외장함수
#ex : random

##glob : 경로내의 폴더/ 파일 목록 조회 (윈도우 dir)
# import glob
# print(glob.glob("*.py")) #확장자가 py인 모든 파일

##os : 운영체제에서 제공하는 기본 기능
# import os
# print(os.getcwd()) #현재 디렉토리

# folder = "sample_dir"

# if os.path.exists(folder):
#     print("이미 존재하는 폴더입니다.")
#     os.rmdir(folder)
#     print(folder, "폴더를 삭제하였습니다.")
# else:
#     os.makedirs(folder) #폴더 생성
#     print(folder, "폴더를 생성하였습니다")

# import os
# print(os.listdir())

# #time : 시간 관련 함수
# import time
# print(time.localtime())
# print(time.strftime("%Y-%m-%d %H:%M:%S"))

# import datetime
# print("오늘 날짜는 ", datetime.date.today())

# #timedelta : 두 날짜 사이의 간격
# today = datetime.date.today() #오늘 날짜 저장
# td = datetime.timedelta(days = 100) #100일 저장
# print("우리가 만난지 100일은", today + td) #오늘부터 100일 후







