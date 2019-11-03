#1st version
#1.Choose a horse
#2.Use 2 dices to start
#3.Rule
import random
import time

horse1 = 0
horse2 = 0
choose = input('请选一匹马，输入 1 或 2')
print ('你选的是'+str(choose)+'号马，加油')
if choose == 1:
    player1 = horse1
    player2 = horse2
else:
    player1 = horse2
    player2 = horse1
time.sleep(1)
start=input('开始游戏? 输入 Y 开始')
while horse1<10 and horse2<10:
    if start == 'Y': #开始掷骰子
        time.sleep(1)
        print('开始掷马骰子')
        rollhorse = random.randint(1, 2)
        time.sleep(1)
        print ('掷出一个'+str(rollhorse)+','+str(rollhorse)+'号马开始走')
        time.sleep(1)
        print('开始掷步数骰子')
        rollstep = random.randint(0, 2)
        time.sleep(1)
        print('掷出一个' + str(rollstep) + ',' + str(rollhorse) + '号马走了'+str(rollstep)+'步')
        if rollhorse == 1 :
            horse1 = horse1+rollstep
            if horse1>=10:
                time.sleep(1)
                print('1号马赢了')
            else:
                time.sleep(1)
                print('1号马在第'+str(horse1)+'格')

        else:
            horse2 = horse2+rollstep
            if horse2 >= 10:
                time.sleep(1)
                print('2号马赢了')
            else:
                time.sleep(1)
                print('2号马在第' + str(horse2) + '格')