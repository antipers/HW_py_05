# Создайте программу для игры с конфетами человек против человека.
# Условие задачи: На столе лежит 2021 конфета.
# Играют два игрока делая ход друг после друга.
# Первый ход определяется жеребьёвкой.
# За один ход можно забрать не более чем 28 конфет.
# Все конфеты оппонента достаются сделавшему последний ход.
# Сколько конфет нужно взять первому игроку, чтобы забрать все конфеты у своего конкурента?

from random import randint


def count_candys(x):
    x = int(
        input(f"{x}, сколько конфет вы хотите взят и скушац, в диапазоне от 1 до 28: "))
    while x < 1 or x > 28:
        x = int(
            input(f"{x}, введите количество конфет, в диапазоне от 1 до 28: "))
    return x


def play():
    player_1 = input("Имя первого игрока: ")
    player_2 = input("Имя второго игрока: ")
    value_candys = int(input("Сколько всего конфет будет на столе: "))
    turn = randint(0, 2)

    if turn:
        print(f"Первым ходит игрок: {player_1}")

    else:
        print(f"Первым ходит игрок: {player_2}")

    while value_candys > 27:
        if turn:
            value_candys -= count_candys(player_1)
            turn = False
            print(f"На столе осталось: {value_candys} конфет")
        else:

            value_candys -= count_candys(player_2)
            turn = True
            print(f"На столе осталось: {value_candys} конфет")

    if value_candys:
        print(f"Выиграл игрок: {player_1}")
    else:
        print(f"Выиграл игрок: {player_2}")


play()
