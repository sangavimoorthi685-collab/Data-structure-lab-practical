def solve(row, n, columns, diagonal1, diagonal2, board):
    if row == n:
        print(board)
        return

    for col in range(n):
        if col not in columns and row - col not in diagonal1 and row + col not in diagonal2:

            board.append(col)

            columns.add(col)
            diagonal1.add(row - col)
            diagonal2.add(row + col)

            solve(row + 1, n, columns, diagonal1, diagonal2, board)

            board.pop()
            columns.remove(col)
            diagonal1.remove(row - col)
            diagonal2.remove(row + col)


n = int(input("Enter N: "))

solve(0, n, set(), set(), set(), [])