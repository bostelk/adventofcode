"""
DAY 3
PART 1
"""
import sys
filename = sys.argv[1]
G_BIT_MASK = 1
with open(filename, 'r') as file:
    line = file.readline()
    num_bits = len(line.strip()) # strip whitespace.
    bit_on_count = [0] * num_bits
    bit_off_count = [0] * num_bits
    while line:
        diagnostic_number = int(line, 2)
        for i in range(0, num_bits):
            if diagnostic_number >> i & G_BIT_MASK == G_BIT_MASK:
                bit_on_count[i] += 1
            else:
                bit_off_count[i] += 1
        line = file.readline()
    gamma_rate = 0
    epsilon_rate = 0
    for i in range(0, num_bits):
        if (bit_on_count[i] > bit_off_count[i]):
            gamma_rate |= G_BIT_MASK << i
        else:
            epsilon_rate |= G_BIT_MASK << i
    power_consumption = gamma_rate * epsilon_rate
    print("gamma rate * epsilon rate = power consumption")
    print("= %s * %s = %s" % (gamma_rate, epsilon_rate, power_consumption))
    print("End of input")
