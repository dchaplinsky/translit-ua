# -*- coding: utf-8 -*-
import re

_MAIN_TRANSLIT_TABLE = {
    u"а": u"a",
    u"б": u"b",
    u"в": u"v",
    u"г": u"h",
    u"ґ": u"g",
    u"д": u"d",
    u"е": u"e",
    u"є": u"ie",
    u"ж": u"zh",
    u"з": u"z",
    u"и": u"y",
    u"і": u"i",
    u"ї": u"i",
    u"й": u"i",
    u"к": u"k",
    u"л": u"l",
    u"м": u"m",
    u"н": u"n",
    u"о": u"o",
    u"п": u"p",
    u"р": u"r",
    u"с": u"s",
    u"т": u"t",
    u"у": u"u",
    u"ф": u"f",
    u"х": u"kh",
    u"ц": u"ts",
    u"ч": u"ch",
    u"ш": u"sh",
    u"щ": u"shch",
    u"ь": u"",
    u"ю": u"iu",
    u"я": u"ia",
    u"'": u""
}

_SPECIAL_CASES = {
    u"зг": u"zgh",
    u"ЗГ": u"ZGh",
}

_FIRST_CHARACTERS = {
    u"є": u"ye",
    u"ї": u"yi",
    u"й": u"y",
    u"ю": u"yu",
    u"я": u"ya"
}


def add_uppercase(table):
    orig = table.copy()
    orig.update(
        dict((k.capitalize(), v.capitalize()) for k, v in table.iteritems()))

    return orig


def convert_table(table):
    return dict((ord(k), v) for k, v in table.iteritems())


MAIN_TRANSLIT_TABLE = convert_table(add_uppercase(_MAIN_TRANSLIT_TABLE))
FIRST_CHARACTERS = add_uppercase(_FIRST_CHARACTERS)
SPECIAL_CASES = add_uppercase(_SPECIAL_CASES)


def translit_ukr(src):
    """
    """
    pattern1 = re.compile(u"(?mu)" + u'|'.join(re.escape(key)
                          for key in SPECIAL_CASES.keys()))
    src = pattern1.sub(lambda x: SPECIAL_CASES[x.group()], src)

    pattern2 = re.compile(u"(?mu)" + r"\b(" + u'|'.join(re.escape(key)
                          for key in FIRST_CHARACTERS.keys()) + u")")

    src = pattern2.sub(lambda x: FIRST_CHARACTERS[x.group()], src)
    return src.translate(MAIN_TRANSLIT_TABLE)

__all__ = ["translit_ukr"]


if __name__ == '__main__':
    print(translit_ukr(u"Дмитро Згуровский"))
    print(translit_ukr(u"Дмитро ЗГуровский"))
    print(translit_ukr(u"Дмитро згуровский"))

    print(translit_ukr(u"Євген Петренко"))
    print(translit_ukr(u"Петренко Євген"))
    print(translit_ukr(u"Петренко.Євген"))
    print(translit_ukr(u"Петренко,Євген"))
    print(translit_ukr(u"Петренко/Євген"))
    print(translit_ukr(u"Євгєн"))
