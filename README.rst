translit-ua
===========

Transliteration (romanization, latinization) for ukrainian and russian languages with variety of transliteration tables (including official ones).
Translit-ua has 13 transliteration tables for Ukrainian language:

- UkrainianKMU (National 2010, most recent one approved by The Cabinet)
- UkrainianSimple (Simple one)
- UkrainianWWS (WWS or Woodrow Wilson School or Scholarly)
- UkrainianBritish (British Standard)
- UkrainianBGN (BGN/PGGN 1965 System, United States Board on Geographic Names/Permanent Committee on Geographical Names)
- UkrainianISO9 (ISO 9, from International Organization for Standardization)
- UkrainianFrench (Jean Girodet (1976), Dictionnaire de la langue française)
- UkrainianGerman ((2000) Duden, v 22, Mannheim: Dudenverlag.)
- UkrainianGOST1971 (The Soviet Union's GOST from 1971)
- UkrainianGOST1986 (The Soviet Union's GOST from 1986)
- UkrainianPassport2007 (Used in Ukrainian passport in 2007-2010)
- UkrainianNational1996 (Codified by Committee on Issues of Legal Terminology in 1996)
- UkrainianPassport2004Alt (Yet another alternative that was sometimes used in Ukrainian passport in 2004-2007)


Translit-ua works with python 2.6+ and python 3+ and has doctests.

Installation
==================================
Install from PyPI.

.. code-block:: none

    $ pip install translitua

Usage
==================================

.. code-block:: python

    from translitua import translit

    translit(
        u"""Берег моря. Чути розбещенi крики морських птахiв, ревiння моржа,
    а також iншi звуки, iздаваємиє різною морською сволотою. Входить Гамлєт,
    вдягнутий в зручну приємну товстовку і такі ж самі парусинові штани.
    Гамлєт красиво підперезаний вузеньким шкіряним пояском.
    Він босий, бородатий і пацаватий. В руках у нього дебелий дрючок.
    """)



More about `Ukrainian transliteration`_

More about `Russian transliteration`_

.. _Ukrainian transliteration: http://en.wikipedia.org/wiki/Romanization_of_Ukrainian
.. _Russian transliteration: https://ru.wikipedia.org/wiki/%D0%A2%D1%80%D0%B0%D0%BD%D1%81%D0%BB%D0%B8%D1%82%D0%B5%D1%80%D0%B0%D1%86%D0%B8%D1%8F_%D1%80%D1%83%D1%81%D1%81%D0%BA%D0%BE%D0%B3%D0%BE_%D0%B0%D0%BB%D1%84%D0%B0%D0%B2%D0%B8%D1%82%D0%B0_%D0%BB%D0%B0%D1%82%D0%B8%D0%BD%D0%B8%D1%86%D0%B5%D0%B9
