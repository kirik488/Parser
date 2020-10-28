import random
import copy
import time

print("Добро пожаловать в карточную игру в 21. Тут предусмотрены комбинации "
      "ТузТуз, 678 и 777.Комбинации дают при победе двойные очки. При равном счёте будете ничья")
bank_player = int(input("Введите кол-во монет"))
bank_comp = copy.copy(bank_player)

# Ценность
base = {"6": 6, "7": 7, "8": 8, "9": 9, "10": 10, "Валет": 2, "Дама": 3, "Король": 4}


# Колода
def deck_of_cards():
    stek = ["6", "7", "8", "9", "10", "Валет", "Дама", "Король", "Туз",
            "6", "7", "8", "9", "10", "Валет", "Дама", "Король", "Туз",
            "6", "7", "8", "9", "10", "Валет", "Дама", "Король", "Туз",
            "6", "7", "8", "9", "10", "Валет", "Дама", "Король", "Туз"
            ]
    random.shuffle(stek)
    return stek


# Значение туза
def account(arg):
    count = 0
    for i in arg:
        if i == "Туз":
            a = input("ТУЗ:Введите '-' если ровняется 1 и '+' если 11.")
            if a == "+":
                count += 11
            else:
                count += 1
        else:
            count += base[i]
    return count


# Комбинации
def comb(arg, a):
    if len(arg) == 3:
        if "6" in arg and "7" in arg and "8" in arg:
            print(f"В руке {a} есть комбинация 678")
            return True
        if arg.count("7") == 3:
            print(f"В руке {a} есть комбинация 777")
            return True
        else:
            return False


# Раунды
round_ = 1
while bank_comp > 0 and bank_player > 0:
    print(f"---Раунд:{round_}---")
    x = deck_of_cards()
    #  Игрок
    arm_player = []
    player_count = 0
    comp_combination = False
    player_combination = False
    while True:
        arg = input("'+' взять карту, '-' хватит")
        if arg == "+":
            arm_player.append(x.pop())
            time.sleep(0.3)
            print(arm_player)
            if len(arm_player) == 2 and arm_player.count("Туз") == 2:
                print("Золотое очко, два туза")
                player_count = 21
                player_combination = True
                break
        elif arg == "-":
            player_count = account(arm_player)
            break
        else:
            print("Такой команды нет")
    print("У вас:", player_count)
    # Компьютер
    print("-------------comp---------------")
    arm_comp = []
    comp_count = 0
    while True:
        if comp_count < 16:
            zc = x.pop()
            arm_comp.append(zc)
            if zc == "Туз":
                if len(arm_comp) == 2 and arm_comp.count("Туз") == 2:
                    print("Золотое очко, два туза")
                    comp_count = 21
                    comp_combination = True
                    break
                if comp_count + 11 <= 21:
                    comp_count += 11
                else:
                    comp_count += 1
            else:
                comp_count += base[zc]
            print("сomputer takes the card")
            time.sleep(1)
        else:
            print("Computer finished")
            time.sleep(2)
            break
    print("-------------comp---------------")
    print(f"Рука компа: {arm_comp}\n"
          f"ценность: {comp_count}")
    time.sleep(2)

    # Проверка на 678 и 777!!!
    if not player_combination:
        player_combination = comb(arm_player, "Игрока")
    if not comp_combination:
        comp_combination = comb(arm_comp, "Компьютера")

    # Победа в раунде
    if comp_count <= 21 and player_count > 21:
        if comp_combination:
            bank_comp += 2
            print("Победил компьютер с комбинацией. Получает два очка")
        else:
            bank_comp += 1
            print("Победил компьютер. +1 очко в банк")
        bank_player -= 1
    elif comp_count > 21 and player_count <= 21:
        if player_combination:
            bank_player += 2
            print("Вы победили с комбинацией. +2 очка")
        else:
            bank_player += 1
            print("Вы победили и получаете 1 очко")
        bank_comp -= 1
    elif comp_count > 21 and player_count > 21:
        print("Вы оба перебрали. счёт не изменился")
    elif comp_count <= 21 and player_count <= 21:
        if comp_count == player_count:
            print("Ничья. счёт не изменился")
        elif comp_count > player_count:
            if comp_combination:
                bank_comp += 2
                print("Победил компьютер с комбинацией. Получает два очка")
            else:
                bank_comp += 1
                print("Победил компьютер. +1 очко в банк")
            bank_player -= 1
        elif comp_count < player_count:
            if player_combination:
                bank_player += 2
                print("Вы победили с комбинацией. +2 очка")
            else:
                bank_player += 1
                print("Вы победили и получаете 1 очко")
            bank_comp -= 1
    print(f"Компьютер: {bank_comp}.\n"
          f"Игрок: {bank_player}.")
    round_ += 1
print("_________Общий счёт____________")
if bank_comp > bank_player:
    print("К сожалению ваш банк пуст, компьютер набрал", bank_comp, "очка")
elif bank_comp < bank_player:
    print("Вы победила компьютер набрав", bank_player, "очка")
