# -*- coding: utf-8 -*-
import re
import sys

if sys.version < '3':
    text_type = unicode
else:
    text_type = str

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
        dict((k.capitalize(), v.capitalize()) for k, v in table.items()))

    return orig


def convert_table(table):
    return dict((ord(k), v) for k, v in table.items())


MAIN_TRANSLIT_TABLE = convert_table(add_uppercase(_MAIN_TRANSLIT_TABLE))
FIRST_CHARACTERS = add_uppercase(_FIRST_CHARACTERS)
SPECIAL_CASES = add_uppercase(_SPECIAL_CASES)

PATTERN1 = re.compile(u"(?mu)" + u'|'.join(SPECIAL_CASES.keys()))
PATTERN2 = re.compile(u"(?mu)" + r"\b(" +
                      u'|'.join(FIRST_CHARACTERS.keys()) + u")")


def translitua(src):
    u""" Transliterates given ukrainian unicode `src` text
    to officially transliterated variant.

    >>> print(translitua(u"Дмитро Згуровский"))
    Dmytro Zghurovskyi
    >>> print(translitua(u"Дмитро ЗГуровский"))
    Dmytro ZGhurovskyi
    >>> print(translitua(u"Дмитро згуровский"))
    Dmytro zghurovskyi
    >>> print(translitua(u"Євген Петренко"))
    Yevhen Petrenko
    >>> print(translitua(u"Петренко Євген"))
    Petrenko Yevhen
    >>> print(translitua(u"Петренко.Євген"))
    Petrenko.Yevhen
    >>> print(translitua(u"Петренко,Євген"))
    Petrenko,Yevhen
    >>> print(translitua(u"Петренко/Євген"))
    Petrenko/Yevhen
    >>> print(translitua(u"Євгєн"))
    Yevhien
    """

    src = text_type(src)

    src = PATTERN1.sub(lambda x: SPECIAL_CASES[x.group()], src)
    src = PATTERN2.sub(lambda x: FIRST_CHARACTERS[x.group()], src)
    return src.translate(MAIN_TRANSLIT_TABLE)

__all__ = ["translitua"]


if __name__ == '__main__':
    import doctest
    doctest.testmod()
