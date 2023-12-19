# Домашнее задание SkillFactory 
# Игра Крестики-нолики
import os

clear = lambda: os.system('cls')
gui = [' ', '1', '2', '3',
        '1', '-', '-', '-',
        '2', '-', '-', '-',
        '3', '-', '-', '-']

victory = [ [5, 6, 7],
            [9, 10, 11],
            [13, 14, 15],
            [5, 9, 13],
            [6, 10, 14],
            [7, 11, 15],
            [5, 10, 15],
            [7, 10, 13]]

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

def step(column, line, symb):
    if column == 1 and line == 1:
        gui[5] = symb
    if column == 1 and line == 2:
        gui[9] = symb
    if column == 1 and line == 3:
        gui[13] = symb

    if column == 2 and line == 1:
        gui[6] = symb
    if column == 2 and line == 2:
        gui[10] = symb
    if column == 2 and line == 3:
        gui[14] = symb

    if column == 3 and line == 1:
        gui[7] = symb
    if column == 3 and line == 2:
        gui[11] = symb
    if column == 3 and line == 3:
        gui[15] = symb

def result():
    win = ""
    for i in victory:
        if gui[i[0]] == "X" and gui[i[1]] == "X" and gui[i[2]] == "X":
            win = "X"
        if gui[i[0]] == "O" and gui[i[1]] == "O" and gui[i[2]] == "O":
            win = "O"
    return win

def busy():
    if 


game_over = False
p1 = True

while game_over == False:
    print_gui()
    if p1 == True:
        symb = "X"
        print("Игрок 1")
        column = int(input("Введите колонку: "))
        line = int(input("Введите строку: "))
    else:
        symb = "O"
        print("Игрок 2")
        column = int(input("Введите колонку: "))
        line = int(input("Введите строку: "))
    clear()
    step(column, line, symb)
    win = result() 

    if win != "":
        game_over = True
    else:
        game_over = False
    p1 = not(p1) 

print_gui()
print("победил", win)