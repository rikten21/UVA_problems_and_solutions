import sys

def chessboardFEN():
    pieces = ["p", "n", "b", "r", "q", "k"]
    while True:
        line = sys.stdin.readline().strip()
        if line == "":
            break
        rows = line.split('/')
        table = []
        answer = []
        for i in range(64):
            table.append(0)
            answer.append(0)
        for b in range(8):
            squares = 0
            for square in range(len(rows[b])):
                if rows[b][square].lower() in pieces:
                    squares += 1
                    if rows[b][square].lower() == "p": # mert a gyalognál számít, hogy fekete vagy fehér
                        table[b * 8 + squares - 1] = rows[b][square]
                        answer[b*8 + squares-1] = 1
                    else:
                        table[b*8 + squares -1 ] = rows[b][square].lower()
                        answer[b * 8 + squares - 1] = 1
                else:
                    squares += int(rows[b][square])
        for r in range(8):
            for c in range(8):
                if table[r*8 + c] == 0:
                    if figures(table, r, c):
                        answer[r * 8 + c] = 1
                    elif knight(table, r, c):
                        answer[r * 8 + c] = 1
        count = 0
        for a in range(64):
            if answer[a] == 0:
                count += 1
        print(count)


def knight(table, row, column):
    for i in range(1, 3):
        if (row - i) >= 0 and (column - (3 - i)) >= 0 and table[(row - i) * 8 + column - (3 - i)] == "n":
            return True
        if (row + i) < 8 and (column + (3 - i)) < 8 and table[(row + i) * 8 + column + (3 - i)] == "n":
            return True
        if (row - i) >= 0 and (column + (3 - i)) < 8 and table[(row - i) * 8 + column + (3 - i)] == "n":
            return True
        if (row + i) < 8 and (column - (3 - i)) >= 0 and table[(row + i) * 8 + column - (3 - i)] == "n":
            return True
    return False

def figures(table, row, column):
    rowtmp = row + 1
    columntmp = column
    while rowtmp < 8 and table[rowtmp * 8 + columntmp] == 0:
        rowtmp += 1
    if rowtmp < 8 and (table[rowtmp*8 + columntmp] == "q" or table[rowtmp*8 + columntmp] == "r" or (abs(rowtmp-row) == 1 and table[rowtmp*8 + columntmp] == "k")):
        return True

    rowtmp = row - 1
    columntmp = column
    while rowtmp >= 0 and table[rowtmp * 8 + columntmp] == 0:
        rowtmp -= 1
    if rowtmp >= 0 and (table[rowtmp * 8 + columntmp] == "q" or table[rowtmp * 8 + columntmp] == "r" or (
            abs(rowtmp - row) == 1 and table[rowtmp * 8 + columntmp] == "k")):
        return True

    rowtmp = row
    columntmp = column + 1
    while columntmp < 8 and table[rowtmp * 8 + columntmp] == 0:
        columntmp += 1
    if columntmp < 8 and (table[rowtmp * 8 + columntmp] == "q" or table[rowtmp * 8 + columntmp] == "r" or (
            abs(columntmp - column) == 1 and table[rowtmp * 8 + columntmp] == "k")):
        return True

    rowtmp = row
    columntmp = column - 1
    while columntmp >= 0 and table[rowtmp * 8 + columntmp] == 0:
        columntmp -= 1
    if columntmp >= 0 and (table[rowtmp * 8 + columntmp] == "q" or table[rowtmp * 8 + columntmp] == "r" or (
            abs(columntmp - column) == 1 and table[rowtmp * 8 + columntmp] == "k")):
        return True

    rowtmp = row - 1
    columntmp = column - 1
    while columntmp >= 0 and rowtmp >= 0 and table[rowtmp * 8 + columntmp] == 0:
        rowtmp -= 1
        columntmp -= 1
    if rowtmp >= 0 and columntmp >= 0 and (table[rowtmp * 8 + columntmp] == "q" or table[rowtmp * 8 + columntmp] == "b" or (
            abs(columntmp - column) == 1 and abs(rowtmp - row) == 1 and (table[rowtmp * 8 + columntmp] == "k" or table[rowtmp * 8 + columntmp] == "p"))):
        return True

    rowtmp = row - 1
    columntmp = column + 1
    while columntmp < 8 and rowtmp >= 0 and table[rowtmp * 8 + columntmp] == 0:
        rowtmp -= 1
        columntmp += 1
    if rowtmp >= 0 and columntmp < 8 and (table[rowtmp * 8 + columntmp] == "q" or table[rowtmp * 8 + columntmp] == "b" or (
            abs(columntmp - column) == 1 and abs(rowtmp - row) == 1 and (table[rowtmp * 8 + columntmp] == "k" or table[rowtmp * 8 + columntmp] == "p"))):
        return True

    rowtmp = row + 1
    columntmp = column + 1
    while columntmp < 8 and rowtmp < 8 and table[rowtmp * 8 + columntmp] == 0:
        rowtmp += 1
        columntmp += 1
    if rowtmp < 8 and columntmp < 8 and (table[rowtmp * 8 + columntmp] == "q" or table[rowtmp * 8 + columntmp] == "b" or (
            abs(columntmp - column) == 1 and abs(rowtmp - row) == 1 and (table[rowtmp * 8 + columntmp] == "k" or table[rowtmp * 8 + columntmp] == "P"))):
        return True

    rowtmp = row + 1
    columntmp = column - 1
    while columntmp >= 0 and rowtmp < 8 and table[rowtmp * 8 + columntmp] == 0:
        rowtmp += 1
        columntmp -= 1
    if rowtmp < 8 and columntmp >= 0 and (table[rowtmp * 8 + columntmp] == "q" or table[rowtmp * 8 + columntmp] == "b" or (
            abs(columntmp - column) == 1 and abs(rowtmp - row) == 1 and (table[rowtmp * 8 + columntmp] == "k" or table[rowtmp * 8 + columntmp] == "P"))):
        return True

    return False

def main():
    chessboardFEN()

if __name__ == "__main__":
    main()