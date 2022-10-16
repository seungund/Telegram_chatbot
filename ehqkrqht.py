import random
import os
import time


life = 5
score = 0

while 1:
    if life == 0:
        print("게임 종료")
        break

    N = random.randint(1,99)
    print("점수 : {}, 목숨 : {}".format(score, life))
    user = int(input("홀(0), 짝(1) : "))

    print("정답 : {}".format(N), end='/ ')

    if user:
        if N % 2:
            print("틀렸습니다.")
            life -= 1
        else:
            print("맞았습니다.")
            score += 100
    else:
        if N % 2:
            print("맞았습니다.")
            score += 100
        else:
            print("틀렸습니다.")
            life -= 1

    time.sleep(2)               # 프로그램을 잠시 멈춤
    os.system("cls")            # 화면을 바꿔줌

print("총 점수 : ", score)