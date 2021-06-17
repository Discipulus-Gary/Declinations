import random

def decline(i, j, k, l):
    if i == 0:
        stem = nouns[i][j][1][:-2]
        declinations = [[[nouns[i][j][0]], [stem + 'ae']],
                        [[nouns[i][j][1]], [stem + 'arum']],
                        [[stem + 'ae'],    [stem + 'is']],
                        [[stem + 'am'],    [stem + 'as']],
                        [[stem + 'a'],     [stem + 'is']]]
        return declinations[k][l]
    if i == 1:
        stem = nouns[i][j][1][:-1]
        declinations = [[[nouns[i][j][0]], [stem + 'i']],
                        [[nouns[i][j][1]], [stem + 'orum']],
                        [[stem + 'o'],     [stem + 'is']],
                        [[stem + 'um'],    [stem + 'os']],
                        [[stem + 'o'],     [stem + 'is']]]
        return declinations[k][l]
    if i == 2:
        stem = nouns[i][j][1][:-1]
        declinations = [[[nouns[i][j][0]], [stem + 'a']],
                        [[nouns[i][j][1]], [stem + 'orum']],
                        [[stem + 'o'],     [stem + 'is']],
                        [[stem + 'um'],    [stem + 'a']],
                        [[stem + 'o'],     [stem + 'is']]]
        return declinations[k][l]
    if i == 3:
        stem = nouns[i][j][1][:-2]
        declinations = [[[nouns[i][j][0]], [stem + 'es']],
                        [[nouns[i][j][1]], [stem + 'um']],
                        [[stem + 'i'],     [stem + 'ibus']],
                        [[stem + 'em'],    [stem + 'es']],
                        [[stem + 'e'],     [stem + 'ibus']]]
        return declinations[k][l]
    if i == 4:
        stem = nouns[i][j][1][:-2]
        declinations = [[[nouns[i][j][0]], [stem + 'a']],
                        [[nouns[i][j][1]], [stem + 'um']],
                        [[stem + 'i'],     [stem + 'ibus']],
                        [[nouns[i][j][0]], [stem + 'a']],
                        [[stem + 'e'],     [stem + 'ibus']]]
        return declinations[k][l]
    if i == 5:
        stem = nouns[i][j][1][:-2]
        declinations = [[[nouns[i][j][0]],           [stem + 'es']],
                        [[nouns[i][j][1]],           [stem + 'ium']],
                        [[stem + 'i'],               [stem + 'ibus']],
                        [[stem + 'em', stem + 'im'], [stem + 'es', stem + 'is']],
                        [[stem + 'e', stem + 'i'],   [stem + 'ibus']]]
        return declinations[k][l]
    if i == 6:
        stem = nouns[i][j][1][:-2]
        declinations = [[[nouns[i][j][0]], [stem + 'ia']],
                        [[nouns[i][j][1]], [stem + 'ium']],
                        [[stem + 'i'],     [stem + 'ibus']],
                        [[nouns[i][j][0]], [stem + 'ia']],
                        [[stem + 'i'],     [stem + 'ibus']]]
        return declinations[k][l]
    if i == 7:
        stem = nouns[i][j][1][:-2]
        declinations = [[[nouns[i][j][0]], [stem + 'es']],
                        [[nouns[i][j][1]],  [stem + 'ium']],
                        [[stem + 'i'],      [stem + 'ibus']],
                        [[stem + 'em'],     [stem + 'es', stem + 'is']],
                        [[stem + 'e'],      [stem + 'ibus']]]
        return declinations[k][l]
    if i == 8:
        stem = nouns[i][j][1][:-2]
        declinations = [[[nouns[i][j][0]], [stem + 'us']],
                        [[nouns[i][j][1]], [stem + 'uum']],
                        [[stem + 'ui'],    [stem + 'ibus']],
                        [[stem + 'um'],    [stem + 'us']],
                        [[stem + 'u'],     [stem + 'ibus']]]
        return declinations[k][l]
    if i == 9:
        stem = nouns[i][j][1][:-2]
        declinations = [[[nouns[i][j][0]], [stem + 'ua']],
                        [[nouns[i][j][1]], [stem + 'uum']],
                        [[stem + 'u'],     [stem + 'ibus']],
                        [[stem + 'u'],     [stem + 'ua']],
                        [[stem + 'u'],     [stem + 'ibus']]]
        return declinations[k][l]
    stem = nouns[i][j][1][:-2]
    declinations = [[[nouns[i][j][0]], [stem + 'es']],
                    [[nouns[i][j][1]], [stem + 'erum']],
                    [[stem + 'ei'],    [stem + 'ebus']],
                    [[stem + 'em'],    [stem + 'es']],
                    [[stem + 'e'],     [stem + 'ebus']]]
    return declinations[k][l]

files = ['first.txt', 'second_MF.txt', 'second_N.txt', 'third_consonantal_MF.txt', 'third_consonantal_N.txt', 'third_i_MF.txt', 'third_i_N.txt', 'third_mixed.txt', 'fourth_MF.txt', 'fourth_N.txt', 'fifth.txt']

nouns = []

for i in range(len(files)):
    file = open(files[i], 'r')
    nouns.append([])
    for noun in file:
        nouns[i].append(noun.split())
    file.close()

declension = ['first declension', 'second declension masculine/feminine', 'second declension neuter', 'third declension consonantal-stem masculine/feminine', 'third declension consonantal-stem neuter', 'third declension i-stem masculine/feminine', 'third declension i-stem neuter', 'third declension mixed-i-stem', 'fourth declension masculine/feminine', 'fourth declension neuter', 'fifth declension']
case = ['nominative', 'genitive', 'dative', 'accusative', 'ablative']
number = ['singular', 'plural']

weights = []

file = open('weights.txt', 'r')
for weight in file:
    weights.append(int(weight))
file.close()

weights.append(1)

choices = [i for i in range(len(weights))]

while True:
    choice = random.choices(choices, weights = weights)[0]

    if choice == len(choices) - 1:
        choice = random.randrange(len(choices) - 1)
    
    i = choice // 10
    j = random.randrange(len(nouns[i]))
    k = choice % 10 // 2
    l = choice % 10 % 2
    
    declinations = decline(i, j, k, l)

    _input = input(case[k] + ' ' + number[l] + ' of ' + nouns[i][j][0] + ', ' + nouns[i][j][1] + ' ' + nouns[i][j][2] + ': ')

    while _input == 'R':
        for m in range(len(weights) - 1):
            weights[m] = 1
        file = open('weights.txt', 'w')
        for m in range(len(weights) - 1):
            file.write(str(weights[m]) + '\n')
        file.close()
        _input = input(case[k] + ' ' + number[l] + ' of ' + nouns[i][j][0] + ', ' + nouns[i][j][1] + ' ' + nouns[i][j][2] + ': ')

    if _input in declinations:
        weights[choice] = max(weights[choice] - 1, 0)
        print('Correct!')
    else:
        weights[choice] += 1
        print('Incorrect!')

    file = open('weights.txt', 'w')
    for m in range(len(weights) - 1):
        file.write(str(weights[m]) + '\n')
    file.close()
    
    print(case[k] + ' ' + number[l] + ' of ' + nouns[i][j][0] + ', ' + nouns[i][j][1] + ' ' + nouns[i][j][2] + ' (' + declension[i] + '):')

    for declination in declinations:
        print(declination)

    print()
