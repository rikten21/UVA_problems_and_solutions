import sys

def mestermindHelper():
    puzzles = []
    for i in range(6):
        puzzles.append(codeGenerator(i, [], []))
    N = int(sys.stdin.readline().strip())
    for n in range(N):
        line = sys.stdin.readline().strip()
        line = line.split(" ")
        guess = [int(i) for i in line[0]]
        s = int(line[1])
        w = int(line[2])
        count = 0
        for i in range(len(puzzles[len(guess)])):
            strong, weak = hint(puzzles[len(guess)][i], guess)
            if strong == s and weak == w:
                count += 1
        print(count)

def codeGenerator(len, result, tmp):
    if len == 0:
        result.append(tmp)
        return result
    for i in range(1, 10):
        copylist = tmp.copy()
        copylist.append(i)
        codeGenerator(len - 1, result, copylist)
    return result

def hint(code, guess):
    hints = [0, 0, [], []]
    for i in range(len(code)):
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
    return hints[0], hints[1]

def main():
    mestermindHelper()

if __name__ == "__main__":
    main()