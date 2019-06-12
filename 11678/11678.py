import sys

def switch():
    while True:
        line = sys.stdin.readline().strip()
        if line == "0 0":
            break
        line = line.split(" ")
        A = int(line[0])
        B = int(line[1])
        Ai = sys.stdin.readline().strip()
        Ai = Ai.split(" ")
        Ai = set(Ai)
        Bi = sys.stdin.readline().strip()
        Bi = Bi.split(" ")
        Bi = set(Bi)
        difAi = []
        difBi = []
        for i in Ai:
            difAi.append(i)
        for j in Bi:
            difBi.append(j)
        maxA = 0
        maxB = 0
        for a in range(len(difAi)):
            if difAi[a] not in Bi:
                maxA += 1
        for b in range(len(difBi)):
            if difBi[b] not in Ai:
                maxB += 1
        print(min(maxA, maxB))

def main():
    switch()

if __name__ == "__main__":
    main()