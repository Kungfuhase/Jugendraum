import  board_tools
def check_diag (board):
    board_infunc = board.copy[:]
    board_infunc.reverse()
    packs = []
    loops = 0
    while loops != 3:
        for j in range(4): # bis 4 (range 5 ) == bis 4
            pack = []
            for i in range(len(board_infunc)-2 + loops):
                print(board_infunc[i][j + i])


                pack.append(board_infunc[i][j+i])
            if pack != [] :
                packs.append(pack)
        del board_infunc [0]
        loops += 1
    return packs






board_example = [
        ["1.2", "1.2", "1.3", "1.4", "1.5", "1.6", "1.7"],
        ["2.1", "2.2", "2.3", "2.4", "2.5", "2.6", "2.7"],
        ["3.1", "3.2", "3.3", "3.4", "3.5", "3.6", "3.7"],
        ["4.1", "4.2", "4.3", "4.4", "4.5 ","4.6 ","4.7"],
        ["5.1", "5.2", "5.3", "5.4", "5.5", "5.6", "5.7"],
        ["6.1", "6.2", "6.3", "6.4", "6.5", "6.6", "6.7"],

    ]

print(board_example)
print(check_diag(board_example))
print(board_example)