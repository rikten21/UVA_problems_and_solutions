import sys

def snakesAndLeaders():
    T = int(sys.stdin.readline().strip())
    for t in range(T):
        line = sys.stdin.readline().strip()
        line = line.split(" ")
        a = int(line[0]) # játékosok száma
        b = int(line[1]) # kígyók és létrák száma
        c = int(line[2]) # dobások száma
        board = []
        importantSquares = [] # mezők, melyeken történik valami
        for i in range(b):
            squares = sys.stdin.readline().strip()
            squares = squares.split(" ")
            board.append(squares)
            importantSquares.append(int(squares[0]))
        players = [[]]
        for j in range(a):
            players.append(1)
        flag = 0 # valamelyik játékos elérte-e a 100-as mezőt
        for p in range(c):
            if flag == 1:
                sys.stdin.readline().strip()
            else:
                player = p%a + 1
                roll = int(sys.stdin.readline().strip())
                players[player] += roll
                if players[player] in importantSquares:
                    idx = importantSquares.index(players[player])
                    players[player] = int(board[idx][1])
                if players[player] >= 100:
                    players[player] = 100
                    flag = 1
        for P in range(1, a+1):
            print("Position of player {} is {}.".format(P, players[P]))

def main():
    snakesAndLeaders()

if __name__ == "__main__":
    main()