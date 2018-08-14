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