"""
DAY 2
PART 1
"""
import sys
import re

filename = sys.argv[1]

def parse_game(line):
    result = {}

    parts = line.split(':')

    game = parts[:1][0]
    _, game_id = game.split(' ')
    result['id'] = int(game_id)

    subsets = parts[1:][0]
    subsets = subsets.split(';')

    result['subsets'] = []
    for subset in subsets:
        result_subset = {}
        cubes = subset.split(',')
        for cube in cubes:
            count, color = cube.strip().split(' ')
            result_subset[color] = int(count)
        result['subsets'].append(result_subset)
    return result

def validate_color_amount(game, color, count):
    for subset in game['subsets']:
        if color in subset and subset[color] > count:
            return False
    return True

g_valid_game_count = 0

with open(filename, 'r') as file:
    line = file.readline()
    while line:
        # Remove newline char.
        if line[len(line) - 1] == '\n':
            line = line[:-1]

        game = parse_game(line)

        if not validate_color_amount(game, 'red', 12):
            print("game is invalid; too many red cubes")
        elif not validate_color_amount(game, 'green', 13):
            print("game is invalid; too many green cubes")
        elif not validate_color_amount(game, 'blue', 14):
            print("game is invalid; too many blue cubes")
        else:
            g_valid_game_count += game['id']

        line = file.readline()

    print("sum of valid game ids: " + str(g_valid_game_count))
    print("End of input")
