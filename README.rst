translit-ua
===========

Transliteration (romanization, latinization) for ukrainian language that uses rules officialy approved
by The Cabinet. Translit-ua works with python 2.6+ and python 3+ and has doctests.

Installation
==================================
Install from PyPI.

.. code-block:: none

    $ pip install translitua

Usage
==================================

.. code-block:: python

    from translitua import translitua

    translitua(
        u"""Берег моря. Чути розбещенi крики морських птахiв, ревiння моржа,
    а також iншi звуки, iздаваємиє різною морською сволотою. Входить Гамлєт,
    вдягнутий в зручну приємну товстовку і такі ж самі парусинові штани.
    Гамлєт красиво підперезаний вузеньким шкіряним пояском.
    Він босий, бородатий і пацаватий. В руках у нього дебелий дрючок.
    """)



More about `Ukrainian National transliteration`_

.. _Ukrainian National transliteration: http://en.wikipedia.org/wiki/Romanization_of_Ukrainian
