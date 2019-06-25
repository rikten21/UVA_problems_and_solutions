import sys

def mineSweeper():
    T = int(sys.stdin.readline().strip())
    for t in range(T):
        sys.stdin.readline()
        n = int(sys.stdin.readline().strip())
        board = []
        for i in range(n):
            row = sys.stdin.readline().strip()
            for j in range(n):
                board.append(row[j])
        for i in range(n):
            board.append(".")
        play = []
        for i in range(n):
            row = sys.stdin.readline().strip()
            for j in range(n):
                play.append(row[j])
        flag = 0
        for p in range(n*n):
            if play[p] == "x" and board[p] == "*":
                flag = 1
        for i in range(n):
            prow = ""
            for j in range(n):
                if play[i*n+j] == "x":
                    if board[i*n+j] == "*":
                        prow += "*"
                    elif board[i*n+j] == ".":
                        mines = 0
                        for r in range(3):
                            for c in range(3):
                                if (i-1+r) >= 0 and (i-1+r) < n and (j-1+c) >= 0 and (j-1+c) < n:
                                        if board[(i-1+r)*n+(j-1+c)] == "*":
                                            mines += 1
                        prow += str(mines)
                else:
                    if flag == 1 and board[i*n+j] == "*":
                        prow += "*"
                    else:
                        prow += "."
            print(prow)
        if t != T-1:
            print()

def main():
    mineSweeper()

if __name__ == "__main__":
    main()