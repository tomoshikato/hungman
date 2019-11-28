def hangman(word):
    wrong = 0
    stages = ["",
              "_____      ",
              "|          ",
              "|    |     ",
              "|    0     ",
              "|   /|\    ",
              "|   / \    ",
              "|          "
             ]
    rletters = list(word)
    board = ["_"] * len(word)
    win = False
    print("Welcome to Hungman")
    while wrong < len(stages) - 1:
        print("\n")
        msg = "guess a letter"
        char = input(msg)
        if char in rletters:
            cind = rletters.index(char)
            board[cind] = char
            rletters[cind] = "$"
        else:
            wrong += 1
        print(" ".join(board))
        print("\n".join(stages[0: wrong + 1]))
        if "_" not in board:
            print("You Win")
            print(" ". join(board))
            win = True
            break
    if not win:
            print("\n".join(stages[0:wrong+1]))
            print("You Lose! Answer is {}".format(word))

hangman("cat")
