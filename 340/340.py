import sys

def mestermindHints():
    idx = 1
    while True:
        N = int(sys.stdin.readline().strip())
        if N == 0:
            break
        print("Game {}:".format(idx))
        code = sys.stdin.readline().strip()
        code = code.split(" ")
        while True:
            guess = sys.stdin.readline().strip()
            guess = guess.split(" ")
            if guess[0] == "0":
                break
            hints = [0, 0, [], []]
            for i in range(N):
                if code[i] == guess[i]:
                    hints[0] += 1
                else:
                    hints[2].append(code[i])
                    hints[3].append(guess[i])
            hints[2].sort()
            hints[3].sort()
            idx1 = 0
            idx2 = 0
            while len(hints[2]) > idx1 and len(hints[3]) > idx2:
                if hints[2][idx1] == hints[3][idx2]:
                    hints[1] += 1
                    idx1 += 1
                    idx2 += 1
                elif hints[2][idx1] < hints[3][idx2]:
                    idx1 += 1
                else:
                    idx2 += 1

            print("    ({},{})".format(hints[0], hints[1]))
        idx += 1

def main():
    mestermindHints()

if __name__ == "__main__":
    main()