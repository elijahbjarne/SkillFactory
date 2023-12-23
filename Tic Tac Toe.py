# Домашнее задание SkillFactory 
# Игра Крестики-нолики V0.0.2
# Добаавление ничьей
# Добааваление проверки ввода 
import os

clear = lambda: os.system('clear') # Для красоты, что бы стирать прошлые выводы
gui = [' ', '1', '2', '3',
        '1', '-', '-', '-',
        '2', '-', '-', '-',
        '3', '-', '-', '-']

# Условия победы
victory =   [[5, 6, 7],
            [9, 10, 11],
            [13, 14, 15],
            [5, 9, 13],
            [6, 10, 14],
            [7, 11, 15],
            [5, 10, 15],
            [7, 10, 13]]
check = True

def print_gui(): # Вывод игры в консоль
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

def step(column, line, symb): # Ставим символ в игру
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

def result(): # Определяем победителя
    win = ""
    for i in victory:
        if gui[i[0]] == "X" and gui[i[1]] == "X" and gui[i[2]] == "X":
            win = "X"
        if gui[i[0]] == "O" and gui[i[1]] == "O" and gui[i[2]] == "O":
            win = "O"
    return win

game_over = False
player1 = True
step_count = 0

# Основная программа
while game_over == False: 
    print_gui()
    check = True
    if player1 == True: # Ход первого игрока
        symb = "X"
        print("Игрок X")
        column = int(input("Введите колонку: "))
        line = int(input("Введите строку: "))
    else: # Ход второго игрока
        symb = "O"
        print("Игрок O")
        column = int(input("Введите колонку: "))
        line = int(input("Введите строку: "))
   
    step_count += 1

    if step_count == 9: # Проверка ничьей
        win = "дружба! :)"
        clear() 
    else:
        clear() # Убираем ненужное из консоли (для красоты)
        step(column, line, symb)
        win = result() 
        
# Проверка конца игры
    if win != "": 
        game_over = True
    else:
        game_over = False

    if check == True:
        player1 = not(player1) 
        print(check)
    if check == False:
        player1 = player1
        step_count -= 1
        print(check)

print_gui()
print("Победил(а)", win)
