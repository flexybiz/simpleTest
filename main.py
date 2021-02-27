from test.snils import generate_snils as GS
from test.snils import replace_in_text as RT
from test.snils import generate_guid as GUID
from test.snils import make_mzmk_mother as MMZMK
from test.snils import info_from_emu as IFE
from test.snils import send_to_emu as STE


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
    print(GUID())
    MMZMK()
    IFE()
    STE()
