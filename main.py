from test.snils import generateSnils as GS
from test.snils import replaceInText as RT


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')
    print(GS())
    txt = '''This is the
text with a #{element} to be
replaced with another element
    '''
    print(RT(txt, '#{element}', 'simple element'))

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
