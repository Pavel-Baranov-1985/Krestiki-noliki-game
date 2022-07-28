def greet():
    print("  Крестики-нолики  ")
    print("-------------------")
    print(" формат ввода: x y ")
    print(" x - номер строки  ")
    print(" y - номер столбца ")

field = [[" ", " ", " "] for i in range(3)]

def show():
    print(f"  0 1 2")
    for i in range(3):
        print(f"{i} {field[i][0]} {field[i][1]} {field[i][2]}")

def your_step():
    while True:
        x, y = map(int, input("Ваш ход: ").split())

        if 0 <= x <= 2 and 0 <= y <= 2 :
            if field[x][y] == " ":
                return x, y
            else:
                print("Ячейка занята")
        else:
            print("Выход за пределы")

def winner():
    win_cord = [((0, 0), (0, 1), (0, 2)), ((1, 0), (1, 1), (1, 2)), ((2, 0), (2, 1), (2, 2)),
                ((0, 0), (1, 0), (2, 0)), ((0, 1), (1, 1), (2, 1)), ((0, 2), (1, 2), (2, 2)),
                ((0, 0), (1, 1), (2, 2)), ((0, 2), (1, 1), (2, 0))]
    for cord in win_cord:
        symbols = []
        for c in cord:
            symbols.append(field[c[0]][c[1]])
        if symbols == ["X", "X", "X"]:
            print("Выиграл X!!!")
            return True
        if symbols == ["0", "0", "0"]:
            print("Выиграл 0!!!")
            return True
    return False

greet()

step = 0
while True:
    step += 1

    show()

    if step % 2 == 1:
        print("Ходит крестик")
    else:
        print("Ходит нолик")

    x, y = your_step()

    if step % 2 == 1:
        field[x][y] = "X"
    else:
        field[x][y] = "0"

    if step == 9:
        print("Ничья!")
        break

    if winner():
        break
