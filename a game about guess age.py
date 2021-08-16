# 猜年龄小游戏
# 1 允许用户最多尝试3次
# 2 每尝试3次后，如果还没猜对，就问用户是否还想继续玩，如果回答Y或者y,就继续让其猜3次，以此往复，如果回答N或者n,就退出程序
# 3 猜对了，就直接退出



import random

age = random.randint(0, 101)
print(age)
time = 0
while time < 3:
    guess = int(input('输入你的猜测: '))
    if guess == age:
        print('恭喜你猜对了')
        break
        pass
    elif time == 2:
        choice = input('输入你的选择: ')
        if choice == 'Y' or choice == 'y':
            print('可以再尝试3次')
            time = -1
            print('time 此时的值是多少 %d' % time)
            pass
        elif choice == 'N' or choice == 'n':
            print('放弃也是一种选择')
            break
            exit(0)
            pass
        pass
    time += 1
    print('time          此时的值是多少 %d' % time)
    pass
