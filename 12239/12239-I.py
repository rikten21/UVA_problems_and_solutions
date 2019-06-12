import sys

def newBingo():
    while True:
        line = sys.stdin.readline().strip()
        if line == "0 0":
            break
        sline = line.split(" ")
        N = int(sline[0])
        B = int(sline[1])
        line = sys.stdin.readline().strip()
        leftovers = line.split(" ")
        values = []
        for z in range(N+1):
            values.append(0)
        for i in range(B):
            for j in range(i, B):
                value = abs(int(leftovers[i]) - int(leftovers[j]))
                if values[value] == 0:
                    values[value] = 1
        for v in range(N+1):
            if values[v] == 0:
                print('N')
                break
            elif v == N and values[v] != 0:
                print('Y')

def main():
    newBingo()

if __name__ == "__main__":
    main()