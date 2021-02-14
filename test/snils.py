import random
import re
import uuid


def guid():
    return str(uuid.uuid4())


def makeMZMKMother():
    snils = generateSnils()
    uid = guid()
    infile = open('test/data/МЗМКмать.xml', mode='r', encoding='utf-8')
    intext = infile.read()
    infile.close()
    intext = replaceInText(intext, '#{snils}', snils[2])
    intext = replaceInText(intext, '#{guid}', uid)
    outfile = open('F:/mzmk_mother.xml', mode='w', encoding='utf-8')
    outfile.write(intext)
    outfile.close()


def replaceInText(text, inp, to):
    out = ''
    for line in text.split('\n'):
        out += line.replace(inp, to) + '\n'
    return out


def cut_text(text, lenth):
    textArr = re.findall('.{'+str(lenth)+'}', text)
    return textArr


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
    # Возвращает снилс в 3ёх видах ХХХХХХХХХХХХ , ХХХ ХХХ ХХХ ХХ ,  ХХХ-ХХХ-ХХХ ХХ
    return [number + chkSum, ' '.join(cut_text(number, 3)) + ' ' + chkSum, '-'.join(cut_text(number, 3)) + ' ' + chkSum]