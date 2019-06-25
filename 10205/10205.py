import sys

def crooked():
    C = int(sys.stdin.readline().strip())
    sys.stdin.readline()
    for c in range(C):
        if c > 0:
            print()
        cards = [[], "2 of Clubs", "3 of Clubs", "4 of Clubs", "5 of Clubs", "6 of Clubs", "7 of Clubs", "8 of Clubs",
                 "9 of Clubs", "10 of Clubs", "Jack of Clubs", "Queen of Clubs", "King of Clubs", "Ace of Clubs",
                 "2 of Diamonds", "3 of Diamonds", "4 of Diamonds", "5 of Diamonds", "6 of Diamonds", "7 of Diamonds",
                 "8 of Diamonds",
                 "9 of Diamonds", "10 of Diamonds", "Jack of Diamonds", "Queen of Diamonds", "King of Diamonds",
                 "Ace of Diamonds",
                 "2 of Hearts", "3 of Hearts", "4 of Hearts", "5 of Hearts", "6 of Hearts", "7 of Hearts",
                 "8 of Hearts",
                 "9 of Hearts", "10 of Hearts", "Jack of Hearts", "Queen of Hearts", "King of Hearts", "Ace of Hearts",
                 "2 of Spades", "3 of Spades", "4 of Spades", "5 of Spades", "6 of Spades", "7 of Spades",
                 "8 of Spades",
                 "9 of Spades", "10 of Spades", "Jack of Spades", "Queen of Spades", "King of Spades", "Ace of Spades"]
        n = int(sys.stdin.readline().strip())
        shuffles = [[]]
        shufflecard = []
        while True:
            if len(shufflecard) == n*52:
                break
            line = sys.stdin.readline().strip()
            line = [int(i) for i in line.split(" ")]
            shufflecard.extend(line)
        for i in range(n):
            shuffles.append([0])
            shuffles[i+1].extend(shufflecard[i*52:(i+1)*52])
        while True:
            shuf = sys.stdin.readline().strip()
            if not shuf or shuf == "":
                break
            tmpdeck = cards.copy()
            for k in range(1, 53):
                cards[k] = tmpdeck[shuffles[int(shuf)][k]]
        for card in range(1, 53):
            print(cards[card])


def main():
    crooked()

if __name__ == "__main__":
    main()