#클래스를 활용해보기




# #클래스
# #스타크래프트
# #마린 : 공격유닛, 군인. 총을 쏠 수 있음
# name = "마린"
# hp = 40
# damage = 5

# print("{} 유닛이 생성되었습니다 " .format(name))
# print("체력 {0}, 공격력 {1}\n" .format(hp, damage))

# #탱크 : 공격유닛, 탱크, 포를 쏠 수 있음, 일반 모드/ 시즈 모드
# tank_name = "탱크"
# tank_hp = 150
# tank_damage = 35

# print("{0} 유닛이 생성되었습니다 " .format(tank_name))
# print("체력 {0}, 공격력 {1}\n" .format(tank_hp, tank_damage))

# def attack(name, location, damage):
#     print("{0} : {1} 방향으로 적군을 공격합니다. [공격력 {2}]" .format(name, location, damage))

# attack(name , "1시", damage)
# attack(tank_name, "1시", tank_damage)



# #클래스
# #__init__ 함수  //파이썬에서 사용되는 생성자 //자동으로 생성되는?? 객체??
# class Unit: 
#     def __init__(self, name, hp, damage):
#         self.name = name
#         self.hp = hp
#         self.damage = damage
#         print("{0} 유닛이 생성 되었습니다 " .format(self.name))
#         print("체력 {0}, 공격력 {1}" .format(self.hp, self.damage))

# marine1 = Unit("마린", 40, 5)
# marine2 = Unit("마린", 40, 5)
# tank = Unit("탱크", 150, 35)
# #멤버변수
# #레이스 : 공중 유닛, 비행기. 클로깅(상대방에게 보이지 않음)
# wraith1 = Unit("레이스", 80, 5)
# print("유닛 이름 : {0}, 공격력 : {1}" .format(warith1.name, warith1.damage))
# #마인드 컨트롤 : 상대방 유닛을 내 것으로 만드는 것(빼앗음)
# wraith2 = ("빼앗은 레이스", 80, 5)
# wraith2.clocking = True

# if wraith2.clocking == True:
#     print("{0}는 현재 클로킹 상태입니다" .format(wraith2.name))


# #일반유닛
# class Unit: 
#     def __init__(self, name, hp, damage):
#         self.name = name
#         self.hp = hp
#         self.damage = damage
#         print("{0} 유닛이 생성 되었습니다 " .format(self.name))
#         print("체력 {0}, 공격력 {1}" .format(self.hp, self.damage))

# #공격유닛
# class AttackUnit:
#     def __init__(self, name, hp, damage):
#         self.name = name
#         self.hp = hp
#         self.damage = damage

#     def attack(self, location):
#         print("{0} : {1} 방향으로 적군을 공격합니다. [공격력 {2}]" .format(self.name, location, self.damage))

#     def damaged(self, damage):
#         print("{0} : {1} 데미지를 입었습니다 " .format(self.name, damage))
#         self.hp -= damage
#         print("{0} : 현재 체력은 {1}입니다 " .format(self.name, self.hp))
#         if self.hp <= 0:
#             print("{0} : 파괴되었습니다 " .format(self.name))

# #파이어뱃: 공격유닛, 화염방사기
# firebat1 = AttackUnit("파이어뱃", 50, 16)
# firebat1.attack("5시")

# #공격을 2번 받는다고 가정
# firebat1.damaged(25)
# firebat1.damaged(25)




# #상속

# #메딕 : 의무병
# #일반유닛
# class Unit: 
#     def __init__(self, name, hp):
#         self.name = name
#         self.hp = hp

# #공격유닛
# class AttackUnit(Unit):
#     def __init__(self, name, hp, damage):
#         Unit.__init__(self, name, hp)
#         self.damage = damage

#     def attack(self, location):
#         print("{0} : {1} 방향으로 적군을 공격합니다. [공격력 {2}]" .format(self.name, location, self.damage))

#     def damaged(self, damage):
#         print("{0} : {1} 데미지를 입었습니다 " .format(self.name, damage))
#         self.hp -= damage
#         print("{0} : 현재 체력은 {1}입니다 " .format(self.name, self.hp))
#         if self.hp <= 0:
#             print("{0} : 파괴되었습니다 " .format(self.name))

# #파이어뱃: 공격유닛, 화염방사기
# firebat1 = AttackUnit("파이어뱃", 50, 16)
# firebat1.attack("5시")

# #공격을 2번 받는다고 가정
# firebat1.damaged(25)
# firebat1.damaged(25)



# #다중상속

# #메딕 : 의무병
# #일반유닛
# class Unit: 
#     def __init__(self, name, hp):
#         self.name = name
#         self.hp = hp

# #공격유닛
# class AttackUnit(Unit):
#     def __init__(self, name, hp, damage):
#         Unit.__init__(self, name, hp)
#         self.damage = damage

#     def attack(self, location):
#         print("{0} : {1} 방향으로 적군을 공격합니다. [공격력 {2}]" .format(self.name, location, self.damage))

#     def damaged(self, damage):
#         print("{0} : {1} 데미지를 입었습니다 " .format(self.name, damage))
#         self.hp -= damage
#         print("{0} : 현재 체력은 {1}입니다 " .format(self.name, self.hp))
#         if self.hp <= 0:
#             print("{0} : 파괴되었습니다 " .format(self.name))

# #드랍쉽 : 공중유닛, 수송기. 마린/파이어뱃/탱크 등을 수송. 공격기능X
# class Flyable:
#     def __init__(self, flying_speed):
#         self.flying_speed = flying_speed

#     def fly(self, name, location):
#         print("{0} : {1} 방향으로 날아갑니다 [속도 {2}]" .format(name, location, self.flying_speed))

# #공중공격 유닛 클래스
# class FlyableAttackUnit(AttackUnit, Flyable):
#     def __init__(self, name, hp, damage, flying_speed):
#         AttackUnit.__init__(self, name, hp, damage)
#         Flyable.__init__(self, flying_speed)

# #발키리 : 공중 공격 유닛, 한번에 14발 미사일 발사
# varkyrie = FlyableAttackUnit("발키리", 200, 6, 5)
# varkyrie.fly(varkyrie.name, "3시")

# #파이어뱃: 공격유닛, 화염방사기
# firebat1 = AttackUnit("파이어뱃", 50, 16)
# firebat1.attack("5시")

# #공격을 2번 받는다고 가정
# firebat1.damaged(25)
# firebat1.damaged(25)



# #오버라이딩 : 부모클래스 말고 자식클래스의 .. 를 쓰고 싶을 때?

# #메딕 : 의무병
# #일반유닛
# class Unit: 
#     def __init__(self, name, hp, speed):
#         self.name = name
#         self.hp = hp
#         self.speed = speed

#     def move(self, location):
#         print("[지상 유닛 이동]")
#         print("{0} : {1} 방향으로 이동합니다. [속도 {2}]" \
#             .format(self.name, location, self.speed))

# #공격유닛
# class AttackUnit(Unit):
#     def __init__(self, name, hp, speed, damage):
#         Unit.__init__(self, name, hp, speed)
#         self.damage = damage

#     def attack(self, location):
#         print("{0} : {1} 방향으로 적군을 공격합니다. [공격력 {2}]" .format(self.name, location, self.damage))

#     def damaged(self, damage):
#         print("{0} : {1} 데미지를 입었습니다 " .format(self.name, damage))
#         self.hp -= damage
#         print("{0} : 현재 체력은 {1}입니다 " .format(self.name, self.hp))
#         if self.hp <= 0:
#             print("{0} : 파괴되었습니다 " .format(self.name))

# #드랍쉽 : 공중유닛, 수송기. 마린/파이어뱃/탱크 등을 수송. 공격기능X
# class Flyable:
#     def __init__(self, flying_speed):
#         self.flying_speed = flying_speed

#     def fly(self, name, location):
#         print("{0} : {1} 방향으로 날아갑니다 [속도 {2}]" .format(name, location, self.flying_speed))

# #공중공격 유닛 클래스
# class FlyableAttackUnit(AttackUnit, Flyable):
#     def __init__(self, name, hp, damage, flying_speed):
#         AttackUnit.__init__(self, name, hp, 0, damage) #지상 speed 0
#         Flyable.__init__(self, flying_speed)

#     def move(self, location):
#         print("[공중 유닛 이동]")
#         self.fly(self.name, location)

# #벌처 : 지상 유닛, 가동성이 좋음
# vulture = AttackUnit("벌쳐", 80, 10, 20)

# #배틀크루저: 공중유닛, 처력도 좋음, 공격력도 좋음
# battlecruiser = FlyableAttackUnit("배틀크루저", 500, 25, 3)

# vulture.move("11시")
# #battlecruiser.fly(battlecruiser.name, "9시")
# battlecruiser.move("9시")



# #건물
# class BuildingUnit(Unit):
#     def __init__(self, name, hp, location):
#         #Unit.__init__(self, name, hp, 0) ==
#         super().__init__(name, hp, 0)  #하나의 클래스만 상속할 수 있다
#         self.location = location





#스타크래프트 프로젝트

#메딕 : 의무병
#일반유닛
class Unit: 
    def __init__(self, name, hp, speed):
        self.name = name
        self.hp = hp
        self.speed = speed
        print("{0} 유닛이 생성되었습니다" .format(name))

    def move(self, location):
        print("[지상 유닛 이동]")
        print("{0} : {1} 방향으로 이동합니다. [속도 {2}]" \
            .format(self.name, location, self.speed))

    def damaged(self, damage):
        print("{0} : {1} 데미지를 입었습니다 " .format(self.name, damage))
        self.hp -= damage
        print("{0} : 현재 체력은 {1}입니다 " .format(self.name, self.hp))
        if self.hp <= 0:
            print("{0} : 파괴되었습니다 " .format(self.name))

#공격유닛

class AttackUnit(Unit):
    def __init__(self, name, hp, speed, damage):
        Unit.__init__(self, name, hp, speed)
        self.damage = damage

    def attack(self, location):
        print("{0} : {1} 방향으로 적군을 공격합니다. [공격력 {2}]" .format(self.name, location, self.damage))

#마린
class Marine(AttackUnit):
    def __init__(self):
        AttackUnit.__init__(self, "마린", 40, 1, 5)

    #스팀팩: 일정 시간 동안 이동 및 공격속도 증가, 체력 10 감소
    def stimpack(self):
        if self.hp > 10:
            self.hp -= 10
            print("{0} : 스팀팩을 사용합니다 (HP 10 감소)" .format(self.name))
        else:
            print("{0} : 체력이 부족하여 스팀팩을 사용하지 않습니다" .format(self.name))


#탱크
class Tank(AttackUnit):
    #시즈모드 : 탱크를 고정시켜서 더 높은 파워로 공격 가능
    seize_developed = False #시즈모드 개발여부

    def __init__(self):
        AttackUnit.__init__(self, "탱크", 150, 1, 35)
        self.seize_mode = False

    def set_seize_mode(self):
        if Tank.seize_developed == False:
            return

        #현재 시즈모드가 아닐 때 ==> 사즈모드
        if self.seize_mode == False:
            print("{0} : 시즈모드로 전환합니다 " .format(self.name))
            self.damage *= 2
            self.seize_mode = True

        #현재 시즈모드일 때 ==> 시즈모드 해제
        else:
            print("{0} : 시즈모드를 해제합니다 " .format(self.name))
            self.damage /=2
            self.seize_mode = False

#드랍쉽 : 공중유닛, 수송기. 마린/파이어뱃/탱크 등을 수송. 공격기능X
class Flyable:
    def __init__(self, flying_speed):
        self.flying_speed = flying_speed

    def fly(self, name, location):
        print("{0} : {1} 방향으로 날아갑니다 [속도 {2}]" .format(name, location, self.flying_speed))

#공중공격 유닛 클래스
class FlyableAttackUnit(AttackUnit, Flyable):
    def __init__(self, name, hp, damage, flying_speed):
        AttackUnit.__init__(self, name, hp, 0, damage) #지상 speed 0
        Flyable.__init__(self, flying_speed)

    def move(self, location):
        print("[공중 유닛 이동]")
        self.fly(self.name, location)

#레이스
class Wraith(FlyableAttackUnit):
    def __init__(self):
        FlyableAttackUnit.__init__(self, "레이스", 80, 20 ,5)
        self.clocked = False #클로킹 모드 (해제상태)

    def clocking(self):
        if self.clocked == True: #클로킹 모드-> 모드해제
            print("{0} : 클로킹 모드 해제합니다" .format(self.name))
            self.clocked = False
        else: #클로킹모드해제 -> 모드 설정
            print("{0} : 클로킹 모드 설정합니다" .format(self.name))
            self.clocked = True

def game_start():
    print("[알림] 새로운 게임을 시작합니다.")

def game_over():
    print("Player : gg")
    print("[player] 님이 게임에서 퇴장하셨습니다")



#실제게임 시작
game_start()

#마린 3개 생성
m1 = Marine()
m2 = Marine()
m3 = Marine()

#탱크 2개
t1 = Tank()
t2 = Tank()

#레이스 1개 생성
w1 = Wraith()

#유닛 일괄 관리
attack_units = []
attack_units.append(m1)
attack_units.append(m2)
attack_units.append(m3)
attack_units.append(t1)
attack_units.append(t2)
attack_units.append(w1)

#전군 이동
for unit in attack_units:
    unit.move("1시")

#탱크 시즈모드 개발
Tank.seize_developed = True
print("[알림] 탱크 시즈모드 개발이 완료되었습니다")

#공격모드 준비(마린: 스팀팩, 탱크: 시즈모드, 레이스: 클로킹)
for unut in attack_units:
    if isinstance(unit, Marine):
        unit.stimpack()
    elif isinstance(unit, Tank):
        unit.set_seize_mode()
    elif isinstance(unit, Wraith):
        unit.clocking()

#전군 공격
for unit in attack_units:
    unit.attack("1시")

#전군 피해
from random import *
for unit in attack_units:
    unit.damaged(randint(5, 21)) #공격은 랜덤으로 받음(5~20)


#게임종료
game_over()