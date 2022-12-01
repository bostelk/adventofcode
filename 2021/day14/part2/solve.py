"""
DAY 14
PART 1
"""
import sys
template = None
insertion_rules = {}
insertion_rules_1 = {}
filename = sys.argv[1]
with open(filename, 'r') as file:
    line = file.readline()
    while line:
        if not template:
            template = line.strip()
            line = file.readline()
            line = file.readline()
        insertion_rule = map(lambda x: x.strip(), line.strip().split('->'))
        insertion_rules[insertion_rule[0]] = insertion_rule[1]
        insertion_rules_1[insertion_rule[0]] = [insertion_rule[0][0] + insertion_rule[1],insertion_rule[1] +insertion_rule[0][1]]
        line = file.readline()
    print("End of input")
def split_pairs(template):
    pairs = []
    for i in range(0, len(template)-1):
        pair = template[i] + template[i+1]
        pairs.append(pair)
    return pairs
def count_elements(template):
    count = {}
    for c in template:
        if c not in count:
            count[c] = 1
        else:
            count[c] += 1
    return count
def insert_pair(occurance, pair, count=1):
    if pair in occurance:
        occurance[pair] += count
    else:
        occurance[pair] = count
def insert_pairs(occurance, pairs, count=1):
    for i in range(0, len(pairs)):
        insert_pair(occurance, pairs[i], count)
count = count_elements(template)
pairs_to_occurance = {} # the number of times a pair occurs
pairs_to_count = split_pairs(template)
insert_pairs(pairs_to_occurance, pairs_to_count)
for step in range(0, 40):
    new_pairs_to_occurance = {}
    for pair in pairs_to_occurance.keys():
        insert_element = insertion_rules[pair]
        if insert_element in count:
            count[insert_element] += pairs_to_occurance[pair]
        else:
            count[insert_element] = pairs_to_occurance[pair]
        insert_pairs(new_pairs_to_occurance, insertion_rules_1[pair], pairs_to_occurance[pair])
    pairs_to_occurance = new_pairs_to_occurance
count = sorted(count.items(), key=lambda x: x[1])
least_common = count[0]
most_common = count[len(count)-1]
print most_common[1] - least_common[1]
