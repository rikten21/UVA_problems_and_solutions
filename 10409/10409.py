import sys

def dieGame():
    while True:
        C = int(sys.stdin.readline().strip())
        if C == 0:
            break
        die = [1, 2, 4, 5, 3, 6] # top n e s w bottom
        for c in range(C):
            command = sys.stdin.readline().strip()
            tmp = die.copy()
            if command == "north":
                die[0] = tmp[3]
                die[1] = tmp[0]
                die[3] = tmp[5]
                die[5] = tmp[1]
            elif command == "east":
                die[0] = tmp[4]
                die[2] = tmp[0]
                die[4] = tmp[5]
                die[5] = tmp[2]
            elif command == "south":
                die[0] = tmp[1]
                die[1] = tmp[5]
                die[3] = tmp[0]
                die[5] = tmp[3]
            elif command == "west":
                die[0] = tmp[2]
                die[2] = tmp[5]
                die[4] = tmp[0]
                die[5] = tmp[4]
        print(die[0])

def main():
    dieGame()

if __name__ == "__main__":
    main()