"""
DAY 2
PART 2
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

def max_color_amount(game, color):
    max_amount = 0
    for subset in game['subsets']:
        if color in subset and subset[color] > max_amount:
            max_amount = subset[color]
    return max_amount

g_power_sum = 0

with open(filename, 'r') as file:
    line = file.readline()
    while line:
        # Remove newline char.
        if line[len(line) - 1] == '\n':
            line = line[:-1]

        game = parse_game(line)

        max_color_amounts = {
            'red': max_color_amount(game, 'red'),
            'blue': max_color_amount(game, 'blue'),
            'green': max_color_amount(game, 'green')
        }
        power = max_color_amounts['red'] * max_color_amounts['blue'] * max_color_amounts['green']
        g_power_sum += power

        line = file.readline()

    print("sum of power sets: " + str(g_power_sum))
    print("End of input")
