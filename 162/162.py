import sys

def beggarMyNeighbour():
    while True:
        line = sys.stdin.readline().strip()
        if line == "#":
            break
        deck = []
        for i in range(4):
            cards = line.split(' ')
            for j in range(13):
                deck.append(cards[j])
            if i != 3:
                line = sys.stdin.readline().strip()

        deck1 = [] # osztó paklija
        deck2 = [] # első játékos paklija

        for d in range(0, 52, 2):
            deck2.append(deck[d])
            deck1.append(deck[d+1])

        deck1.reverse()
        deck2.reverse()
        decks = [[], deck1, deck2]
        flag = 2 # melyik játékos van soron
        heap = []
        facecards = ['J', 'Q', 'K', 'A']
        punishment = 0
        facecard = False
        while True:
            if facecard:
                decks[flag].extend(heap)
                heap = []
                facecard = False
            if len(decks[flag]) == 0:
                flag = 3 - flag
                print("{}{:>3}".format(flag, len(decks[flag])))
                break
            card = decks[flag][0]
            heap.append(card)
            decks[flag] = decks[flag][1:]
            if punishment > 0:
                punishment -= 1
                if punishment == 0 and card[1] not in facecards:
                    facecard = True
            if card[1] in facecards:
                punishment = facecards.index(card[1]) + 1
                flag = 3 - flag
            elif punishment == 0:
                flag = 3 - flag


def main():
    beggarMyNeighbour()

if __name__ == "__main__":
    main()