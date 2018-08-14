import  board_tools


board_example = [
    ["X"," "," "," "," "," "," "],
    ["X"," "," "," "," "," "," "],
    ["X"," "," "," "," "," "," "],
    ["X"," "," "," "," "," "," "],
    ["X"," "," "," "," "," "," "],
    ["X"," "," "," "," "," "," "],

]


def ui_board (board):
    print("   1   2   3   4   5   6   7")
    print(" |",board[0][0],  "|", board[0][1],  "|", board[0][2],  "|", board[0][3],  "|", board[0][4],  "|", board[0][5],  "|", board[0][6], "|")
    print(" |",board[1][0],  "|", board[1][1],  "|", board[1][2],  "|", board[1][3],  "|", board[1][4],  "|", board[1][5],  "|", board[1][6], "|")
    print(" |",board[2][0],  "|", board[2][1],  "|", board[2][2],  "|", board[2][3],  "|", board[2][4],  "|", board[2][5],  "|", board[2][6], "|")
    print(" |",board[3][0],  "|", board[3][1],  "|", board[3][2],  "|", board[3][3],  "|", board[3][4],  "|", board[3][5],  "|", board[3][6], "|")
    print(" |",board[4][0],  "|", board[4][1],  "|", board[4][2],  "|", board[4][3],  "|", board[4][4],  "|", board[4][5],  "|", board[4][6], "|")
    print(" |",board[5][0],  "|", board[5][1],  "|", board[5][2],  "|", board[5][3],  "|", board[5][4],  "|", board[5][5],  "|", board[5][6], "|")


def row_check (board,column):
    row_possible = 5
    for i in range(len(board)):  # checks which row is possible for placing an token\player symbol in this column. by checking the index (column) element of every row
        if board [i] [column-1] == " ":
            row_possible = i
        elif board [i] [column-1] != " ":
            if i == 0:            #fixing the problem that it would return 5 if the first row is blocked.Which happens bc the row_possible doen't get changed by a loop if the first one is blocked
                row_possible = None
                return row_possible
            else:
                return row_possible



    return (row_possible)


def check_4_same (board,player_symbol):
    four_same = False
    for i in range(len(board)): #überprüft ob vier aufeinanderfolgende elemente in einer list gleich sind fängt in der obersten an
        for j in range(len(board[i])):
            if (len(board[i])) -j >= 4: #Solange Elemente von j bis j+4 exitiert tue x (abruch falls nach elemten j nicht mehr 3 weitere kommen / nicht mehr 4 elemente möglich sind)
                if board [i][j:j+4] == [player_symbol,player_symbol,player_symbol,player_symbol]: #noch nach besserer methode für player_symbol fragen
                    four_same = True
    return four_same


def check_4_same_list (list,player_symbol):
    four_same = False
    for i in range(len(list)):
        if (len(list)) -i >= 4:
            if list[i:i+4] == [player_symbol,player_symbol,player_symbol,player_symbol]:  #noch nach besserer methode für player_symbol fragen
                four_same = True
    return four_same


def check_vert (board,player_symbol):
    won = False
    columns = board_tools.create_empty(7)
    for i in range(len(board[0])): #wandelt liste mit  [rows[columns]] in [columns[rows]] um
        for j in range(len(board)):
            columns[i].append(board[j][i])
    columns.reverse()

    for i in range(len(columns)):
        columns[i].reverse()
    won = check_4_same(columns,player_symbol)
    return won


def check_diag (board,player): #bug bei reversed liste die übergeben wird (Dafuq)
    board_infunc = board.copy()
    board_infunc.reverse()
    packs = []
    loops = 0
    while loops != 3:
        for j in range(4): 
            pack = []
            for i in range(len(board_infunc)-2 + loops):
                pack.append(board_infunc[i][j+i])
            if pack != [] :
                packs.append(pack)
        del board_infunc [0]
        loops += 1
    return (check_4_same(packs,player))


def change_board (board,player_symbol,column):
    row = row_check(board,column)
    board[row] [column-1] = player_symbol
    return board


def check_main (board,player_symbol):
    board = board.copy()
    board_reversed = board.copy()
    results = []

    results.append (check_4_same(board,player_symbol))
    results.append (check_vert(board,player_symbol))

    if board [2] != [" "," "," "," "," "," "," "]:
        results.append(check_diag(board,player_symbol))
        for i in range(len(board_reversed)):
            board_reversed[i].reverse()
        results.append(check_diag(board_reversed,player_symbol))
    if True in results:
        return True
    else :
        return False


def user_input(board):
    while True:
        try:
            choice = int(input("Bitte wähle die Spalte: "))
            print()
            if 1 <= choice <= 7:
              if row_check(board,choice) == None:
                print ("Diese Spalte ist bereits voll,versuche es erneut!")
                print()
                continue
              else:
                  return choice
            else:
              print("Du musst eine Zahl zwischen 1 und 7 eingeben!")
              print()
              continue
        except(ValueError,TypeError):
            print()
            print("Du musst eine Zahl von 1-7 eingeben !")
            print()
            continue


def main() :
    board_main = board_tools.create(6,7)
    player_turn = 0
    print()
    print("=== Willkommen bei 4 Gewinnt ===")
    print()
    print()

    while True:
        player_turn += 1

        if player_turn % 2 == 1:
            player = "X"
            player_int = 1
        elif player_turn % 2 == 0:
            player = "O"
            player_int = 2

        choice = user_input(board_main)
        board_main = change_board(board_main,player,choice)
        board_to_print = board_main.copy()
        ui_board(board_to_print)
        board_to_check = board_main.copy()
        print()
        if check_main(board_to_check,player) == True :
            print("Spieler :" ,player_int, " hat gewonnen")
            print()
            answer = input("Noch eine Runde? : ")
            answer.lower()
            if answer in ["yes","y","ja","j"]:
                main()
            else:
                break

        elif player_turn == 42:
            ui_board(board_main)
            print()
            print ("Unentschieden")
            print()
            answer = input("Noch eine Runde? :")
            print()
            answer.lower()
            if answer in ["yes","y","ja","j"]:
                main()
            else:
                break











main()
