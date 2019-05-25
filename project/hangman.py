lives = 10
word = "Parth".lower()

def findAllPositions(ch):
    pos = list()
    for i in range(len(word)):
        if (word[i] == ch):
            pos.append(i)
    return pos

def addCharInAnswer(answer, ch, positions):
    for pos in positions:
        answer[pos] = ch
    return answer

def play():
    global word, lives
    answer = ["_"] * len(word)
    while(lives > 0 and ("_" in answer)):
        ch = input("Guess a character : ").lower()
        positions = findAllPositions(ch)
        if len(positions) == 0:
            print("Wrong Guess!! You lost 1 life")
            lives-=1
            print("Lives left : {}".format(lives))
        else:
            print("Awesome!!You guessed right.")
            answer = addCharInAnswer(answer, ch, positions)
            print(answer)

    if ("_" not in answer):
        print("You won. Answer is : ")
        print(answer)
    else:
        print("Game Over!!! You lost")

play()
