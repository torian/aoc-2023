import sys
import re
import operator
from functools import reduce

filename = sys.argv[1]
data = []

game_sum   = 0
game_power = 0

with open(filename) as f:
    for line in f.readlines():
        line = line.rstrip()
        data.append(line)

        game_id = int(re.search(r"[0-9]+", line.split(":")[0]).group(0))
        sets = line.split(":")[1]

        possible = True
        cubes = { "red": 0, "green": 0, "blue": 0 }
        for s in sets.split(';'):
            r = 0
            g = 0
            b = 0
            for c in s.split(','):
                if 'red' in c:
                    r = int(re.search("[0-9]+", c).group(0))
                    if r > cubes["red"]:
                        cubes["red"] = r
                if 'green' in c:
                    g = int(re.search("[0-9]+", c).group(0))
                    if g > cubes["green"]:
                        cubes["green"] = g
                if 'blue' in c:
                    b = int(re.search("[0-9]+", c).group(0))
                    if b > cubes["blue"]:
                        cubes["blue"] = b
            if r > 12 or g > 13 or b > 14:
                possible = False
                continue

        set_power  = reduce(operator.mul, cubes.values())
        game_power = game_power + set_power

        if possible:
            game_sum = game_sum + game_id

print("Game SUM:", game_sum)
print("Game Power SUM:", game_power)
