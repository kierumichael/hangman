import password
def hangman ():
    wrong = 0
    stages = ["\nHangman\n######################\n",
              "________         ",
              "|                ",
              "|       |        ",
              "|       0        ",
              "|      /|\       ",
              "|       w===3    ",
              "|      / \       ",
              "|                "]

    win = False
    print (" Welcome to Hangman\n######################\n")
    print("Player1:Enter a word ")
    word=password.pyssword()
    rletters = list (word)
    board = ["__"] * len(word)
    while wrong < len(stages) - 1:
        print("\n")
        msg = "Player2:Guess a letter: "
        char = input(msg)
        if char in rletters:
            cind = rletters.index(char)
            board[cind] = char
            rletters[cind] = '$'
        else:
            wrong += 1
            print(wrong)
        print((" ".join(board)))
        e = wrong + 1
        print(e)
        print("\n".join(stages[0: e]))
        if "__" not in board:
            print ("\nYou Win!")
            print(" ".join(board))
            win = True
            hangman()
            
    if not win:
        print("\n".join(stages[0: wrong]))
        print("\nYou lose! It was {}.".format(word))
        hangman()

hangman()

                     
