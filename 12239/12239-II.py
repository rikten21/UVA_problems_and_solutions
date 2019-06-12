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
        for i in range(B):
            for j in range(i, B):
                value = abs(int(leftovers[i]) - int(leftovers[j]))
                values.append(value)
        values = set(values)
        values = list(values)
        idx1 = 0
        idx2 = 0
        while idx1 < N+1 and idx2 < len(values):
            if idx1 == values[idx2]:
                idx1 += 1
                idx2 += 1
            else:
                break
        if idx1 == N+1:
            print("Y")
        else:
            print('N')

def main():
    newBingo()

if __name__ == "__main__":
    main()