cost = int(input("금액을 입력하시오: "))
people = int(input("몇명인지입력하시오: "))

average = (cost / people)
print("1인당 %d원씩 지불하시면 됩니다"% average)

if (cost % people) != 0:
    print("남은 금액은 가위바위보를 통해 당첨자가 %d원을 지불하시면 됩니다^^"%(cost % people))