import sys

def moveTheBishop():
    C = int(sys.stdin.readline().strip())
    for c in range(C):
        sys.stdin.readline().strip()
        T = int(sys.stdin.readline().strip())
        N = int(sys.stdin.readline().strip())
        for t in range(T):
            positions = sys.stdin.readline().strip()
            positions = positions.split(" ")
            rB = int(positions[0])
            cB = int(positions[1])
            rG = int(positions[2])
            cG = int(positions[3])
            if rB == rG and cB == cG:
                print(0)
            elif ((rB+cB) % 2 == 0 and (rG+cG) % 2 != 0) or ((rB+cB) % 2 != 0 and (rG+cG) % 2 == 0):
                print("no move")
            elif abs(rB - rG) == abs(cB - cG):
                print(1)
            else:
                print(2)

def main():
    moveTheBishop()

if __name__ == "__main__":
    main()