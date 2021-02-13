import math
import random

def generateSnils():
    # rnd = math.floor(math)
    number = str(random.randrange(1001998, 999999999, 1)).rjust(9, '0')
    numbers = [[char, i] for i, char in enumerate(number)]
    chk = sum(list(map(lambda x: int(x[0]) * (9 - x[1]), numbers)))
    if chk > 101:
        chk = chk % 101
    chkSum = ''
    if chk == 100 or chk == 101:
        chkSum = '00'
    else:
        chkSum = str(chk).rjust(2, '0')
    # TODO сделать возврат двух форматов снилс, через дефис и через пробел
    return [number, chkSum]