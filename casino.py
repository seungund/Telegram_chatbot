import random   

door = ''' 

            @@@@@@@@@@@@@@@@@@@@@@@@   $$$$$$$$$$$$$$$$$$$$$$$$$   *************************
            @@                    @@   $$                     $$   **                     **
            @@                    @@   $$                     $$   **                     **
            @@                    @@   $$                     $$   **                     **
            @@        door        @@   $$        door         $$   **        door         **
            @@         1          @@   $$         2           $$   **         3           **
            @@                    @@   $$                     $$   **                     **
            @@                    @@   $$                     $$   **                     **
            @@                    @@   $$                     $$   **                     **
            @@@@@@@@@@@@@@@@@@@@@@@@   $$$$$$$$$$$$$$$$$$$$$$$$$   *************************

'''

road = '''

         A                 A      B                         B           C                     C
             A               A       B                      B           C                     C
               A              A       B                     B           C                    C
               A               A        B                   B           C                    C
                A               A       B                  B          C                   C
                   A       1      A      B        2        B        C         3        C
                      A             A    B                B        C                C
                        A            A    B               B      C                C
                           A          A    B              B    C               C
                             A         A   B            B   C             C
                               A         A B            B  C          C
                                A          AB           BC         C
                                  A                                C


'''

print("배팅게임에 오신 것을 환영합니다.\n")
print("한 레벨을 통과하실 때마다 배팅 금액의 2배를 상금으로 받으실 수 있습니다.\n")
print("레벨 통과에 실패하시면 모든 배팅 금액을 잃게 됩니다.\n")
print("=" * 31)
print()

bet = int(input("배팅 금액을 입력하세요. 단위 : $ >>> "))
print(f"총 ${bet} 배팅하셨습니다. ")

#level 1
print(road)

win = random.randint(1,3)
#print(win)
choice = int(input("3갈래의 길로 나뉘어 있습니다. 어느 길을 선택하시겠습니까? 1,2,3 >>>"))

if choice == win:

  print(f"축하합니다! 2배 획득!! 총 금액은 ${bet *2}7가 되었습니다.")
  next = input("다음단계로 이동하시겠습니까?   성공시 2배, 실패시 $0 ( y ) or ( n ) >>> ").lower()

#level 2
  if next == 'y':
    print(door)
    win = random.randint(1,3)
    #print(win)
    choice = int(input("총 3개의 문이 있습니다. 하나를 입력해주세요. 1,2,3 >>> "))
    if win == choice :
      print(f"축하합니다! 2배 획득!! 총 금액은 ${bet *4}7가 되었습니다.")
      print(f"게임이 종료되었습니다. 총 금액: ${bet *4} ")
    else:
      print("아쉽네요. 모든 배팅 금액을 잃었습니다.")
      
  else:
    print(f"게임이 종료되었습니다. 총 금액: ${bet *2} ")
else:
    print("아쉽네요. 모든 배팅 금액을 잃었습니다.")