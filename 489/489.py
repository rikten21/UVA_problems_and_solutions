import sys

def hangmanJudge():
    while True:
        r = sys.stdin.readline().strip()
        if r == "-1":
            break
        print("Round", r)
        word = sys.stdin.readline().strip()
        solutionLetters = list(set(word))
        guessline = sys.stdin.readline().strip()
        guesses = []
        for i in guessline:
            if i not in guesses:
                guesses.append(i)
        strokes = 0
        for i in range(len(guesses)):
            if guesses[i] in solutionLetters:
                solutionLetters.remove(guesses[i])
                if len(solutionLetters) == 0:
                    print("You win.")
                    break
            else:
                strokes += 1
            if strokes == 7:
                print("You lose.")
                break
        if len(solutionLetters) > 0 and strokes < 7:
            print("You chickened out.")

def main():
    hangmanJudge()

if __name__ == "__main__":
    main()