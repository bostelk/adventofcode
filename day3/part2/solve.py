"""
DAY 3
PART 2
"""
import sys
filename = sys.argv[1]
G_BIT_MASK = 1
def most_common_bit(numbers, bit_offset):
    bit_on_count = 0
    bit_off_count = 0
    for i in range(0, len(numbers)):
        number = numbers[i]
        if number >> bit_offset & G_BIT_MASK == G_BIT_MASK:
            bit_on_count += 1
        else:
            bit_off_count += 1
    return bit_on_count >= bit_off_count
def filter_common_bit_functor(bit_on, i):
    if bit_on:
        return lambda x: x >> i & G_BIT_MASK == G_BIT_MASK
    else:
        return lambda x: x >> i & G_BIT_MASK != G_BIT_MASK
def calc_rating_from_numbers(numbers, select_most_common):
    for i in reversed(range(0, num_bits)):
        common_bit_on = most_common_bit(numbers, i)
        if not select_most_common:
            common_bit_on = not common_bit_on
        numbers = filter(filter_common_bit_functor(common_bit_on, i), numbers)
        if len(numbers) == 1:
            return numbers[0]
    return None
with open(filename, 'r') as file:
    line = file.readline()
    num_bits = len(line.strip()) # strip whitespace.
    diagnostic_numbers = []
    while line:
        diagnostic_number = int(line, 2)
        diagnostic_numbers.append(diagnostic_number)
        line = file.readline()
    oxygen_generator_rating = calc_rating_from_numbers(list(diagnostic_numbers), select_most_common=True)
    c02_scrubber_rating = calc_rating_from_numbers(list(diagnostic_numbers), select_most_common=False)
    life_support_rating = oxygen_generator_rating * c02_scrubber_rating
    print("oxygen generator rating * c02 scrubber rating = life support rating")
    print("= %s * %s = %s" % (oxygen_generator_rating, c02_scrubber_rating, life_support_rating))
    print("End of input")
