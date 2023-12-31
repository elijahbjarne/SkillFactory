# Домашнее задание SkillFactory 
# Игра Крестики-нолики V0.0.2
# Добаавление ничьей
# Добааваление проверки ввода 
import os

# Для красоты, что бы стирать прошлые выводы
clear = lambda: os.system('clear') 

# Рисуем пользовательсий интерфейс
gui = [' ', '1', '2', '3',
        '1', '-', '-', '-',
        '2', '-', '-', '-',
        '3', '-', '-', '-']

# Условия победы
victory = [[5, 6, 7],
            [9, 10, 11],
            [13, 14, 15],
            [5, 9, 13],
            [6, 10, 14],
            [7, 11, 15],
            [5, 10, 15],
            [7, 10, 13]]
check = True

# Вывод игры в консоль
def print_gui():
    print(gui[0], end = " ")
    print(gui[1], end = " ")
    print(gui[2], end = " ")
    print(gui[3])

    print(gui[4], end = " ")
    print(gui[5], end = " ")
    print(gui[6], end = " ")
    print(gui[7])

    print(gui[8], end = " ")
    print(gui[9], end = " ")
    print(gui[10], end = " ")
    print(gui[11])

    print(gui[12], end = " ")
    print(gui[13], end = " ")
    print(gui[14], end = " ")
    print(gui[15])

# Ставим символ в игру и проверяем не занята ли ячейка
def step(column, line, symb):
    global check  

    if column == 1 and line == 1:
        if gui[5] == "X" or gui[5] == "O":
            clear() 
            print("Ячейка занята")
            check = False
        else:
            gui[5] = symb
            

    if column == 1 and line == 2:
        if gui[9] == "X" or gui[9] == "O":
            clear() 
            print("Ячейка занята")
            check = False
        else:
            gui[9] = symb

    if column == 1 and line == 3:
            if gui[13] == "X" or gui[13] == "O":
                clear() 
                print("Ячейка занята") 
                check = False
            else:
                gui[13] = symb

    if column == 2 and line == 1:
        if gui[6] == "X" or gui[6] == "O":
            clear() 
            print("Ячейка занята")
            check = False
        else:
            gui[6] = symb

    if column == 2 and line == 2:
        if gui[10] == "X" or gui[10] == "O":
            clear() 
            print("Ячейка занята")
            check = False
        else:
            gui[10] = symb

    if column == 2 and line == 3:
        if gui[14] == "X" or gui[14] == "O":
            clear() 
            print("Ячейка занята")
            check = False
        else:
            gui[14] = symb

    if column == 3 and line == 1:
        if gui[7] == "X" or gui[7] == "O":
            clear() 
            print("Ячейка занята")
            check = False
        else:
            gui[7] = symb
  
    if column == 3 and line == 2:
        if gui[11] == "X" or gui[11] == "O":
            clear() 
            print("Ячейка занята")
            check = False
        else:
            gui[11] = symb
  
    if column == 3 and line == 3:
        if gui[15] == "X" or gui[15] == "O":
            clear() 
            print("Ячейка занята")
            check = False
        else:
            gui[15] = symb

# Определяем победителя
def result():
    win = ""
    for i in victory:
        if gui[i[0]] == "X" and gui[i[1]] == "X" and gui[i[2]] == "X":
            win = "X"
        if gui[i[0]] == "O" and gui[i[1]] == "O" and gui[i[2]] == "O":
            win = "O"
    return win

# Задаем необходимые переменные 
game_over = False
player1 = True
step_count = 0

# Основная программа
while game_over == False: 
    print_gui()
    check = True
# Ход первого игрока
    if player1 == True: 
        symb = "X"
        print("Игрок X")
# Ввод игрока 1

        try: # проверка ввода первого игрока (колонка)
            column = int(input("Введите колонку: "))
        except Exception: 
            print("Неверно введено значение, попробуйте еще раз")
            column = int(input("Введите колонку: "))

        try: # проверка ввода первого игрока (линия)
            line = int(input("Введите строку: "))
        except Exception:
            print("Неверно введено значение, попробуйте еще раз")
            line = int(input("Введите строку: "))

# Ход второго игрока
    else: 
        symb = "O"
        print("Игрок O")
# Ввод игрока 2

        try: # проверка ввода первого игрока (колонка)
            column = int(input("Введите колонку: "))
        except Exception: 
            print("Неверно введено значение, попробуйте еще раз")
            column = int(input("Введите колонку: "))

        try: # проверка ввода второго игрока (линия)
            line = int(input("Введите строку: "))
        except Exception:
            print("Неверно введено значение, попробуйте еще раз")
            line = int(input("Введите строку: "))
   
    step_count += 1

# Проверка ничьей
    if step_count == 9:
        win = "дружба! :)"
        clear() 
    else:
        clear()
        step(column, line, symb)
        win = result() 

# Проверка конца игры
    if win != "": 
        game_over = True
    else:
        game_over = False

# Делаем так, что бы нельзя было ставить символ в одно место 
    if check == True:
        player1 = not(player1) 
        print(check)

    if check == False:
        player1 = player1
        step_count -= 1
        print(check)

print_gui()
print("Победил(а)", win)
