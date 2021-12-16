"""
DAY 14
PART 1
"""
import sys
template = None
insertion_rules = {}
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
        line = file.readline()
    print("End of input")
print template
def apply_rules(template, rules):
    new_template = template[0]
    for i in range(0, len(template)-1):
        pair = template[i] + template[i+1]
        if pair in rules:
            new_template += rules[pair] + template[i+1]
        else:
            new_template += pair
    return new_template
def count_elements(template):
    count = {}
    for c in template:
        if c not in count:
            count[c] = 1
        else:
            count[c] += 1
    return count
steps = 10
print "Template: ", template
for i in range(0, steps):
    template = apply_rules(template, insertion_rules)
    print("After step %s: %s" % (i + 1, template))
count = count_elements(template)
count = sorted(count.items(), key=lambda x: x[1])
least_common = count[0]
most_common = count[len(count)-1]
print most_common[1] - least_common[1]
