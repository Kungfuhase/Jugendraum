def create(rows, columns):
    element_empty = " "
    field = []
    for i in range (rows):
        field.append([])
        for j in range(columns):
            field[i].append(element_empty)
    return field

def create_empty(rows):
    field = []
    for i in range(rows):
        field.append([])
    return field

def check_4_same_list (list,player_symbol,length_check) :
    four_same = False
    for i in range(len(list)):
        if (len(list)) -i >= length_check:
            if list[i:i+length_check] == [player_symbol,player_symbol,player_symbol,player_symbol]:
                four_same = True
    return four_same

def check_4_same (board,player_symbol,length_check):
    four_same = False
    for i in range(len(board)):
        for j in range(len(board[i])):
            if (len(board[i])) -j >= length_check: 
                if board [i][j:j+length_check] == [player_symbol,player_symbol,player_symbol,player_symbol]: #noch nach besserer methode für player_symbol fragen
                    four_same = True
    return four_same
