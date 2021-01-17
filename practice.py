# Крестики нолики
board = [[], [], []]


def printo():
    print(board[0])
    print(board[1])
    print(board[2])


i = 1
while i < 10:
    add = input("Первым ходит Х потом 0 ведите индекс, например(11): ")
    value = ""
    if i % 2 == 0:
        value = '0'
    else:
        value = 'х'
    i += 1

    if add == '00':
        board[0].insert(0, value)
        printo()
    elif add == '01':
        board[0].insert(1, value)
        printo()
    elif add == '02':
        board[0].insert(2, value)
        printo()

    elif add == '10':
        board[1].insert(0, value)
        printo()
    elif add == '11':
        board[1].insert(1, value)
        printo()
    elif add == '12':
        board[1].insert(2, value)
        printo()

    elif add == '20':
        board[2].insert(0, value)
        printo()
    elif add == '21':
        board[2].insert(1, value)
        printo()
    elif add == '22':
        board[2].insert(2, value)
        printo()


file = 'result.txt'
s = ""
for n in board:
    s += str(n) + '\n'

f = open(file, 'a')
f.write("\n" + s)
f.close()
