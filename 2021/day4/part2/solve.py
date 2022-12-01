"""
DAY 4
PART 2
"""
import sys
def read_input(filename, board_dim):
    with open(filename, 'r') as file:
        line = file.readline()
        # the order in which the numbers are drawn
        draw = map(lambda p: int(p), line.rstrip().split(","))
        # an array of bingo boards
        boards = []
        while line:
            rows = []
            line = file.readline()
            if line:
                for i in range(0, board_dim):
                    line = file.readline()
                    parts = line.rstrip().split()
                    rows.append(map(lambda p: int(p), parts))
                boards.append(rows)
        print("End of input")
    return draw, boards
def board_intersection_drawn(board, board_dim, drawn_set):
    for row in range(0, board_dim):
        row_set = set(board[row])
        if row_set.intersection(drawn_set) == row_set:
            return "row", row
    for col in range(0, board_dim):
        col_set = set()
        for row in range(0, board_dim):
            col_set.add(board[row][col])
        if col_set.intersection(drawn_set) == col_set:
            return "col", col
    return None, None
def sum_not_drawn_numbers(board, board_dim, drawn_set):
    numbers_set = set()
    for row in range(0, board_dim):
        for col in range(0, board_dim):
            numbers_set.add(board[row][col])
    not_drawn_numbers = numbers_set.difference(drawn_set)
    return sum(not_drawn_numbers)
filename = sys.argv[1]
board_dim = 5 # board is square
draw, boards = read_input(filename, board_dim)
drawn_set = set()
winner_set = set()
for i in range(0, len(draw)):
    number = draw[i]
    drawn_set.add(number)
    # check for winner
    if i > board_dim - 1:
        for b in range(0, len(boards)):
            row_or_col_name, row_or_col = board_intersection_drawn(boards[b], board_dim, drawn_set)
            if row_or_col_name is not None:
                print("Board %s wins. Winning number is %s. Winning %s is %s." % (b+1, number, row_or_col_name, row_or_col))
                not_drawn_numbers_sum = sum_not_drawn_numbers(boards[b], board_dim, drawn_set)
                final_score = not_drawn_numbers_sum * number
                print("Final score is %s." % final_score)
                winner_set.add(b)
            if len(winner_set) == len(boards):
                break
        if len(winner_set) == len(boards):
            break
