def search_word_txt(file, words):
    indices = []
    for i in range(len(file)):
        if '\n' in file[i]:
            file[i] = file[i].rstrip('\n')
        for word in words:
            start_i = 0
            done = False
            while not done:
                if word in file[i][start_i:]:
                    index = file[i].find(word, start_i)
                    indices.append(('Row:' + str(i), index, word))
                    start_i += index + len(word)
                else:
                    done = True
    return indices


def search_word_and_x(file, words, length_x):
    indices = []
    for i in range(len(file)):
        if '\n' in file[i]:
            file[i] = file[i].rstrip('\n')
        for word in words:
            start_i = 0
            done = False
            while not done:
                if word in file[i][start_i:]:
                    index = file[i].find(word, start_i)
                    start_i += index + len(word)
                    if len(file[i][start_i:]) < length_x:
                        part_1 = file[i][start_i:]
                        dif = length_x - len(file[i][start_i:])
                        part_2 = file[i+1][0 if dif == 0 else 0:dif+1]
                        following_word = part_1 + part_2
                        row = i
                    elif len(file[i][start_i:start_i+length_x]) == 0:
                        following_word = file[i+1][0:length_x]
                        row = i+1
                    else:
                        following_word = file[i][start_i:start_i + length_x]
                        row = i
                    indices.append(('Row:' + row, index, word, following_word))
                else:
                    done = True
    return indices


def search_word_string(string, words):
    indices = []

    for word in words:
            start_i = 0
            done = False
            while not done:
                if word in string[start_i:]:
                    index = string.find(word, start_i)
                    indices.append((index, word))
                    start_i += index + len(word)
                else:
                    done = True
    return indices


def search_word_and_x_string(string, words, length_x):
    indices = []
    for word in words:
        start_i = 0
        done = False
        while not done:
            if word in string[start_i:]:
                index = string.find(word, start_i)
                start_i += index + len(word)
                indices.append((index, word, string[start_i:start_i + length_x]))
            else:
                done = True
    return indices


def y_n_question (msg="Yes or No?: "):
    while True:
        q = input(msg)
        if q.lower() in ['y', 'yes']:
            answer = True
            break
        elif q.lower() in ['n', 'no']:
            answer = False
            break
        else:
            print('Please enter y or n')
            continue
    return answer






if __name__ == '__main__':
    print("=============================")
    print("      Txt search tool    ")
    print("      Version 0.1        ")
    print("============================= ")
    choice = ''
    while choice != 'q':
        print("\n Options:")
        print("     [1] Search words in txt and print index")
        print("     [2] Search words in txt and print index + following figures ")
        print("     [3] Search words in string and print index + following figures ")
        print("     [4] Search words in string and print index ")
        print("     [q] quit \n")
        choice = input("Please choose a function: ")
        if choice in ['1', '2']:
            while True:
                path = input("Please enter the path(plus .txt): ")
                try:
                    txt = open(path).readlines()
                    break
                except Exception:
                    print("\nThis is an invalid path\n")
            words_raw = input("Please enter the words, divide them with a ',' no spaces")
            words = words_raw.split(',')
            if choice == '1':
                result_tuple = search_word_txt(txt,words)
                if not result_tuple:
                    check_again = y_n_question("Nothing found but you could check it again (no rows): ")
                    if check_again:
                        txt_string = open(path).read()
                        for i in range(len(txt_string)):
                            txt_string = txt_string.rstrip('\n')
                        result_tuple = search_word_string(txt_string,words)
                        if not result_tuple:
                            print('Still nothing found')
                            cont = y_n_question("Continue?: ")
                            if not cont:
                                choice = 'q'
            elif choice == '2':
                while True:
                    length_following_figures = int(input('Please enter the number of following figures: '))
                    if length_following_figures <= 0:
                        break
                    else:
                        print("Invalid length try again")
                result_tuple = search_word_and_x(txt,words,length_following_figures)


                #HEREEEEEEEEEEE

                pass
        elif choice == 'q' or 'Q':
            print("Closing the program")
            break
        else:
            print("Invalid choice please try again")
            continue
