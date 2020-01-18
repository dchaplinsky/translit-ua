# -*- coding: utf-8 -*-
from __future__ import unicode_literals
import re
import sys

if sys.version < '3':
    text_type = unicode
else:
    text_type = str


def add_uppercase(table):
    """
    Extend the table with uppercase options

    >>> print("а" in add_uppercase({"а": "a"}))
    True
    >>> print(add_uppercase({"а": "a"})["а"] == "a")
    True
    >>> print("А" in add_uppercase({"а": "a"}))
    True
    >>> print(add_uppercase({"а": "a"})["А"] == "A")
    True
    >>> print(len(add_uppercase({"а": "a"}).keys()))
    2
    >>> print("Аа" in add_uppercase({"аа": "aa"}))
    True
    >>> print(add_uppercase({"аа": "aa"})["Аа"] == "Aa")
    True
    """
    orig = table.copy()
    orig.update(
        dict((k.capitalize(), v.capitalize()) for k, v in table.items()))

    return orig


def convert_table(table):
    """
    >>> print(1072 in convert_table({"а": "a"}))
    True
    >>> print(1073 in convert_table({"а": "a"}))
    False
    >>> print(convert_table({"а": "a"})[1072] == "a")
    True
    >>> print(len(convert_table({"а": "a"}).keys()) == 1)
    True
    """

    return dict((ord(k), v) for k, v in table.items())


class UkrainianKMU(object):
    """
    According to National system from
    https://en.wikipedia.org/wiki/Romanization_of_Ukrainian#Tables_of_romanization_systems
    """
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
        u"ю": u"iu",
        u"я": u"ia",
    }

    _DELETE_CASES = [
        u"ь",
        u"Ь",
        u"\u0027",
        u"\u2019",
        u"\u02BC",
    ]

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

    MAIN_TRANSLIT_TABLE = convert_table(add_uppercase(_MAIN_TRANSLIT_TABLE))
    FIRST_CHARACTERS = add_uppercase(_FIRST_CHARACTERS)
    SPECIAL_CASES = add_uppercase(_SPECIAL_CASES)

    PATTERN1 = re.compile(u"(?mu)" + u'|'.join(SPECIAL_CASES.keys()))
    PATTERN2 = re.compile(u"(?mu)" + r"\b(" +
                          u'|'.join(FIRST_CHARACTERS.keys()) + u")")
    DELETE_PATTERN = re.compile(u"(?mu)" + u'|'.join(_DELETE_CASES))


class UkrainianSimple(object):
    """
    Borrowed from https://github.com/barseghyanartur/transliterate/blob/master/src/transliterate/contrib/languages/uk/data/python32.py
    by Artur Barseghyan <artur.barseghyan@gmail.com>
    """
    _MAIN_TRANSLIT_TABLE = {
        u"а": u"a",
        u"б": u"b",
        u"в": u"v",
        u"г": u"h",
        u"ґ": u"g",
        u"д": u"d",
        u"е": u"e",
        u"є": u"ye",
        u"ж": u"zh",
        u"з": u"z",
        u"и": u"y",
        u"і": u"i",
        u"ї": u"yi",
        u"й": u"j",
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
        u"ь": u"'",
        u"ю": u"ju",
        u"я": u"ja",
    }

    MAIN_TRANSLIT_TABLE = convert_table(add_uppercase(_MAIN_TRANSLIT_TABLE))


class RussianSimple(object):
    """
    Borrowed from https://github.com/barseghyanartur/transliterate/blob/master/src/transliterate/contrib/languages/ru/data/python32.py
    by Artur Barseghyan <artur.barseghyan@gmail.com>
    """

    _MAIN_TRANSLIT_TABLE = {
        u"а": u"a",
        u"б": u"b",
        u"в": u"v",
        u"г": u"g",
        u"д": u"d",
        u"е": u"e",
        u"ж": u"zh",
        u"з": u"z",
        u"и": u"i",
        u"й": u"j",
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
        u"х": u"h",
        u"ц": u"ts",
        u"ч": u"ch",
        u"ш": u"sh",
        u"щ": u"sch",
        u"ъ": u"'",
        u"ы": u"y",
        u"ь": u"'",
        u"ю": u"ju",
        u"я": u"ja",
    }

    MAIN_TRANSLIT_TABLE = convert_table(add_uppercase(_MAIN_TRANSLIT_TABLE))


class UkrainianWWS(object):
    """
    According to Scholarly system from
    https://en.wikipedia.org/wiki/Romanization_of_Ukrainian#Tables_of_romanization_systems
    """

    _MAIN_TRANSLIT_TABLE = {
        u"а": u"a",
        u"б": u"b",
        u"в": u"v",
        u"г": u"h",
        u"ґ": u"g",
        u"д": u"d",
        u"е": u"e",
        u"є": u"je",
        u"ж": u"ž",
        u"з": u"z",
        u"и": u"y",
        u"і": u"i",
        u"ї": u"ji",
        u"й": u"j",
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
        u"х": u"x",
        u"ц": u"c",
        u"ч": u"č",
        u"ш": u"š",
        u"щ": u"šč",
        u"ь": u"ʹ",
        u"ю": u"ju",
        u"я": u"ja",
        u"\u0027": u"",
        u"\u2019": u"",
        u"\u02BC": u"",
    }

    MAIN_TRANSLIT_TABLE = convert_table(add_uppercase(_MAIN_TRANSLIT_TABLE))


class RussianGOST2006(object):
    """
    According to GOST 2006 system from
    https://ru.wikipedia.org/wiki/%D0%A2%D1%80%D0%B0%D0%BD%D1%81%D0%BB%D0%B8%D1%82%D0%B5%D1%80%D0%B0%D1%86%D0%B8%D1%8F_%D1%80%D1%83%D1%81%D1%81%D0%BA%D0%BE%D0%B3%D0%BE_%D0%B0%D0%BB%D1%84%D0%B0%D0%B2%D0%B8%D1%82%D0%B0_%D0%BB%D0%B0%D1%82%D0%B8%D0%BD%D0%B8%D1%86%D0%B5%D0%B9#.D0.A1.D1.80.D0.B0.D0.B2.D0.BD.D0.B8.D1.82.D0.B5.D0.BB.D1.8C.D0.BD.D0.B0.D1.8F_.D1.82.D0.B0.D0.B1.D0.BB.D0.B8.D1.86.D0.B0_.D1.81.D0.B8.D1.81.D1.82.D0.B5.D0.BC_.D1.82.D1.80.D0.B0.D0.BD.D1.81.D0.BB.D0.B8.D1.82.D0.B5.D1.80.D0.B0.D1.86.D0.B8.D0.B8

    According to https://en.wikipedia.org/wiki/Romanization_of_Russian#Transliteration_of_the_names_in_Russian_passports
    (International Passport 2010)
    """

    _MAIN_TRANSLIT_TABLE = {
        u"а": u"a",
        u"б": u"b",
        u"в": u"v",
        u"г": u"g",
        u"д": u"d",
        u"е": u"e",
        u"ё": u"e",
        u"ж": u"zh",
        u"з": u"z",
        u"и": u"i",
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
        u"ц": u"tc",
        u"ч": u"ch",
        u"ш": u"sh",
        u"щ": u"shch",
        u"ъ": u"",
        u"ы": u"y",
        u"ь": u"",
        u"э": u"e",
        u"ю": u"iu",
        u"я": u"ia",
    }

    MAIN_TRANSLIT_TABLE = convert_table(add_uppercase(_MAIN_TRANSLIT_TABLE))


class UkrainianBritish(object):
    """
    According to British system from
    https://en.wikipedia.org/wiki/Romanization_of_Ukrainian#Tables_of_romanization_systems
    """

    _MAIN_TRANSLIT_TABLE = {
        u"а": u"a",
        u"б": u"b",
        u"в": u"v",
        u"г": u"h",
        u"ґ": u"g",
        u"д": u"d",
        u"е": u"e",
        u"є": u"ye",
        u"ж": u"zh",
        u"з": u"z",
        u"и": u"ȳ",
        u"і": u"i",
        u"ї": u"yi",
        u"й": u"ĭ",
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
        u"ю": u"yu",
        u"я": u"ya",
        u"\u0027": u"",
        u"\u2019": u"",
        u"\u02BC": u"",
    }

    MAIN_TRANSLIT_TABLE = convert_table(add_uppercase(_MAIN_TRANSLIT_TABLE))


class UkrainianBGN(object):
    """
    According to BGN system from
    https://en.wikipedia.org/wiki/Romanization_of_Ukrainian#Tables_of_romanization_systems
    """

    _MAIN_TRANSLIT_TABLE = {
        u"а": u"a",
        u"б": u"b",
        u"в": u"v",
        u"г": u"h",
        u"ґ": u"g",
        u"д": u"d",
        u"е": u"e",
        u"є": u"ye",
        u"ж": u"zh",
        u"з": u"z",
        u"и": u"y",
        u"і": u"i",
        u"ї": u"yi",
        u"й": u"y",
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
        u"ь": u"'",
        u"ю": u"yu",
        u"я": u"ya",
    }

    MAIN_TRANSLIT_TABLE = convert_table(add_uppercase(_MAIN_TRANSLIT_TABLE))


class UkrainianISO9(object):
    """
    According to ISO9 system from
    https://en.wikipedia.org/wiki/Romanization_of_Ukrainian#Tables_of_romanization_systems
    """

    _MAIN_TRANSLIT_TABLE = {
        u"а": u"a",
        u"б": u"b",
        u"в": u"v",
        u"г": u"g",
        u"ґ": u"g̀",
        u"д": u"d",
        u"е": u"e",
        u"є": u"ê",
        u"ж": u"ž",
        u"з": u"z",
        u"и": u"i",
        u"і": u"ì",
        u"ї": u"ï",
        u"й": u"j",
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
        u"х": u"h",
        u"ц": u"c",
        u"ч": u"č",
        u"ш": u"š",
        u"щ": u"ŝ",
        u"ь": u"′",
        u"ю": u"û",
        u"я": u"â",
    }

    MAIN_TRANSLIT_TABLE = convert_table(add_uppercase(_MAIN_TRANSLIT_TABLE))


class UkrainianFrench(object):
    """
    According to French system from
    https://en.wikipedia.org/wiki/Romanization_of_Ukrainian#Tables_of_romanization_systems
    """

    _MAIN_TRANSLIT_TABLE = {
        u"а": u"a",
        u"б": u"b",
        u"в": u"v",
        u"г": u"h",
        u"ґ": u"g",
        u"д": u"d",
        u"е": u"e",
        u"є": u"ie",
        u"ж": u"j",
        u"з": u"z",
        u"и": u"y",
        u"і": u"i",
        u"ї": u"ï",
        u"й": u"y",
        u"к": u"k",
        u"л": u"l",
        u"м": u"m",
        u"н": u"n",
        u"о": u"o",
        u"п": u"p",
        u"р": u"r",
        u"с": u"s",
        u"т": u"t",
        u"у": u"ou",
        u"ф": u"f",
        u"х": u"kh",
        u"ц": u"ts",
        u"ч": u"tch",
        u"ш": u"ch",
        u"щ": u"chtch",
        u"ь": u"",
        u"ю": u"iou",
        u"я": u"ia",
        u"\u0027": u"",
        u"\u2019": u"",
        u"\u02BC": u"",
    }

    MAIN_TRANSLIT_TABLE = convert_table(add_uppercase(_MAIN_TRANSLIT_TABLE))


class UkrainianGerman(object):
    """
    According to German system from
    https://en.wikipedia.org/wiki/Romanization_of_Ukrainian#Tables_of_romanization_systems
    """

    _MAIN_TRANSLIT_TABLE = {
        u"а": u"a",
        u"б": u"b",
        u"в": u"w",
        u"г": u"h",
        u"ґ": u"g",
        u"д": u"d",
        u"е": u"e",
        u"є": u"je",
        u"ж": u"sh",
        u"з": u"s",
        u"и": u"y",
        u"і": u"i",
        u"ї": u"ji",
        u"й": u"j",
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
        u"х": u"ch",
        u"ц": u"z",
        u"ч": u"tsch",
        u"ш": u"sch",
        u"щ": u"schtsch",
        u"ь": u"",
        u"ю": u"ju",
        u"я": u"ja",
        u"\u0027": u"",
        u"\u2019": u"",
        u"\u02BC": u"",
    }

    MAIN_TRANSLIT_TABLE = convert_table(add_uppercase(_MAIN_TRANSLIT_TABLE))


class UkrainianGOST1971(object):
    """
    According to Gost 1971 system from
    https://en.wikipedia.org/wiki/Romanization_of_Ukrainian#Tables_of_romanization_systems
    """

    _MAIN_TRANSLIT_TABLE = {
        u"а": u"a",
        u"б": u"b",
        u"в": u"v",
        u"г": u"g",
        u"ґ": u"g",
        u"д": u"d",
        u"е": u"e",
        u"є": u"je",
        u"ж": u"zh",
        u"з": u"z",
        u"и": u"i",
        u"і": u"i",
        u"ї": u"ji",
        u"й": u"j",
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
        u"ц": u"c",
        u"ч": u"ch",
        u"ш": u"sh",
        u"щ": u"shh",
        u"ь": u"'",
        u"ю": u"ju",
        u"я": u"ja",
    }

    MAIN_TRANSLIT_TABLE = convert_table(add_uppercase(_MAIN_TRANSLIT_TABLE))


class UkrainianGOST1986(object):
    """
    According to Gost 1986 system from
    https://en.wikipedia.org/wiki/Romanization_of_Ukrainian#Tables_of_romanization_systems
    """

    _MAIN_TRANSLIT_TABLE = {
        u"а": u"a",
        u"б": u"b",
        u"в": u"v",
        u"г": u"g",
        u"ґ": u"–",
        u"д": u"d",
        u"е": u"e",
        u"є": u"je",
        u"ж": u"ž",
        u"з": u"z",
        u"и": u"i",
        u"і": u"i",
        u"ї": u"i",
        u"й": u"j",
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
        u"х": u"h",
        u"ц": u"c",
        u"ч": u"č",
        u"ш": u"š",
        u"щ": u"šč",
        u"ь": u"'",
        u"ю": u"ju",
        u"я": u"ja",
        u"\u0027": u"",
        u"\u2019": u"",
        u"\u02BC": u"",
    }

    MAIN_TRANSLIT_TABLE = convert_table(add_uppercase(_MAIN_TRANSLIT_TABLE))


class UkrainianPassport2007(object):
    """
    According to Passport 2007 system from
    https://en.wikipedia.org/wiki/Romanization_of_Ukrainian#Tables_of_romanization_systems
    """

    _MAIN_TRANSLIT_TABLE = {
        u"а": u"a",
        u"б": u"b",
        u"в": u"v",
        u"г": u"g",
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
        u"\u0027": u"",
        u"\u2019": u"",
        u"\u02BC": u"",
    }

    MAIN_TRANSLIT_TABLE = convert_table(add_uppercase(_MAIN_TRANSLIT_TABLE))


class UkrainianNational1996(object):
    """
    According to National 1996 system from
    https://en.wikipedia.org/wiki/Romanization_of_Ukrainian#Tables_of_romanization_systems
    """
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
        u"щ": u"sch",
        u"ь": u"'",
        u"ю": u"iu",
        u"я": u"ia",
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

    MAIN_TRANSLIT_TABLE = convert_table(add_uppercase(_MAIN_TRANSLIT_TABLE))
    FIRST_CHARACTERS = add_uppercase(_FIRST_CHARACTERS)
    SPECIAL_CASES = add_uppercase(_SPECIAL_CASES)

    PATTERN1 = re.compile(u"(?mu)" + u'|'.join(SPECIAL_CASES.keys()))
    PATTERN2 = re.compile(u"(?mu)" + r"\b(" +
                          u'|'.join(FIRST_CHARACTERS.keys()) + u")")


class UkrainianPassport2004Alt(object):
    """
    According to Passport 2004 system from
    https://en.wikipedia.org/wiki/Romanization_of_Ukrainian#Tables_of_romanization_systems
    """
    _MAIN_TRANSLIT_TABLE = {
        u"а": u"a",
        u"б": u"b",
        u"в": u"v",
        u"г": u"g",
        u"ґ": u"h",
        u"д": u"d",
        u"е": u"e",
        u"є": u"ie",
        u"ж": u"j",
        u"з": u"z",
        u"и": u"y",
        u"і": u"i",
        u"ї": u"i",
        u"й": u"i",
        u"к": u"c",
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
        u"ь": u"'",
        u"ю": u"iu",
        u"я": u"ia",
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

    MAIN_TRANSLIT_TABLE = convert_table(add_uppercase(_MAIN_TRANSLIT_TABLE))
    FIRST_CHARACTERS = add_uppercase(_FIRST_CHARACTERS)
    SPECIAL_CASES = add_uppercase(_SPECIAL_CASES)

    PATTERN1 = re.compile(u"(?mu)" + u'|'.join(SPECIAL_CASES.keys()))
    PATTERN2 = re.compile(u"(?mu)" + r"\b(" +
                          u'|'.join(FIRST_CHARACTERS.keys()) + u")")


class RussianICAO(object):
    """
    According to https://ru.wikipedia.org/wiki/%D0%A2%D1%80%D0%B0%D0%BD%D1%81%D0%BB%D0%B8%D1%82%D0%B5%D1%80%D0%B0%D1%86%D0%B8%D1%8F_%D1%80%D1%83%D1%81%D1%81%D0%BA%D0%BE%D0%B3%D0%BE_%D0%B0%D0%BB%D1%84%D0%B0%D0%B2%D0%B8%D1%82%D0%B0_%D0%BB%D0%B0%D1%82%D0%B8%D0%BD%D0%B8%D1%86%D0%B5%D0%B9#.D0.A1.D1.80.D0.B0.D0.B2.D0.BD.D0.B8.D1.82.D0.B5.D0.BB.D1.8C.D0.BD.D0.B0.D1.8F_.D1.82.D0.B0.D0.B1.D0.BB.D0.B8.D1.86.D0.B0_.D1.81.D0.B8.D1.81.D1.82.D0.B5.D0.BC_.D1.82.D1.80.D0.B0.D0.BD.D1.81.D0.BB.D0.B8.D1.82.D0.B5.D1.80.D0.B0.D1.86.D0.B8.D0.B8
    (Doc 9303, ICAO)
    According to https://en.wikipedia.org/wiki/Romanization_of_Russian#Transliteration_of_the_names_in_Russian_passports
    (International Passport 2013)
    According to https://ru.wikipedia.org/wiki/%D0%A2%D1%80%D0%B0%D0%BD%D1%81%D0%BB%D0%B8%D1%82%D0%B5%D1%80%D0%B0%D1%86%D0%B8%D1%8F_%D1%80%D1%83%D1%81%D1%81%D0%BA%D0%BE%D0%B3%D0%BE_%D0%B0%D0%BB%D1%84%D0%B0%D0%B2%D0%B8%D1%82%D0%B0_%D0%BB%D0%B0%D1%82%D0%B8%D0%BD%D0%B8%D1%86%D0%B5%D0%B9#%D0%A1%D1%80%D0%B0%D0%B2%D0%BD%D0%B8%D1%82%D0%B5%D0%BB%D1%8C%D0%BD%D0%B0%D1%8F_%D1%82%D0%B0%D0%B1%D0%BB%D0%B8%D1%86%D0%B0_%D1%81%D0%B8%D1%81%D1%82%D0%B5%D0%BC_%D1%82%D1%80%D0%B0%D0%BD%D1%81%D0%BB%D0%B8%D1%82%D0%B5%D1%80%D0%B0%D1%86%D0%B8%D0%B8
    Приказ МИД N 4271 (2016-н/в) 
    """

    _MAIN_TRANSLIT_TABLE = {
        u"а": u"a",
        u"б": u"b",
        u"в": u"v",
        u"г": u"g",
        u"д": u"d",
        u"е": u"e",
        u"ё": u"e",
        u"ж": u"zh",
        u"з": u"z",
        u"и": u"i",
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
        u"ъ": u"ie",
        u"ы": u"y",
        u"ь": u"",
        u"э": u"e",
        u"ю": u"iu",
        u"я": u"ia",
    }

    MAIN_TRANSLIT_TABLE = convert_table(add_uppercase(_MAIN_TRANSLIT_TABLE))



class RussianISOR9Table2(object):
    """
    According to https://ru.wikipedia.org/wiki/%D0%A2%D1%80%D0%B0%D0%BD%D1%81%D0%BB%D0%B8%D1%82%D0%B5%D1%80%D0%B0%D1%86%D0%B8%D1%8F_%D1%80%D1%83%D1%81%D1%81%D0%BA%D0%BE%D0%B3%D0%BE_%D0%B0%D0%BB%D1%84%D0%B0%D0%B2%D0%B8%D1%82%D0%B0_%D0%BB%D0%B0%D1%82%D0%B8%D0%BD%D0%B8%D1%86%D0%B5%D0%B9#.D0.A1.D1.80.D0.B0.D0.B2.D0.BD.D0.B8.D1.82.D0.B5.D0.BB.D1.8C.D0.BD.D0.B0.D1.8F_.D1.82.D0.B0.D0.B1.D0.BB.D0.B8.D1.86.D0.B0_.D1.81.D0.B8.D1.81.D1.82.D0.B5.D0.BC_.D1.82.D1.80.D0.B0.D0.BD.D1.81.D0.BB.D0.B8.D1.82.D0.B5.D1.80.D0.B0.D1.86.D0.B8.D0.B8
    (ISO/R 9 (1968), ГОСТ 16876-71, СТ СЭВ 1362-78, ООН (1987))
    """

    _MAIN_TRANSLIT_TABLE = {
        u"а": u"a",
        u"б": u"b",
        u"в": u"v",
        u"г": u"g",
        u"д": u"d",
        u"е": u"e",
        u"ё": u"jo",
        u"ж": u"zh",
        u"з": u"z",
        u"и": u"i",
        u"й": u"jj",
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
        u"ц": u"c",
        u"ч": u"ch",
        u"ш": u"sh",
        u"щ": u"shh",
        u"ъ": u"″",
        u"ы": u"y",
        u"ь": u"′",
        u"э": u"eh",
        u"ю": u"ju",
        u"я": u"ja",
    }

    MAIN_TRANSLIT_TABLE = convert_table(add_uppercase(_MAIN_TRANSLIT_TABLE))

class RussianTelegram(object):
    """
    According to https://ru.wikipedia.org/wiki/%D0%A2%D1%80%D0%B0%D0%BD%D1%81%D0%BB%D0%B8%D1%82%D0%B5%D1%80%D0%B0%D1%86%D0%B8%D1%8F_%D1%80%D1%83%D1%81%D1%81%D0%BA%D0%BE%D0%B3%D0%BE_%D0%B0%D0%BB%D1%84%D0%B0%D0%B2%D0%B8%D1%82%D0%B0_%D0%BB%D0%B0%D1%82%D0%B8%D0%BD%D0%B8%D1%86%D0%B5%D0%B9#.D0.A1.D1.80.D0.B0.D0.B2.D0.BD.D0.B8.D1.82.D0.B5.D0.BB.D1.8C.D0.BD.D0.B0.D1.8F_.D1.82.D0.B0.D0.B1.D0.BB.D0.B8.D1.86.D0.B0_.D1.81.D0.B8.D1.81.D1.82.D0.B5.D0.BC_.D1.82.D1.80.D0.B0.D0.BD.D1.81.D0.BB.D0.B8.D1.82.D0.B5.D1.80.D0.B0.D1.86.D0.B8.D0.B8
    (telegrams)
    """

    _MAIN_TRANSLIT_TABLE = {
        u"а": u"a",
        u"б": u"b",
        u"в": u"v",
        u"г": u"g",
        u"д": u"d",
        u"е": u"e",
        u"ё": u"e",
        u"ж": u"j",
        u"з": u"z",
        u"и": u"i",
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
        u"х": u"h",
        u"ц": u"c",
        u"ч": u"ch",
        u"ш": u"sh",
        u"щ": u"sc",
        u"ъ": u"",
        u"ы": u"y",
        u"ь": u"",
        u"э": u"e",
        u"ю": u"iu",
        u"я": u"ia",
    }

    MAIN_TRANSLIT_TABLE = convert_table(add_uppercase(_MAIN_TRANSLIT_TABLE))


class RussianISO9SystemA(object):
    """
    According to https://ru.wikipedia.org/wiki/%D0%A2%D1%80%D0%B0%D0%BD%D1%81%D0%BB%D0%B8%D1%82%D0%B5%D1%80%D0%B0%D1%86%D0%B8%D1%8F_%D1%80%D1%83%D1%81%D1%81%D0%BA%D0%BE%D0%B3%D0%BE_%D0%B0%D0%BB%D1%84%D0%B0%D0%B2%D0%B8%D1%82%D0%B0_%D0%BB%D0%B0%D1%82%D0%B8%D0%BD%D0%B8%D1%86%D0%B5%D0%B9#.D0.A1.D1.80.D0.B0.D0.B2.D0.BD.D0.B8.D1.82.D0.B5.D0.BB.D1.8C.D0.BD.D0.B0.D1.8F_.D1.82.D0.B0.D0.B1.D0.BB.D0.B8.D1.86.D0.B0_.D1.81.D0.B8.D1.81.D1.82.D0.B5.D0.BC_.D1.82.D1.80.D0.B0.D0.BD.D1.81.D0.BB.D0.B8.D1.82.D0.B5.D1.80.D0.B0.D1.86.D0.B8.D0.B8
    (ISO 9:1995, ГОСТ 7.79-2000 система А)
    """

    _MAIN_TRANSLIT_TABLE = {
        u"а": u"a",
        u"б": u"b",
        u"в": u"v",
        u"г": u"g",
        u"д": u"d",
        u"е": u"e",
        u"ё": u"ë",
        u"ж": u"ž",
        u"з": u"z",
        u"и": u"i",
        u"й": u"j",
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
        u"х": u"h",
        u"ц": u"c",
        u"ч": u"č",
        u"ш": u"š",
        u"щ": u"ŝ",
        u"ъ": u"″",
        u"ы": u"y",
        u"ь": u"′",
        u"э": u"è",
        u"ю": u"û",
        u"я": u"â",
    }

    MAIN_TRANSLIT_TABLE = convert_table(add_uppercase(_MAIN_TRANSLIT_TABLE))

class RussianISO9SystemB(object):
    """
    According to https://ru.wikipedia.org/wiki/%D0%A2%D1%80%D0%B0%D0%BD%D1%81%D0%BB%D0%B8%D1%82%D0%B5%D1%80%D0%B0%D1%86%D0%B8%D1%8F_%D1%80%D1%83%D1%81%D1%81%D0%BA%D0%BE%D0%B3%D0%BE_%D0%B0%D0%BB%D1%84%D0%B0%D0%B2%D0%B8%D1%82%D0%B0_%D0%BB%D0%B0%D1%82%D0%B8%D0%BD%D0%B8%D1%86%D0%B5%D0%B9#.D0.A1.D1.80.D0.B0.D0.B2.D0.BD.D0.B8.D1.82.D0.B5.D0.BB.D1.8C.D0.BD.D0.B0.D1.8F_.D1.82.D0.B0.D0.B1.D0.BB.D0.B8.D1.86.D0.B0_.D1.81.D0.B8.D1.81.D1.82.D0.B5.D0.BC_.D1.82.D1.80.D0.B0.D0.BD.D1.81.D0.BB.D0.B8.D1.82.D0.B5.D1.80.D0.B0.D1.86.D0.B8.D0.B8
    (ISO 9:1995, ГОСТ 7.79-2000 система B)
    """

    _MAIN_TRANSLIT_TABLE = {
        u"а": u"a",
        u"б": u"b",
        u"в": u"v",
        u"г": u"g",
        u"д": u"d",
        u"е": u"e",
        u"ё": u"yo",
        u"ж": u"zh",
        u"з": u"z",
        u"и": u"i",
        u"й": u"j",
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
        u"х": u"x",
        u"ц": u"cz",
        u"ч": u"ch",
        u"ш": u"sh",
        u"щ": u"shh",
        u"ъ": u"''",
        u"ы": u"y'",
        u"ь": u"'",
        u"э": u"e'",
        u"ю": u"yu",
        u"я": u"ya",
    }

    # 4: Рекомендуется использовать c перед буквами e, i, y, j; и cz — в остальных случаях.

    _SPECIAL_CASES = {
        u"це": u"ce",
        u"цэ": u"ce'",
        u"ци": u"ci",
        u"цё": u"cyo", 
        u"цы": u"cy'",
        u"цю": u"cyu",
        u"ця": u"cya", 
        u"цй": u"cj",
    }

    SPECIAL_CASES = add_uppercase(_SPECIAL_CASES)
    PATTERN1 = re.compile(u"(?mu)" + u'|'.join(SPECIAL_CASES.keys()))

    MAIN_TRANSLIT_TABLE = convert_table(add_uppercase(_MAIN_TRANSLIT_TABLE))

class RussianInternationalPassport1997(object):
    """
    According to https://en.wikipedia.org/wiki/Romanization_of_Russian#Transliteration_of_the_names_in_Russian_passports
    (International Passport 1997)
    """

    _MAIN_TRANSLIT_TABLE = {
        u"а": u"a",
        u"б": u"b",
        u"в": u"v",
        u"г": u"g",
        u"д": u"d",
        u"е": u"e",
        u"ё": u"e",
        u"ж": u"zh",
        u"з": u"z",
        u"и": u"i",
        u"й": u"y",
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
        u"ъ": u"'",
        u"ы": u"y",
        u"ь": u"",
        u"э": u"e",
        u"ю": u"yu",
        u"я": u"ya",
    }

    MAIN_TRANSLIT_TABLE = convert_table(add_uppercase(_MAIN_TRANSLIT_TABLE))

    _SPECIAL_CASES = {
        u"ье": u"'ye",
        u"ьё": u"'ye",
    }

    SPECIAL_CASES = add_uppercase(_SPECIAL_CASES)
    PATTERN1 = re.compile(u"(?mu)" + u'|'.join(SPECIAL_CASES.keys()))


class RussianInternationalPassport1997Reduced(object):
    """
    According to https://en.wikipedia.org/wiki/Romanization_of_Russian#Transliteration_of_the_names_in_Russian_passports
    (International Passport 1997, reduced variant for ий, ый)
    """

    _MAIN_TRANSLIT_TABLE = {
        u"а": u"a",
        u"б": u"b",
        u"в": u"v",
        u"г": u"g",
        u"д": u"d",
        u"е": u"e",
        u"ё": u"e",
        u"ж": u"zh",
        u"з": u"z",
        u"и": u"i",
        u"й": u"y",
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
        u"ъ": u"'",
        u"ы": u"y",
        u"ь": u"",
        u"э": u"e",
        u"ю": u"yu",
        u"я": u"ya",
    }

    MAIN_TRANSLIT_TABLE = convert_table(add_uppercase(_MAIN_TRANSLIT_TABLE))

    _SPECIAL_CASES = {
        u"ье": u"'ye",
        u"ьё": u"'ye",
        u"ый": u"y",
        u"ий": u"y",
    }

    SPECIAL_CASES = add_uppercase(_SPECIAL_CASES)
    PATTERN1 = re.compile(u"(?mu)" + u'|'.join(SPECIAL_CASES.keys()))



class RussianDriverLicense(object):
    """
    According to https://ru.wikipedia.org/wiki/%D0%A2%D1%80%D0%B0%D0%BD%D1%81%D0%BB%D0%B8%D1%82%D0%B5%D1%80%D0%B0%D1%86%D0%B8%D1%8F_%D1%80%D1%83%D1%81%D1%81%D0%BA%D0%BE%D0%B3%D0%BE_%D0%B0%D0%BB%D1%84%D0%B0%D0%B2%D0%B8%D1%82%D0%B0_%D0%BB%D0%B0%D1%82%D0%B8%D0%BD%D0%B8%D1%86%D0%B5%D0%B9#.D0.A1.D1.80.D0.B0.D0.B2.D0.BD.D0.B8.D1.82.D0.B5.D0.BB.D1.8C.D0.BD.D0.B0.D1.8F_.D1.82.D0.B0.D0.B1.D0.BB.D0.B8.D1.86.D0.B0_.D1.81.D0.B8.D1.81.D1.82.D0.B5.D0.BC_.D1.82.D1.80.D0.B0.D0.BD.D1.81.D0.BB.D0.B8.D1.82.D0.B5.D1.80.D0.B0.D1.86.D0.B8.D0.B8
    (Driver license)
    """

    _MAIN_TRANSLIT_TABLE = {
        u"а": u"a",
        u"б": u"b",
        u"в": u"v",
        u"г": u"g",
        u"д": u"d",
        u"е": u"e",
        u"ё": u"ye",
        u"ж": u"zh",
        u"з": u"z",
        u"и": u"i",
        u"й": u"y",
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
        u"ъ": u"'",
        u"ы": u"y",
        u"ь": u"'",
        u"э": u"e",
        u"ю": u"yu",
        u"я": u"ya",
    }

    MAIN_TRANSLIT_TABLE = convert_table(add_uppercase(_MAIN_TRANSLIT_TABLE))

    _SPECIAL_CASES = {
        # e, ye (В начале слов, а также после гласных и Ь, Ъ)
        u"ье": u"'ye",
        u"ъе": u"'ye",

        # e (После согласных Ч, Ш, Щ, Ж),
        # yo (В начале слов, а также после гласных и Ь, Ъ)
        # ye (После согласных, кроме Ч, Ш, Щ, Ж)
        u"ьё": u"'yo",
        u"ъё": u"'yo",

        u"чё": u"che",
        u"шё": u"she",
        u"щё": u"shche",
        u"жё": u"zhe",

        # yi (После Ь)
        u"ьи": u"'yi",
    }

    _FIRST_CHARACTERS = {
        # ye (В начале слов, а также после гласных и Ь, Ъ)
        u"е": u"ye",

        # yo (В начале слов, а также после гласных и Ь, Ъ)
        u"ё": u"yo",
    }

    SPECIAL_CASES = add_uppercase(_SPECIAL_CASES)
    FIRST_CHARACTERS = add_uppercase(_FIRST_CHARACTERS)

    PATTERN1 = re.compile(u"(?mu)" + u'|'.join(SPECIAL_CASES.keys()))
    PATTERN2 = re.compile(u"(?mu)" + r"\b(" +
                          u'|'.join(FIRST_CHARACTERS.keys()) + u")")


ALL_UKRAINIAN = [
    UkrainianKMU, UkrainianSimple, UkrainianWWS, UkrainianBritish,
    UkrainianBGN, UkrainianISO9, UkrainianFrench, UkrainianGerman,
    UkrainianGOST1971, UkrainianGOST1986, UkrainianPassport2007,
    UkrainianNational1996, UkrainianPassport2004Alt
]

ALL_RUSSIAN = [
    RussianSimple, RussianGOST2006, RussianICAO, RussianTelegram,
    RussianInternationalPassport1997, RussianDriverLicense,
    RussianInternationalPassport1997Reduced, RussianISO9SystemB, RussianISO9SystemA,
    RussianISOR9Table2
]

# Backward compatibility
RussianInternationalPassport = RussianInternationalPassport1997

ALL_TRANSLITERATIONS = ALL_UKRAINIAN + ALL_RUSSIAN


def translit(src, table=UkrainianKMU, preserve_case=True):
    u""" Transliterates given unicode `src` text
    to transliterated variant according to a given transliteration table.
    Official ukrainian transliteration is used by default

    :param src: string to transliterate
    :type src: str
    :param table: transliteration table
    :type table: transliteration table object
    :param preserve_case: convert result to uppercase if source is uppercased
    (see the example below for the difference that flag makes)
    :type preserve_case: bool
    :returns: transliterated string
    :rtype: str


    >>> print(translit(u"Дмитро Згуровский"))
    Dmytro Zghurovskyi
    >>> print(translit(u"Дмитро ЗГуровский"))
    Dmytro ZGhurovskyi
    >>> print(translit(u"Дмитро згуровский"))
    Dmytro zghurovskyi
    >>> print(translit(u"Євген Петренко"))
    Yevhen Petrenko
    >>> print(translit(u"Петренко Євген"))
    Petrenko Yevhen
    >>> print(translit(u"Петренко.Євген"))
    Petrenko.Yevhen
    >>> print(translit(u"Петренко,Євген"))
    Petrenko,Yevhen
    >>> print(translit(u"Петренко/Євген"))
    Petrenko/Yevhen
    >>> print(translit(u"Євгєн"))
    Yevhien
    >>> print(translit(u"Яготин"))
    Yahotyn
    >>> print(translit(u"Ярошенко"))
    Yaroshenko
    >>> print(translit(u"Костянтин"))
    Kostiantyn
    >>> print(translit(u"Знам'янка"))
    Znamianka
    >>> print(translit(u"Знам’янка"))
    Znamianka
    >>> print(translit(u"Знам’янка"))
    Znamianka
    >>> print(translit(u"Феодосія"))
    Feodosiia
    >>> print(translit(u"Ньютон"))
    Niuton
    >>> print(translit(u"піранья"))
    pirania
    >>> print(translit(u"кур'єр"))
    kurier
    >>> print(translit(u"ЗГУРОВСЬКИЙ"))
    ZGHUROVSKYI
    >>> print(translit(u"ЗГУРОВСЬКИЙ", preserve_case=False))
    ZGhUROVSKYI

    >>> print(translit(u"Дмитро Згуровский", UkrainianSimple))
    Dmytro Zhurovskyj
    >>> print(translit(u"Дмитро Щуровский", UkrainianWWS))
    Dmytro Ščurovskyj
    >>> print(translit(u"Дмитро Щуровский", UkrainianBritish))
    Dmȳtro Shchurovskȳĭ
    >>> print(translit(u"Дмитро Щуровский", UkrainianFrench))
    Dmytro Chtchourovskyy
    >>> print(translit(u"Дмитро Щуровский", UkrainianGerman))
    Dmytro Schtschurowskyj
    >>> print(translit(u"Дмитро Щуровский", UkrainianGOST1971))
    Dmitro Shhurovskij

    >>> print(translit(u"Варенье", RussianInternationalPassport1997))
    Varen'ye
    >>> print(translit(u"Новьё", RussianInternationalPassport1997))
    Nov'ye
    >>> print(translit(u"Красный", RussianInternationalPassport1997))
    Krasnyy
    >>> print(translit(u"Полоний", RussianInternationalPassport1997))
    Poloniy

    >>> print(translit(u"Красный", RussianInternationalPassport1997Reduced))
    Krasny
    >>> print(translit(u"Полоний", RussianInternationalPassport1997Reduced))
    Polony

    >>> print(translit(u"Варенье", RussianDriverLicense))
    Varen'ye
    >>> print(translit(u"Подъезд", RussianDriverLicense))
    Pod'yezd
    >>> print(translit(u"Новьё", RussianDriverLicense))
    Nov'yo
    >>> print(translit(u"Подъёб", RussianDriverLicense))
    Pod'yob
    >>> print(translit(u"Ель", RussianDriverLicense))
    Yel'
    >>> print(translit(u"Ёж", RussianDriverLicense))
    Yozh

    >>> print(translit(u"Щёки", RussianDriverLicense))
    Shcheki
    >>> print(translit(u"Соловьи", RussianDriverLicense))
    Solov'yi


    >>> print(translit(u"Цёмки", RussianISO9SystemB))
    Cyomki
    >>> print(translit(u"Цыц", RussianISO9SystemB))
    Cy'cz
    """

    src = text_type(src)
    src_is_upper = src.isupper()

    if hasattr(table, "DELETE_PATTERN"):
        src = table.DELETE_PATTERN.sub(u"", src)

    if hasattr(table, "PATTERN1"):
        src = table.PATTERN1.sub(lambda x: table.SPECIAL_CASES[x.group()], src)

    if hasattr(table, "PATTERN2"):
        src = table.PATTERN2.sub(lambda x: table.FIRST_CHARACTERS[x.group()],
                                 src)
    res = src.translate(table.MAIN_TRANSLIT_TABLE)

    if src_is_upper and preserve_case:
        return res.upper()
    else:
        return res


# For backward compatibility
translitua = translit

__all__ = [
    "translit", "translitua", "UkrainianKMU", "UkrainianSimple",
    "UkrainianWWS", "RussianGOST2006", "RussianSimple", "ALL_RUSSIAN",
    "ALL_UKRAINIAN", "UkrainianBritish", "UkrainianBGN", "UkrainianISO9",
    "UkrainianFrench", "UkrainianGerman", "UkrainianGOST1971",
    "UkrainianGOST1986", "UkrainianPassport2007", "UkrainianNational1996",
    "UkrainianPassport2004Alt", "RussianICAO", "ALL_TRANSLITERATIONS",
    "RussianTelegram", "RussianInternationalPassport1997", "RussianDriverLicense",
    "RussianInternationalPassport1997Reduced",
    "RussianInternationalPassport", "RussianISO9SystemB", "RussianISO9SystemA", "RussianISOR9Table2"]


if __name__ == '__main__':
    import doctest
    doctest.testmod()
