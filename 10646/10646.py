import sys

def whatIsTheCard():
    T = int(sys.stdin.readline().strip())
    for t in range(T):
        cards = sys.stdin.readline().strip()
        cards = cards.split(" ")
        hand = cards[27:52]
        deck = cards[:27]
        Y = 0
        for i in range(3):
            if deck[len(deck)-1][0] in ["T", "J", "Q", "K", "A"]:
                X = 10
            else:
                X = int(deck[len(deck)-1][0])
            Y += X
            deck = deck[:len(deck)-1-(10-X)]
        deck += hand
        print("Case {}: {}".format(t+1, deck[Y-1]))


def main():
    whatIsTheCard()

if __name__ == "__main__":
    main()