import random

def guess_nmber_game():
    target = random.randint(1,100)
    print("欢迎参加猜数字游戏，数字为1-100之间")

    while True:
        try:
            #获取用户输入
            guess = input("请输入你的猜测（1-100）：")
            # 尝试转换为整数
            num = int(guess)
            #检测数字范围
            if num < 1 or num > 100:
                print("输入数字超出范围，请重新输入")
                continue
            #判断猜测结果
            if num == target:
                print("猜对了，目标数字是(target)")
                break

            elif num < target:
                print("猜小了")
            else:
                print("猜大了")
        except ValueError:
            print("输入错误")
if __name__ == '__main__':
    guess_nmber_game()

