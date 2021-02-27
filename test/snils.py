import random
import re
import uuid
import requests


def info_from_emu():
    url = "http://localhost:8080/info"
    r = requests.get(url)
    assert str(r.text) == "\"rest-vio-emulator v1.0\""


def send_to_emu():
    url = "http://localhost:8080/send"
    file = open("test/data/mzmk_mother.xml", "rb").read()
    data = {'claim_type': 'MZMK', 'claim_body': file}
    r = requests.post(url, data=data)
    print(r.text)


def generate_guid():
    return str(uuid.uuid4())


def make_mzmk_mother():
    snils = generate_snils()
    guid = generate_guid()
    infile = open('test/data/mzmk_pattern.xml', mode='r', encoding='utf-8')
    intext = infile.read()
    infile.close()
    intext = replace_in_text(intext, '#{snils}', snils[2])
    intext = replace_in_text(intext, '#{guid}', guid)
    outfile = open('test/data/mzmk_mother.xml', mode='w', encoding='utf-8')
    outfile.write(intext)
    outfile.close()


def replace_in_text(text, inp, to):
    out = ''
    for line in text.split('\n'):
        out += line.replace(inp, to) + '\n'
    return out


def cut_text(text, lenth):
    textArr = re.findall('.{'+str(lenth)+'}', text)
    return textArr


def generate_snils():
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