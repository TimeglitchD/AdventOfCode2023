import re

# Find digits written out

class ContinueI(Exception):
    pass

cubes = {'red' : 12, 'green': 13, 'blue': 14}

continue_i = ContinueI(Exception("Impossible game"))

total = 0

with open('Day02.txt', 'r') as file:
    lines = file.readlines()
    for line in lines:
        try:
            line = line.strip()
            id = line[line.find(' ')+1:line.find(':')]
            gameString = line[line.find(':')+2:]
            game = gameString.split(';')
            for handful in game:
                cubesResult = {'red' : 0, 'green': 0, 'blue': 0}
                handful = handful.strip()
                pairs = handful.split(',')
                for pair in pairs:
                    pair = pair.strip()
                    amount = pair[:pair.find(' ')]
                    color = pair[pair.find(' ')+1:]
                    cubesResult[color] += int(amount)
                if cubesResult['red'] > cubes['red'] or cubesResult['green']  > cubes['green'] or cubesResult['blue']  > cubes['blue']:
                    raise continue_i
        except ContinueI:
            continue

        total += int(id)


print(f"The total is: {total}")

total = 0

with open('Day02.txt', 'r') as file:
    lines = file.readlines()
    for line in lines:
        line = line.strip()
        id = line[line.find(' ')+1:line.find(':')]
        gameString = line[line.find(':')+2:]
        game = gameString.split(';')
        cubesGame = {'red' : 0, 'green': 0, 'blue': 0}
        for handful in game:
            cubesHandful = {'red' : 0, 'green': 0, 'blue': 0}
            handful = handful.strip()
            pairs = handful.split(',')
            for pair in pairs:
                pair = pair.strip()
                amount = pair[:pair.find(' ')]
                color = pair[pair.find(' ')+1:]
                cubesHandful[color] += int(amount)

            for color in cubesHandful:
                cubesGame[color] = max(cubesGame[color], cubesHandful[color])


        total += cubesGame['red'] * cubesGame['green'] * cubesGame['blue']


print(f"The total is: {total}")





