import sys

def palindrome():
    punctuation = [" ", ",", ".", "?", "!", "(", ")", "[", "]", "{", "}"]
    squares = []
    for i in range(101):
        squares.append(i*i)
    T = int(sys.stdin.readline().strip())
    for t in range(T):
        print("Case #{}:".format(t + 1))
        phrase = sys.stdin.readline().strip()
        for ch in phrase:
            if ch in punctuation:
                phrase = phrase[0:phrase.index(ch)]+phrase[phrase.index(ch)+1:len(phrase)]
        phrase = phrase.lower()
        L = len(phrase)
        if L not in squares:
            print("No magic :(")
            continue
        K = squares.index(L)

        # visszafelé:
        revphrase = ""
        for rev in range(L, 0, -1):
            revphrase += phrase[rev-1]

        # függőlegesen:
        vertphrase = ""
        revvertphrase = ""
        for i in range(K):
            for j in range(K):
                vertphrase += phrase[j*K+i]
                revvertphrase += revphrase[j*K+i]
        if revphrase == phrase and vertphrase == phrase and revvertphrase == phrase:
            print(K)
        else:
            print("No magic :(")
def main():
    palindrome()

if __name__ == "__main__":
    main()