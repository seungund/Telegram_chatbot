import random
import re

#숫자인지 문자인지 구별
while True:
    range = input("몇명인가요? ")

    if re.match("\d",range):
        range=int(range)
        winner = random.randint(1,range+1)
        count = []
        #제비뽑기 진행
        while True:
            num = int(input("원하시는 숫자를 입력해주세요 : "))
            
         #범위 판독
            if num<1 or num>range:
                print("범위 내의 숫자를 다시 입력해주세요")
        #당첨
            elif num == winner:
                print("당첨입니다ㅋ")
                break
        #입력했던값이랑 중복되는지 판별
            elif num in count:
              print("중복된 숫자입니다ㅋ")
        #탈락
            elif num != winner:
                print("아쉽네요~")
                count.append(num)
          

    else:
        print("숫자로 다시입력해주세요")
      
