import random

def human():
    word_list = ["ちんちん", "うんち", "おなら", "とっぽぎ"]
    random_number = random.randint(0, 4)
    word = word_list[random_number]
    wrong = 0
    stages = ["",
             "_________",
             "|       |",
             "|       |",
             "|       0",
             "|      -|- ",
             "|       |",
             "|      //",
             "|"
             ]

    rletters = list(word)
    board = ["_"] * len(word)
    win = False
    print("ハングマンへようこそ！")
    print("人が吊るされる絵が完成する前に5文字を予測しよう！")
    print("ヒントはこの前みた")

    while wrong < len(stages) - 1:
        print("\n")
        msg = "1文字予想してね："
        chr = input(msg)

        if chr in rletters:
            cind = rletters.index(chr)
            board[cind] = chr
            rletters[cind] = "$"
        else:
            wrong = wrong + 1

        print("こたえ：" + " ".join(board))
        e = wrong + 1
        print("\n".join(stages[0:e]))

        if "_" not in board:
            print("あなたの勝ち！！！")
            print("".join(board))
            win = True
            break
    if not win:
        print("\n".join(stages))
        print("あなたの負け！正解は{}".format(word))

human()

