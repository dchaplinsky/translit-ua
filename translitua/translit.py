import re
from typing import Protocol


class TransliterationTable(Protocol):
    """The contract every transliteration table class satisfies.

    ``MAIN_TRANSLIT_TABLE`` is required; tables may additionally define
    special-case patterns (``PATTERN1``/``SPECIAL_CASES``,
    ``PATTERN2``/``FIRST_CHARACTERS``, ``DELETE_PATTERN``) which
    ``translit`` picks up when present.
    """

    MAIN_TRANSLIT_TABLE: dict


def add_uppercase(table: dict) -> dict:
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
    orig.update(dict((k.capitalize(), v.capitalize()) for k, v in table.items()))

    return orig


def convert_table(table: dict) -> dict:
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


class UkrainianKMU:
    """
    According to National system from
    https://en.wikipedia.org/wiki/Romanization_of_Ukrainian#Tables_of_romanization_systems
    """

    _MAIN_TRANSLIT_TABLE = {
        "а": "a",
        "б": "b",
        "в": "v",
        "г": "h",
        "ґ": "g",
        "д": "d",
        "е": "e",
        "є": "ie",
        "ж": "zh",
        "з": "z",
        "и": "y",
        "і": "i",
        "ї": "i",
        "й": "i",
        "к": "k",
        "л": "l",
        "м": "m",
        "н": "n",
        "о": "o",
        "п": "p",
        "р": "r",
        "с": "s",
        "т": "t",
        "у": "u",
        "ф": "f",
        "х": "kh",
        "ц": "ts",
        "ч": "ch",
        "ш": "sh",
        "щ": "shch",
        "ю": "iu",
        "я": "ia",
    }

    _DELETE_CASES = [
        "ь",
        "Ь",
        "\u0027",
        "\u2019",
        "\u02BC",
    ]

    _SPECIAL_CASES = {
        "зг": "zgh",
        "ЗГ": "ZGh",
    }

    _FIRST_CHARACTERS = {"є": "ye", "ї": "yi", "й": "y", "ю": "yu", "я": "ya"}

    MAIN_TRANSLIT_TABLE = convert_table(add_uppercase(_MAIN_TRANSLIT_TABLE))
    FIRST_CHARACTERS = add_uppercase(_FIRST_CHARACTERS)
    SPECIAL_CASES = add_uppercase(_SPECIAL_CASES)

    PATTERN1 = re.compile("(?mu)" + "|".join(SPECIAL_CASES.keys()))
    PATTERN2 = re.compile("(?mu)" + r"\b(" + "|".join(FIRST_CHARACTERS.keys()) + ")")
    DELETE_PATTERN = re.compile("(?mu)" + "|".join(_DELETE_CASES))


class UkrainianSimple:
    """
    Borrowed from https://github.com/barseghyanartur/transliterate/blob/master/src/transliterate/contrib/languages/uk/data/python32.py
    by Artur Barseghyan <artur.barseghyan@gmail.com>
    """

    _MAIN_TRANSLIT_TABLE = {
        "а": "a",
        "б": "b",
        "в": "v",
        "г": "h",
        "ґ": "g",
        "д": "d",
        "е": "e",
        "є": "ye",
        "ж": "zh",
        "з": "z",
        "и": "y",
        "і": "i",
        "ї": "yi",
        "й": "j",
        "к": "k",
        "л": "l",
        "м": "m",
        "н": "n",
        "о": "o",
        "п": "p",
        "р": "r",
        "с": "s",
        "т": "t",
        "у": "u",
        "ф": "f",
        "х": "kh",
        "ц": "ts",
        "ч": "ch",
        "ш": "sh",
        "щ": "shch",
        "ь": "'",
        "ю": "ju",
        "я": "ja",
    }

    MAIN_TRANSLIT_TABLE = convert_table(add_uppercase(_MAIN_TRANSLIT_TABLE))


class RussianSimple:
    """
    Borrowed from https://github.com/barseghyanartur/transliterate/blob/master/src/transliterate/contrib/languages/ru/data/python32.py
    by Artur Barseghyan <artur.barseghyan@gmail.com>
    """

    _MAIN_TRANSLIT_TABLE = {
        "а": "a",
        "б": "b",
        "в": "v",
        "г": "g",
        "д": "d",
        "е": "e",
        "ё": "e",
        "ж": "zh",
        "з": "z",
        "и": "i",
        "й": "j",
        "к": "k",
        "л": "l",
        "м": "m",
        "н": "n",
        "о": "o",
        "п": "p",
        "р": "r",
        "с": "s",
        "т": "t",
        "у": "u",
        "ф": "f",
        "х": "h",
        "ц": "ts",
        "ч": "ch",
        "ш": "sh",
        "щ": "sch",
        "ъ": "'",
        "ы": "y",
        "ь": "'",
        "э": "e",
        "ю": "ju",
        "я": "ja",
    }

    MAIN_TRANSLIT_TABLE = convert_table(add_uppercase(_MAIN_TRANSLIT_TABLE))


class UkrainianWWS:
    """
    According to Scholarly system from
    https://en.wikipedia.org/wiki/Romanization_of_Ukrainian#Tables_of_romanization_systems
    """

    _MAIN_TRANSLIT_TABLE = {
        "а": "a",
        "б": "b",
        "в": "v",
        "г": "h",
        "ґ": "g",
        "д": "d",
        "е": "e",
        "є": "je",
        "ж": "ž",
        "з": "z",
        "и": "y",
        "і": "i",
        "ї": "ji",
        "й": "j",
        "к": "k",
        "л": "l",
        "м": "m",
        "н": "n",
        "о": "o",
        "п": "p",
        "р": "r",
        "с": "s",
        "т": "t",
        "у": "u",
        "ф": "f",
        "х": "x",
        "ц": "c",
        "ч": "č",
        "ш": "š",
        "щ": "šč",
        "ь": "ʹ",
        "ю": "ju",
        "я": "ja",
        "\u0027": "",
        "\u2019": "",
        "\u02BC": "",
    }

    MAIN_TRANSLIT_TABLE = convert_table(add_uppercase(_MAIN_TRANSLIT_TABLE))


class RussianGOST2006:
    """
    According to GOST 2006 system from
    https://ru.wikipedia.org/wiki/%D0%A2%D1%80%D0%B0%D0%BD%D1%81%D0%BB%D0%B8%D1%82%D0%B5%D1%80%D0%B0%D1%86%D0%B8%D1%8F_%D1%80%D1%83%D1%81%D1%81%D0%BA%D0%BE%D0%B3%D0%BE_%D0%B0%D0%BB%D1%84%D0%B0%D0%B2%D0%B8%D1%82%D0%B0_%D0%BB%D0%B0%D1%82%D0%B8%D0%BD%D0%B8%D1%86%D0%B5%D0%B9#.D0.A1.D1.80.D0.B0.D0.B2.D0.BD.D0.B8.D1.82.D0.B5.D0.BB.D1.8C.D0.BD.D0.B0.D1.8F_.D1.82.D0.B0.D0.B1.D0.BB.D0.B8.D1.86.D0.B0_.D1.81.D0.B8.D1.81.D1.82.D0.B5.D0.BC_.D1.82.D1.80.D0.B0.D0.BD.D1.81.D0.BB.D0.B8.D1.82.D0.B5.D1.80.D0.B0.D1.86.D0.B8.D0.B8

    According to https://en.wikipedia.org/wiki/Romanization_of_Russian#Transliteration_of_the_names_in_Russian_passports
    (International Passport 2010)
    """

    _MAIN_TRANSLIT_TABLE = {
        "а": "a",
        "б": "b",
        "в": "v",
        "г": "g",
        "д": "d",
        "е": "e",
        "ё": "e",
        "ж": "zh",
        "з": "z",
        "и": "i",
        "й": "i",
        "к": "k",
        "л": "l",
        "м": "m",
        "н": "n",
        "о": "o",
        "п": "p",
        "р": "r",
        "с": "s",
        "т": "t",
        "у": "u",
        "ф": "f",
        "х": "kh",
        "ц": "tc",
        "ч": "ch",
        "ш": "sh",
        "щ": "shch",
        "ъ": "",
        "ы": "y",
        "ь": "",
        "э": "e",
        "ю": "iu",
        "я": "ia",
    }

    MAIN_TRANSLIT_TABLE = convert_table(add_uppercase(_MAIN_TRANSLIT_TABLE))


class UkrainianBritish:
    """
    According to British system from
    https://en.wikipedia.org/wiki/Romanization_of_Ukrainian#Tables_of_romanization_systems
    """

    _MAIN_TRANSLIT_TABLE = {
        "а": "a",
        "б": "b",
        "в": "v",
        "г": "h",
        "ґ": "g",
        "д": "d",
        "е": "e",
        "є": "ye",
        "ж": "zh",
        "з": "z",
        "и": "ȳ",
        "і": "i",
        "ї": "yi",
        "й": "ĭ",
        "к": "k",
        "л": "l",
        "м": "m",
        "н": "n",
        "о": "o",
        "п": "p",
        "р": "r",
        "с": "s",
        "т": "t",
        "у": "u",
        "ф": "f",
        "х": "kh",
        "ц": "ts",
        "ч": "ch",
        "ш": "sh",
        "щ": "shch",
        "ь": "",
        "ю": "yu",
        "я": "ya",
        "\u0027": "",
        "\u2019": "",
        "\u02BC": "",
    }

    MAIN_TRANSLIT_TABLE = convert_table(add_uppercase(_MAIN_TRANSLIT_TABLE))


class UkrainianBGN:
    """
    Superseded by the 2019 BGN/PCGN agreement, which adopted the 2010
    national system as-is (see UkrainianBGN2019 / UkrainianKMU).

    According to BGN system from
    https://en.wikipedia.org/wiki/Romanization_of_Ukrainian#Tables_of_romanization_systems
    """

    _MAIN_TRANSLIT_TABLE = {
        "а": "a",
        "б": "b",
        "в": "v",
        "г": "h",
        "ґ": "g",
        "д": "d",
        "е": "e",
        "є": "ye",
        "ж": "zh",
        "з": "z",
        "и": "y",
        "і": "i",
        "ї": "yi",
        "й": "y",
        "к": "k",
        "л": "l",
        "м": "m",
        "н": "n",
        "о": "o",
        "п": "p",
        "р": "r",
        "с": "s",
        "т": "t",
        "у": "u",
        "ф": "f",
        "х": "kh",
        "ц": "ts",
        "ч": "ch",
        "ш": "sh",
        "щ": "shch",
        "ь": "'",
        "ю": "yu",
        "я": "ya",
    }

    MAIN_TRANSLIT_TABLE = convert_table(add_uppercase(_MAIN_TRANSLIT_TABLE))


class UkrainianISO9:
    """
    According to ISO9 system from
    https://en.wikipedia.org/wiki/Romanization_of_Ukrainian#Tables_of_romanization_systems
    """

    _MAIN_TRANSLIT_TABLE = {
        "а": "a",
        "б": "b",
        "в": "v",
        "г": "g",
        "ґ": "g̀",
        "д": "d",
        "е": "e",
        "є": "ê",
        "ж": "ž",
        "з": "z",
        "и": "i",
        "і": "ì",
        "ї": "ï",
        "й": "j",
        "к": "k",
        "л": "l",
        "м": "m",
        "н": "n",
        "о": "o",
        "п": "p",
        "р": "r",
        "с": "s",
        "т": "t",
        "у": "u",
        "ф": "f",
        "х": "h",
        "ц": "c",
        "ч": "č",
        "ш": "š",
        "щ": "ŝ",
        "ь": "′",
        "ю": "û",
        "я": "â",
    }

    MAIN_TRANSLIT_TABLE = convert_table(add_uppercase(_MAIN_TRANSLIT_TABLE))


class UkrainianFrench:
    """
    According to French system from
    https://en.wikipedia.org/wiki/Romanization_of_Ukrainian#Tables_of_romanization_systems
    """

    _MAIN_TRANSLIT_TABLE = {
        "а": "a",
        "б": "b",
        "в": "v",
        "г": "h",
        "ґ": "g",
        "д": "d",
        "е": "e",
        "є": "ie",
        "ж": "j",
        "з": "z",
        "и": "y",
        "і": "i",
        "ї": "ï",
        "й": "y",
        "к": "k",
        "л": "l",
        "м": "m",
        "н": "n",
        "о": "o",
        "п": "p",
        "р": "r",
        "с": "s",
        "т": "t",
        "у": "ou",
        "ф": "f",
        "х": "kh",
        "ц": "ts",
        "ч": "tch",
        "ш": "ch",
        "щ": "chtch",
        "ь": "",
        "ю": "iou",
        "я": "ia",
        "\u0027": "",
        "\u2019": "",
        "\u02BC": "",
    }

    MAIN_TRANSLIT_TABLE = convert_table(add_uppercase(_MAIN_TRANSLIT_TABLE))


class UkrainianGerman:
    """
    According to German system from
    https://en.wikipedia.org/wiki/Romanization_of_Ukrainian#Tables_of_romanization_systems
    """

    _MAIN_TRANSLIT_TABLE = {
        "а": "a",
        "б": "b",
        "в": "w",
        "г": "h",
        "ґ": "g",
        "д": "d",
        "е": "e",
        "є": "je",
        "ж": "sh",
        "з": "s",
        "и": "y",
        "і": "i",
        "ї": "ji",
        "й": "j",
        "к": "k",
        "л": "l",
        "м": "m",
        "н": "n",
        "о": "o",
        "п": "p",
        "р": "r",
        "с": "s",
        "т": "t",
        "у": "u",
        "ф": "f",
        "х": "ch",
        "ц": "z",
        "ч": "tsch",
        "ш": "sch",
        "щ": "schtsch",
        "ь": "",
        "ю": "ju",
        "я": "ja",
        "\u0027": "",
        "\u2019": "",
        "\u02BC": "",
    }

    MAIN_TRANSLIT_TABLE = convert_table(add_uppercase(_MAIN_TRANSLIT_TABLE))


class UkrainianGOST1971:
    """
    According to Gost 1971 system from
    https://en.wikipedia.org/wiki/Romanization_of_Ukrainian#Tables_of_romanization_systems
    """

    _MAIN_TRANSLIT_TABLE = {
        "а": "a",
        "б": "b",
        "в": "v",
        "г": "g",
        "ґ": "g",
        "д": "d",
        "е": "e",
        "є": "je",
        "ж": "zh",
        "з": "z",
        "и": "i",
        "і": "i",
        "ї": "ji",
        "й": "j",
        "к": "k",
        "л": "l",
        "м": "m",
        "н": "n",
        "о": "o",
        "п": "p",
        "р": "r",
        "с": "s",
        "т": "t",
        "у": "u",
        "ф": "f",
        "х": "kh",
        "ц": "c",
        "ч": "ch",
        "ш": "sh",
        "щ": "shh",
        "ь": "'",
        "ю": "ju",
        "я": "ja",
    }

    MAIN_TRANSLIT_TABLE = convert_table(add_uppercase(_MAIN_TRANSLIT_TABLE))


class UkrainianGOST1986:
    """
    According to Gost 1986 system from
    https://en.wikipedia.org/wiki/Romanization_of_Ukrainian#Tables_of_romanization_systems
    """

    _MAIN_TRANSLIT_TABLE = {
        "а": "a",
        "б": "b",
        "в": "v",
        "г": "g",
        "ґ": "g",
        "д": "d",
        "е": "e",
        "є": "je",
        "ж": "ž",
        "з": "z",
        "и": "i",
        "і": "i",
        "ї": "i",
        "й": "j",
        "к": "k",
        "л": "l",
        "м": "m",
        "н": "n",
        "о": "o",
        "п": "p",
        "р": "r",
        "с": "s",
        "т": "t",
        "у": "u",
        "ф": "f",
        "х": "h",
        "ц": "c",
        "ч": "č",
        "ш": "š",
        "щ": "šč",
        "ь": "'",
        "ю": "ju",
        "я": "ja",
        "\u0027": "",
        "\u2019": "",
        "\u02BC": "",
    }

    MAIN_TRANSLIT_TABLE = convert_table(add_uppercase(_MAIN_TRANSLIT_TABLE))


class UkrainianPassport2007:
    """
    According to Passport 2007 system from
    https://en.wikipedia.org/wiki/Romanization_of_Ukrainian#Tables_of_romanization_systems
    """

    _MAIN_TRANSLIT_TABLE = {
        "а": "a",
        "б": "b",
        "в": "v",
        "г": "g",
        "ґ": "g",
        "д": "d",
        "е": "e",
        "є": "ie",
        "ж": "zh",
        "з": "z",
        "и": "y",
        "і": "i",
        "ї": "i",
        "й": "i",
        "к": "k",
        "л": "l",
        "м": "m",
        "н": "n",
        "о": "o",
        "п": "p",
        "р": "r",
        "с": "s",
        "т": "t",
        "у": "u",
        "ф": "f",
        "х": "kh",
        "ц": "ts",
        "ч": "ch",
        "ш": "sh",
        "щ": "shch",
        "ь": "",
        "ю": "iu",
        "я": "ia",
        "\u0027": "",
        "\u2019": "",
        "\u02BC": "",
    }

    MAIN_TRANSLIT_TABLE = convert_table(add_uppercase(_MAIN_TRANSLIT_TABLE))


class UkrainianNational1996:
    """
    According to National 1996 system from
    https://en.wikipedia.org/wiki/Romanization_of_Ukrainian#Tables_of_romanization_systems
    """

    _MAIN_TRANSLIT_TABLE = {
        "а": "a",
        "б": "b",
        "в": "v",
        "г": "h",
        "ґ": "g",
        "д": "d",
        "е": "e",
        "є": "ie",
        "ж": "zh",
        "з": "z",
        "и": "y",
        "і": "i",
        "ї": "i",
        "й": "i",
        "к": "k",
        "л": "l",
        "м": "m",
        "н": "n",
        "о": "o",
        "п": "p",
        "р": "r",
        "с": "s",
        "т": "t",
        "у": "u",
        "ф": "f",
        "х": "kh",
        "ц": "ts",
        "ч": "ch",
        "ш": "sh",
        "щ": "sch",
        "ь": "'",
        "ю": "iu",
        "я": "ia",
    }

    _SPECIAL_CASES = {
        "зг": "zgh",
        "ЗГ": "ZGh",
    }

    _FIRST_CHARACTERS = {"є": "ye", "ї": "yi", "й": "y", "ю": "yu", "я": "ya"}

    MAIN_TRANSLIT_TABLE = convert_table(add_uppercase(_MAIN_TRANSLIT_TABLE))
    FIRST_CHARACTERS = add_uppercase(_FIRST_CHARACTERS)
    SPECIAL_CASES = add_uppercase(_SPECIAL_CASES)

    PATTERN1 = re.compile("(?mu)" + "|".join(SPECIAL_CASES.keys()))
    PATTERN2 = re.compile("(?mu)" + r"\b(" + "|".join(FIRST_CHARACTERS.keys()) + ")")


class UkrainianPassport2004Alt:
    """
    According to Passport 2004 system from
    https://en.wikipedia.org/wiki/Romanization_of_Ukrainian#Tables_of_romanization_systems
    """

    _MAIN_TRANSLIT_TABLE = {
        "а": "a",
        "б": "b",
        "в": "v",
        "г": "g",
        "ґ": "h",
        "д": "d",
        "е": "e",
        "є": "ie",
        "ж": "j",
        "з": "z",
        "и": "y",
        "і": "i",
        "ї": "i",
        "й": "i",
        "к": "c",
        "л": "l",
        "м": "m",
        "н": "n",
        "о": "o",
        "п": "p",
        "р": "r",
        "с": "s",
        "т": "t",
        "у": "u",
        "ф": "f",
        "х": "kh",
        "ц": "ts",
        "ч": "ch",
        "ш": "sh",
        "щ": "shch",
        "ь": "'",
        "ю": "iu",
        "я": "ia",
    }

    _SPECIAL_CASES = {
        "зг": "zgh",
        "ЗГ": "ZGh",
    }

    _FIRST_CHARACTERS = {"є": "ye", "ї": "yi", "й": "y", "ю": "yu", "я": "ya"}

    MAIN_TRANSLIT_TABLE = convert_table(add_uppercase(_MAIN_TRANSLIT_TABLE))
    FIRST_CHARACTERS = add_uppercase(_FIRST_CHARACTERS)
    SPECIAL_CASES = add_uppercase(_SPECIAL_CASES)

    PATTERN1 = re.compile("(?mu)" + "|".join(SPECIAL_CASES.keys()))
    PATTERN2 = re.compile("(?mu)" + r"\b(" + "|".join(FIRST_CHARACTERS.keys()) + ")")


class RussianICAO:
    """
    According to https://ru.wikipedia.org/wiki/%D0%A2%D1%80%D0%B0%D0%BD%D1%81%D0%BB%D0%B8%D1%82%D0%B5%D1%80%D0%B0%D1%86%D0%B8%D1%8F_%D1%80%D1%83%D1%81%D1%81%D0%BA%D0%BE%D0%B3%D0%BE_%D0%B0%D0%BB%D1%84%D0%B0%D0%B2%D0%B8%D1%82%D0%B0_%D0%BB%D0%B0%D1%82%D0%B8%D0%BD%D0%B8%D1%86%D0%B5%D0%B9#.D0.A1.D1.80.D0.B0.D0.B2.D0.BD.D0.B8.D1.82.D0.B5.D0.BB.D1.8C.D0.BD.D0.B0.D1.8F_.D1.82.D0.B0.D0.B1.D0.BB.D0.B8.D1.86.D0.B0_.D1.81.D0.B8.D1.81.D1.82.D0.B5.D0.BC_.D1.82.D1.80.D0.B0.D0.BD.D1.81.D0.BB.D0.B8.D1.82.D0.B5.D1.80.D0.B0.D1.86.D0.B8.D0.B8
    (Doc 9303, ICAO)
    According to https://en.wikipedia.org/wiki/Romanization_of_Russian#Transliteration_of_the_names_in_Russian_passports
    (International Passport 2013)
    According to https://ru.wikipedia.org/wiki/%D0%A2%D1%80%D0%B0%D0%BD%D1%81%D0%BB%D0%B8%D1%82%D0%B5%D1%80%D0%B0%D1%86%D0%B8%D1%8F_%D1%80%D1%83%D1%81%D1%81%D0%BA%D0%BE%D0%B3%D0%BE_%D0%B0%D0%BB%D1%84%D0%B0%D0%B2%D0%B8%D1%82%D0%B0_%D0%BB%D0%B0%D1%82%D0%B8%D0%BD%D0%B8%D1%86%D0%B5%D0%B9#%D0%A1%D1%80%D0%B0%D0%B2%D0%BD%D0%B8%D1%82%D0%B5%D0%BB%D1%8C%D0%BD%D0%B0%D1%8F_%D1%82%D0%B0%D0%B1%D0%BB%D0%B8%D1%86%D0%B0_%D1%81%D0%B8%D1%81%D1%82%D0%B5%D0%BC_%D1%82%D1%80%D0%B0%D0%BD%D1%81%D0%BB%D0%B8%D1%82%D0%B5%D1%80%D0%B0%D1%86%D0%B8%D0%B8
    Приказ МИД N 4271 (2016-н/в)
    """

    _MAIN_TRANSLIT_TABLE = {
        "а": "a",
        "б": "b",
        "в": "v",
        "г": "g",
        "д": "d",
        "е": "e",
        "ё": "e",
        "ж": "zh",
        "з": "z",
        "и": "i",
        "й": "i",
        "к": "k",
        "л": "l",
        "м": "m",
        "н": "n",
        "о": "o",
        "п": "p",
        "р": "r",
        "с": "s",
        "т": "t",
        "у": "u",
        "ф": "f",
        "х": "kh",
        "ц": "ts",
        "ч": "ch",
        "ш": "sh",
        "щ": "shch",
        "ъ": "ie",
        "ы": "y",
        "ь": "",
        "э": "e",
        "ю": "iu",
        "я": "ia",
    }

    MAIN_TRANSLIT_TABLE = convert_table(add_uppercase(_MAIN_TRANSLIT_TABLE))


class RussianISOR9Table2:
    """
    According to https://ru.wikipedia.org/wiki/%D0%A2%D1%80%D0%B0%D0%BD%D1%81%D0%BB%D0%B8%D1%82%D0%B5%D1%80%D0%B0%D1%86%D0%B8%D1%8F_%D1%80%D1%83%D1%81%D1%81%D0%BA%D0%BE%D0%B3%D0%BE_%D0%B0%D0%BB%D1%84%D0%B0%D0%B2%D0%B8%D1%82%D0%B0_%D0%BB%D0%B0%D1%82%D0%B8%D0%BD%D0%B8%D1%86%D0%B5%D0%B9#.D0.A1.D1.80.D0.B0.D0.B2.D0.BD.D0.B8.D1.82.D0.B5.D0.BB.D1.8C.D0.BD.D0.B0.D1.8F_.D1.82.D0.B0.D0.B1.D0.BB.D0.B8.D1.86.D0.B0_.D1.81.D0.B8.D1.81.D1.82.D0.B5.D0.BC_.D1.82.D1.80.D0.B0.D0.BD.D1.81.D0.BB.D0.B8.D1.82.D0.B5.D1.80.D0.B0.D1.86.D0.B8.D0.B8
    (ISO/R 9 (1968), ГОСТ 16876-71, СТ СЭВ 1362-78, ООН (1987))
    """

    _MAIN_TRANSLIT_TABLE = {
        "а": "a",
        "б": "b",
        "в": "v",
        "г": "g",
        "д": "d",
        "е": "e",
        "ё": "jo",
        "ж": "zh",
        "з": "z",
        "и": "i",
        "й": "jj",
        "к": "k",
        "л": "l",
        "м": "m",
        "н": "n",
        "о": "o",
        "п": "p",
        "р": "r",
        "с": "s",
        "т": "t",
        "у": "u",
        "ф": "f",
        "х": "kh",
        "ц": "c",
        "ч": "ch",
        "ш": "sh",
        "щ": "shh",
        "ъ": "″",
        "ы": "y",
        "ь": "′",
        "э": "eh",
        "ю": "ju",
        "я": "ja",
    }

    MAIN_TRANSLIT_TABLE = convert_table(add_uppercase(_MAIN_TRANSLIT_TABLE))


class RussianTelegram:
    """
    According to https://ru.wikipedia.org/wiki/%D0%A2%D1%80%D0%B0%D0%BD%D1%81%D0%BB%D0%B8%D1%82%D0%B5%D1%80%D0%B0%D1%86%D0%B8%D1%8F_%D1%80%D1%83%D1%81%D1%81%D0%BA%D0%BE%D0%B3%D0%BE_%D0%B0%D0%BB%D1%84%D0%B0%D0%B2%D0%B8%D1%82%D0%B0_%D0%BB%D0%B0%D1%82%D0%B8%D0%BD%D0%B8%D1%86%D0%B5%D0%B9#.D0.A1.D1.80.D0.B0.D0.B2.D0.BD.D0.B8.D1.82.D0.B5.D0.BB.D1.8C.D0.BD.D0.B0.D1.8F_.D1.82.D0.B0.D0.B1.D0.BB.D0.B8.D1.86.D0.B0_.D1.81.D0.B8.D1.81.D1.82.D0.B5.D0.BC_.D1.82.D1.80.D0.B0.D0.BD.D1.81.D0.BB.D0.B8.D1.82.D0.B5.D1.80.D0.B0.D1.86.D0.B8.D0.B8
    (telegrams)
    """

    _MAIN_TRANSLIT_TABLE = {
        "а": "a",
        "б": "b",
        "в": "v",
        "г": "g",
        "д": "d",
        "е": "e",
        "ё": "e",
        "ж": "j",
        "з": "z",
        "и": "i",
        "й": "i",
        "к": "k",
        "л": "l",
        "м": "m",
        "н": "n",
        "о": "o",
        "п": "p",
        "р": "r",
        "с": "s",
        "т": "t",
        "у": "u",
        "ф": "f",
        "х": "h",
        "ц": "c",
        "ч": "ch",
        "ш": "sh",
        "щ": "sc",
        "ъ": "",
        "ы": "y",
        "ь": "",
        "э": "e",
        "ю": "iu",
        "я": "ia",
    }

    MAIN_TRANSLIT_TABLE = convert_table(add_uppercase(_MAIN_TRANSLIT_TABLE))


class RussianISO9SystemA:
    """
    According to https://ru.wikipedia.org/wiki/%D0%A2%D1%80%D0%B0%D0%BD%D1%81%D0%BB%D0%B8%D1%82%D0%B5%D1%80%D0%B0%D1%86%D0%B8%D1%8F_%D1%80%D1%83%D1%81%D1%81%D0%BA%D0%BE%D0%B3%D0%BE_%D0%B0%D0%BB%D1%84%D0%B0%D0%B2%D0%B8%D1%82%D0%B0_%D0%BB%D0%B0%D1%82%D0%B8%D0%BD%D0%B8%D1%86%D0%B5%D0%B9#.D0.A1.D1.80.D0.B0.D0.B2.D0.BD.D0.B8.D1.82.D0.B5.D0.BB.D1.8C.D0.BD.D0.B0.D1.8F_.D1.82.D0.B0.D0.B1.D0.BB.D0.B8.D1.86.D0.B0_.D1.81.D0.B8.D1.81.D1.82.D0.B5.D0.BC_.D1.82.D1.80.D0.B0.D0.BD.D1.81.D0.BB.D0.B8.D1.82.D0.B5.D1.80.D0.B0.D1.86.D0.B8.D0.B8
    (ISO 9:1995, ГОСТ 7.79-2000 система А)
    """

    _MAIN_TRANSLIT_TABLE = {
        "а": "a",
        "б": "b",
        "в": "v",
        "г": "g",
        "д": "d",
        "е": "e",
        "ё": "ë",
        "ж": "ž",
        "з": "z",
        "и": "i",
        "й": "j",
        "к": "k",
        "л": "l",
        "м": "m",
        "н": "n",
        "о": "o",
        "п": "p",
        "р": "r",
        "с": "s",
        "т": "t",
        "у": "u",
        "ф": "f",
        "х": "h",
        "ц": "c",
        "ч": "č",
        "ш": "š",
        "щ": "ŝ",
        "ъ": "″",
        "ы": "y",
        "ь": "′",
        "э": "è",
        "ю": "û",
        "я": "â",
    }

    MAIN_TRANSLIT_TABLE = convert_table(add_uppercase(_MAIN_TRANSLIT_TABLE))


class RussianISO9SystemB:
    """
    According to https://ru.wikipedia.org/wiki/%D0%A2%D1%80%D0%B0%D0%BD%D1%81%D0%BB%D0%B8%D1%82%D0%B5%D1%80%D0%B0%D1%86%D0%B8%D1%8F_%D1%80%D1%83%D1%81%D1%81%D0%BA%D0%BE%D0%B3%D0%BE_%D0%B0%D0%BB%D1%84%D0%B0%D0%B2%D0%B8%D1%82%D0%B0_%D0%BB%D0%B0%D1%82%D0%B8%D0%BD%D0%B8%D1%86%D0%B5%D0%B9#.D0.A1.D1.80.D0.B0.D0.B2.D0.BD.D0.B8.D1.82.D0.B5.D0.BB.D1.8C.D0.BD.D0.B0.D1.8F_.D1.82.D0.B0.D0.B1.D0.BB.D0.B8.D1.86.D0.B0_.D1.81.D0.B8.D1.81.D1.82.D0.B5.D0.BC_.D1.82.D1.80.D0.B0.D0.BD.D1.81.D0.BB.D0.B8.D1.82.D0.B5.D1.80.D0.B0.D1.86.D0.B8.D0.B8
    (ISO 9:1995, ГОСТ 7.79-2000 система B)
    """

    _MAIN_TRANSLIT_TABLE = {
        "а": "a",
        "б": "b",
        "в": "v",
        "г": "g",
        "д": "d",
        "е": "e",
        "ё": "yo",
        "ж": "zh",
        "з": "z",
        "и": "i",
        "й": "j",
        "к": "k",
        "л": "l",
        "м": "m",
        "н": "n",
        "о": "o",
        "п": "p",
        "р": "r",
        "с": "s",
        "т": "t",
        "у": "u",
        "ф": "f",
        "х": "x",
        "ц": "cz",
        "ч": "ch",
        "ш": "sh",
        "щ": "shh",
        "ъ": "''",
        "ы": "y'",
        "ь": "'",
        "э": "e'",
        "ю": "yu",
        "я": "ya",
    }

    # 4: Рекомендуется использовать c перед буквами e, i, y, j; и cz — в остальных случаях.

    _SPECIAL_CASES = {
        "це": "ce",
        "цэ": "ce'",
        "ци": "ci",
        "цё": "cyo",
        "цы": "cy'",
        "цю": "cyu",
        "ця": "cya",
        "цй": "cj",
    }

    SPECIAL_CASES = add_uppercase(_SPECIAL_CASES)
    PATTERN1 = re.compile("(?mu)" + "|".join(SPECIAL_CASES.keys()))

    MAIN_TRANSLIT_TABLE = convert_table(add_uppercase(_MAIN_TRANSLIT_TABLE))


class RussianInternationalPassport1997:
    """
    According to https://en.wikipedia.org/wiki/Romanization_of_Russian#Transliteration_of_the_names_in_Russian_passports
    (International Passport 1997)
    """

    _MAIN_TRANSLIT_TABLE = {
        "а": "a",
        "б": "b",
        "в": "v",
        "г": "g",
        "д": "d",
        "е": "e",
        "ё": "e",
        "ж": "zh",
        "з": "z",
        "и": "i",
        "й": "y",
        "к": "k",
        "л": "l",
        "м": "m",
        "н": "n",
        "о": "o",
        "п": "p",
        "р": "r",
        "с": "s",
        "т": "t",
        "у": "u",
        "ф": "f",
        "х": "kh",
        "ц": "ts",
        "ч": "ch",
        "ш": "sh",
        "щ": "shch",
        "ъ": "'",
        "ы": "y",
        "ь": "",
        "э": "e",
        "ю": "yu",
        "я": "ya",
    }

    MAIN_TRANSLIT_TABLE = convert_table(add_uppercase(_MAIN_TRANSLIT_TABLE))

    _SPECIAL_CASES = {
        "ье": "'ye",
        "ьё": "'ye",
    }

    SPECIAL_CASES = add_uppercase(_SPECIAL_CASES)
    PATTERN1 = re.compile("(?mu)" + "|".join(SPECIAL_CASES.keys()))


class RussianInternationalPassport1997Reduced:
    """
    According to https://en.wikipedia.org/wiki/Romanization_of_Russian#Transliteration_of_the_names_in_Russian_passports
    (International Passport 1997, reduced variant for ий, ый)
    """

    _MAIN_TRANSLIT_TABLE = {
        "а": "a",
        "б": "b",
        "в": "v",
        "г": "g",
        "д": "d",
        "е": "e",
        "ё": "e",
        "ж": "zh",
        "з": "z",
        "и": "i",
        "й": "y",
        "к": "k",
        "л": "l",
        "м": "m",
        "н": "n",
        "о": "o",
        "п": "p",
        "р": "r",
        "с": "s",
        "т": "t",
        "у": "u",
        "ф": "f",
        "х": "kh",
        "ц": "ts",
        "ч": "ch",
        "ш": "sh",
        "щ": "shch",
        "ъ": "'",
        "ы": "y",
        "ь": "",
        "э": "e",
        "ю": "yu",
        "я": "ya",
    }

    MAIN_TRANSLIT_TABLE = convert_table(add_uppercase(_MAIN_TRANSLIT_TABLE))

    _SPECIAL_CASES = {
        "ье": "'ye",
        "ьё": "'ye",
        "ый": "y",
        "ий": "y",
    }

    SPECIAL_CASES = add_uppercase(_SPECIAL_CASES)
    PATTERN1 = re.compile("(?mu)" + "|".join(SPECIAL_CASES.keys()))


class RussianDriverLicense:
    """
    According to https://ru.wikipedia.org/wiki/%D0%A2%D1%80%D0%B0%D0%BD%D1%81%D0%BB%D0%B8%D1%82%D0%B5%D1%80%D0%B0%D1%86%D0%B8%D1%8F_%D1%80%D1%83%D1%81%D1%81%D0%BA%D0%BE%D0%B3%D0%BE_%D0%B0%D0%BB%D1%84%D0%B0%D0%B2%D0%B8%D1%82%D0%B0_%D0%BB%D0%B0%D1%82%D0%B8%D0%BD%D0%B8%D1%86%D0%B5%D0%B9#.D0.A1.D1.80.D0.B0.D0.B2.D0.BD.D0.B8.D1.82.D0.B5.D0.BB.D1.8C.D0.BD.D0.B0.D1.8F_.D1.82.D0.B0.D0.B1.D0.BB.D0.B8.D1.86.D0.B0_.D1.81.D0.B8.D1.81.D1.82.D0.B5.D0.BC_.D1.82.D1.80.D0.B0.D0.BD.D1.81.D0.BB.D0.B8.D1.82.D0.B5.D1.80.D0.B0.D1.86.D0.B8.D0.B8
    (Driver license)
    """

    _MAIN_TRANSLIT_TABLE = {
        "а": "a",
        "б": "b",
        "в": "v",
        "г": "g",
        "д": "d",
        "е": "e",
        "ё": "ye",
        "ж": "zh",
        "з": "z",
        "и": "i",
        "й": "y",
        "к": "k",
        "л": "l",
        "м": "m",
        "н": "n",
        "о": "o",
        "п": "p",
        "р": "r",
        "с": "s",
        "т": "t",
        "у": "u",
        "ф": "f",
        "х": "kh",
        "ц": "ts",
        "ч": "ch",
        "ш": "sh",
        "щ": "shch",
        "ъ": "'",
        "ы": "y",
        "ь": "'",
        "э": "e",
        "ю": "yu",
        "я": "ya",
    }

    MAIN_TRANSLIT_TABLE = convert_table(add_uppercase(_MAIN_TRANSLIT_TABLE))

    _SPECIAL_CASES = {
        # e, ye (В начале слов, а также после гласных и Ь, Ъ)
        "ье": "'ye",
        "ъе": "'ye",
        # e (После согласных Ч, Ш, Щ, Ж),
        # yo (В начале слов, а также после гласных и Ь, Ъ)
        # ye (После согласных, кроме Ч, Ш, Щ, Ж)
        "ьё": "'yo",
        "ъё": "'yo",
        "чё": "che",
        "шё": "she",
        "щё": "shche",
        "жё": "zhe",
        # yi (После Ь)
        "ьи": "'yi",
    }

    _FIRST_CHARACTERS = {
        # ye (В начале слов, а также после гласных и Ь, Ъ)
        "е": "ye",
        # yo (В начале слов, а также после гласных и Ь, Ъ)
        "ё": "yo",
    }

    SPECIAL_CASES = add_uppercase(_SPECIAL_CASES)
    FIRST_CHARACTERS = add_uppercase(_FIRST_CHARACTERS)

    PATTERN1 = re.compile("(?mu)" + "|".join(SPECIAL_CASES.keys()))
    PATTERN2 = re.compile("(?mu)" + r"\b(" + "|".join(FIRST_CHARACTERS.keys()) + ")")



class UkrainianDSTU9112A:
    """
    DSTU 9112:2021 (system A, with diacritics), the State Standard of
    Ukraine for reversible Cyrillic-Latin transliteration, approved in
    April 2022. Based on a modified ISO 9:1995. In-text letter forms;
    verified against the uklatn reference implementation
    (https://github.com/paiv/uklatn). Unlike UkrainianKMU, the standard
    preserves the apostrophe and transliterates the soft sign. Forward
    transliteration only, matching the reference implementation on all
    sequences valid in Ukrainian orthography; for strict lossless
    round-tripping (including degenerate inputs) use uklatn.
    """

    _MAIN_TRANSLIT_TABLE = {
        "а": "a",
        "б": "b",
        "в": "v",
        "г": "\u011f",
        "ґ": "g",
        "д": "d",
        "е": "e",
        "є": "je",
        "ж": "\u017e",
        "з": "z",
        "и": "y",
        "і": "i",
        "ї": "\u00ef",
        "й": "j",
        "к": "k",
        "л": "l",
        "м": "m",
        "н": "n",
        "о": "o",
        "п": "p",
        "р": "r",
        "с": "s",
        "т": "t",
        "у": "u",
        "ф": "f",
        "х": "x",
        "ц": "c",
        "ч": "\u010d",
        "ш": "\u0161",
        "щ": "\u015d",
        "ь": "j",
        "ю": "ju",
        "я": "ja",
        "\u2019": "'",
    }

    MAIN_TRANSLIT_TABLE = convert_table(add_uppercase(_MAIN_TRANSLIT_TABLE))

    # The standard separates й from a preceding consonant with an
    # apostrophe (pid'jom), so that j unambiguously decodes back: plain
    # j after a consonant is ь, 'j is й
    SPECIAL_CASES = {"й": "'j", "Й": "'J"}
    PATTERN1 = re.compile(
        "(?mu)(?<=[бвгґджзклмнпрстфхцчшщБВГҐДЖЗКЛМНПРСТФХЦЧШЩ])[йЙ]")


class UkrainianDSTU9112B:
    """
    DSTU 9112:2021 (system B, ASCII digraphs), the State Standard of
    Ukraine for reversible Cyrillic-Latin transliteration, approved in
    April 2022. System B goes back to the transliteration system
    developed by Maksym Vakulenko for Derzhstandart in 1995. In-text
    letter forms; verified against the uklatn reference implementation
    (https://github.com/paiv/uklatn).
    """

    _MAIN_TRANSLIT_TABLE = {
        "а": "a",
        "б": "b",
        "в": "v",
        "г": "gh",
        "ґ": "g",
        "д": "d",
        "е": "e",
        "є": "je",
        "ж": "zh",
        "з": "z",
        "и": "y",
        "і": "i",
        "ї": "ji",
        "й": "j",
        "к": "k",
        "л": "l",
        "м": "m",
        "н": "n",
        "о": "o",
        "п": "p",
        "р": "r",
        "с": "s",
        "т": "t",
        "у": "u",
        "ф": "f",
        "х": "kh",
        "ц": "c",
        "ч": "ch",
        "ш": "sh",
        "щ": "shch",
        "ь": "j",
        "ю": "ju",
        "я": "ja",
        "\u2019": "'",
    }

    MAIN_TRANSLIT_TABLE = convert_table(add_uppercase(_MAIN_TRANSLIT_TABLE))

    # Same consonant-й apostrophe rule as system A
    SPECIAL_CASES = UkrainianDSTU9112A.SPECIAL_CASES
    PATTERN1 = UkrainianDSTU9112A.PATTERN1


class UkrainianALALC:
    """
    ALA-LC romanization for Ukrainian (American Library Association /
    Library of Congress), used in library catalogs worldwide. Full form,
    with ligature ties (U+0361) and the soft sign as modifier prime.
    """

    _MAIN_TRANSLIT_TABLE = {
        "а": "a",
        "б": "b",
        "в": "v",
        "г": "h",
        "ґ": "g",
        "д": "d",
        "е": "e",
        "є": "i\u0361e",
        "ж": "z\u0361h",
        "з": "z",
        "и": "y",
        "і": "i",
        "ї": "\u00ef",
        "й": "\u012d",
        "к": "k",
        "л": "l",
        "м": "m",
        "н": "n",
        "о": "o",
        "п": "p",
        "р": "r",
        "с": "s",
        "т": "t",
        "у": "u",
        "ф": "f",
        "х": "kh",
        "ц": "t\u0361s",
        "ч": "ch",
        "ш": "sh",
        "щ": "shch",
        "ь": "\u02b9",
        "ю": "i\u0361u",
        "я": "i\u0361a",
    }

    MAIN_TRANSLIT_TABLE = convert_table(add_uppercase(_MAIN_TRANSLIT_TABLE))


class UkrainianALALCModified:
    """
    Simplified ("modified") ALA-LC for Ukrainian: no ligature ties or
    diacritics, soft sign and apostrophe omitted. Not a formal standard,
    but the form widely used in English-language academic publishing.
    """

    _MAIN_TRANSLIT_TABLE = {
        "а": "a",
        "б": "b",
        "в": "v",
        "г": "h",
        "ґ": "g",
        "д": "d",
        "е": "e",
        "є": "ie",
        "ж": "zh",
        "з": "z",
        "и": "y",
        "і": "i",
        "ї": "i",
        "й": "i",
        "к": "k",
        "л": "l",
        "м": "m",
        "н": "n",
        "о": "o",
        "п": "p",
        "р": "r",
        "с": "s",
        "т": "t",
        "у": "u",
        "ф": "f",
        "х": "kh",
        "ц": "ts",
        "ч": "ch",
        "ш": "sh",
        "щ": "shch",
        "ю": "iu",
        "я": "ia",
    }

    MAIN_TRANSLIT_TABLE = convert_table(add_uppercase(_MAIN_TRANSLIT_TABLE))
    # Same soft sign + apostrophes removal as UkrainianKMU
    DELETE_PATTERN = UkrainianKMU.DELETE_PATTERN


class RussianALALC:
    """
    ALA-LC romanization for russian (American Library Association /
    Library of Congress), used in library catalogs worldwide. Full form,
    with ligature ties (U+0361) and modifier primes for the signs.
    """

    _MAIN_TRANSLIT_TABLE = {
        "а": "a",
        "б": "b",
        "в": "v",
        "г": "g",
        "д": "d",
        "е": "e",
        "ё": "\u00eb",
        "ж": "zh",
        "з": "z",
        "и": "i",
        "й": "\u012d",
        "к": "k",
        "л": "l",
        "м": "m",
        "н": "n",
        "о": "o",
        "п": "p",
        "р": "r",
        "с": "s",
        "т": "t",
        "у": "u",
        "ф": "f",
        "х": "kh",
        "ц": "t\u0361s",
        "ч": "ch",
        "ш": "sh",
        "щ": "shch",
        "ъ": "\u02ba",
        "ы": "y",
        "ь": "\u02b9",
        "э": "\u0117",
        "ю": "i\u0361u",
        "я": "i\u0361a",
    }

    MAIN_TRANSLIT_TABLE = convert_table(add_uppercase(_MAIN_TRANSLIT_TABLE))


# The 2019 BGN/PCGN agreement and the 2012 UNGEGN resolution both adopted
# the Ukrainian national (KMU 2010) system as-is
UkrainianBGN2019 = UkrainianKMU
UkrainianUNGEGN = UkrainianKMU


ALL_UKRAINIAN = [
    UkrainianKMU,
    UkrainianSimple,
    UkrainianWWS,
    UkrainianBritish,
    UkrainianBGN,
    UkrainianISO9,
    UkrainianFrench,
    UkrainianGerman,
    UkrainianGOST1971,
    UkrainianGOST1986,
    UkrainianPassport2007,
    UkrainianNational1996,
    UkrainianPassport2004Alt,
    UkrainianDSTU9112A,
    UkrainianDSTU9112B,
    UkrainianALALC,
    UkrainianALALCModified,
]

ALL_RUSSIAN = [
    RussianSimple,
    RussianGOST2006,
    RussianICAO,
    RussianTelegram,
    RussianInternationalPassport1997,
    RussianDriverLicense,
    RussianInternationalPassport1997Reduced,
    RussianISO9SystemB,
    RussianISO9SystemA,
    RussianISOR9Table2,
    RussianALALC,
]

# Backward compatibility
RussianInternationalPassport = RussianInternationalPassport1997

ALL_TRANSLITERATIONS = ALL_UKRAINIAN + ALL_RUSSIAN


def translit(src: str, table: type[TransliterationTable] = UkrainianKMU,
             preserve_case: bool = True) -> str:
    """Transliterates given unicode `src` text
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

    >>> print(translit("Дмитро Згуровський", UkrainianDSTU9112A))
    Dmytro Zğurovsjkyj
    >>> print(translit("Київ, Щастя, підйом", UkrainianDSTU9112A))
    Kyïv, Ŝastja, pid'jom
    >>> print(translit("Дмитро Згуровський", UkrainianDSTU9112B))
    Dmytro Zghurovsjkyj
    >>> print(translit("Київ, Щастя, підйом", UkrainianDSTU9112B))
    Kyjiv, Shchastja, pid'jom
    >>> print(translit("Знам'янка, Щастя", UkrainianALALC))
    Znam'i͡anka, Shchasti͡a
    >>> print(translit("Знам'янка, Щастя", UkrainianALALCModified))
    Znamianka, Shchastia
    >>> print(translit("Юрий Ёлкин, Эрмитаж", RussianALALC))
    I͡uriĭ Ëlkin, Ėrmitazh
    >>> print(translit("Київ", UkrainianBGN2019))
    Kyiv
    """

    src = str(src)
    src_is_upper = src.isupper()

    if hasattr(table, "DELETE_PATTERN"):
        src = table.DELETE_PATTERN.sub("", src)

    if hasattr(table, "PATTERN1"):
        src = table.PATTERN1.sub(lambda x: table.SPECIAL_CASES[x.group()], src)

    if hasattr(table, "PATTERN2"):
        src = table.PATTERN2.sub(lambda x: table.FIRST_CHARACTERS[x.group()], src)
    res = src.translate(table.MAIN_TRANSLIT_TABLE)

    if src_is_upper and preserve_case:
        return res.upper()
    else:
        return res


# For backward compatibility
translitua = translit

__all__ = [
    "translit",
    "TransliterationTable",
    "translitua",
    "UkrainianKMU",
    "UkrainianSimple",
    "UkrainianWWS",
    "RussianGOST2006",
    "RussianSimple",
    "ALL_RUSSIAN",
    "ALL_UKRAINIAN",
    "UkrainianBritish",
    "UkrainianBGN",
    "UkrainianISO9",
    "UkrainianFrench",
    "UkrainianGerman",
    "UkrainianGOST1971",
    "UkrainianGOST1986",
    "UkrainianPassport2007",
    "UkrainianNational1996",
    "UkrainianPassport2004Alt",
    "UkrainianDSTU9112A",
    "UkrainianDSTU9112B",
    "UkrainianALALC",
    "UkrainianALALCModified",
    "UkrainianBGN2019",
    "UkrainianUNGEGN",
    "RussianALALC",
    "RussianICAO",
    "ALL_TRANSLITERATIONS",
    "RussianTelegram",
    "RussianInternationalPassport1997",
    "RussianDriverLicense",
    "RussianInternationalPassport1997Reduced",
    "RussianInternationalPassport",
    "RussianISO9SystemB",
    "RussianISO9SystemA",
    "RussianISOR9Table2",
]


if __name__ == "__main__":
    import doctest

    doctest.testmod()
