from collections import Counter

def processList(inList):
    return [(len(group.split('\n')), Counter(group.replace('\n', ''))) for group in inList.split('\n\n')]

with open('input', 'r') as inputs:
    groups = processList(inputs.read())

print('P1 SOLUTION: ', sum(map(lambda group: len(group[1]), groups)))
print('P2 SOLUTION: ', sum(map(lambda group: sum([group[0] == group[1][question] for question in group[1]]), groups)))
