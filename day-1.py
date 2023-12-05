import sys
import re

filename = sys.argv[1]

data = []
calc = 0
with open(filename) as f:
    for line in f.readlines():
        line = line.rstrip()
        data.append(line)
        num = 0
        try:
            num = int(f"{re.search('[1-9]', line).group(0)}{re.search('[1-9]', line[::-1]).group(0)}")
        except:
            pass
        calc = calc + int(num)
f.close()
print(calc)

# -------

calc   = 0
digits = [
    '---',
    'one',
    'two',
    'three',
    'four',
    'five',
    'six',
    'seven',
    'eight',
    'nine',
]

dr = digits[1:].join("|")

for d in data:
    line = d
    #for i in range(1,10):
    #    line = re.sub(digits[i], str(i), line)
    num = int(f"{re.search('[1-9]', line).group(0)}{re.search('[1-9]', line[::-1]).group(0)}")
    calc = calc + int(num)
    print(d, line, num)

print(calc)
