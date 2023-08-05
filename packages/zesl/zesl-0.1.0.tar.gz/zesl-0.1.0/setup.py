# -*- coding: utf-8 -*-
from setuptools import setup

modules = \
['zesl']
install_requires = \
['lark>=1.1.5,<2.0.0']

setup_kwargs = {
    'name': 'zesl',
    'version': '0.1.0',
    'description': "Zayne's Extremely Simple Language",
    'long_description': '<p align="center">\n  <img src="https://user-images.githubusercontent.com/66521670/209605632-24e913e6-aa9b-4515-8b27-906b60b7695f.svg" />\n</p>\n\n# ***Zayne\'s Extremely Simple Language***\nInspired by **Tom\'s Obvious Minimal Language (TOML)** and **YAML**\n\nThis project isn\'t serious btw; This was just a side project 👀.\n**ZESL** won\'t be getting regularly scheduled updates.\n\n## **Grammar**\n**ZESL** uses the **BNF** grammar format. It\'s grammar is as follows:\n```bnf\n<program> ::= <statement>\n\n<statement> ::= <key>\n| <comment>\n\n<letter> ::= "A" | "B" | "C" | "D" | "E" | "F" | "G"\n       | "H" | "I" | "J" | "K" | "L" | "M" | "N"\n       | "O" | "P" | "Q" | "R" | "S" | "T" | "U"\n       | "V" | "W" | "X" | "Y" | "Z" | "a" | "b"\n       | "c" | "d" | "e" | "f" | "g" | "h" | "i"\n       | "j" | "k" | "l" | "m" | "n" | "o" | "p"\n       | "q" | "r" | "s" | "t" | "u" | "v" | "w"\n       | "x" | "y" | "z" \n\n<digit> ::= "0" | "1" | "2" | "3" | "4" | "5"\n\t   | "6" | "7" | "8" | "9"\n\n<symbol> ::=  "|" | " " | "!" | "#" | "$" | "%" | "&" | "(" | ")" | "*" | "+" | "," | "-" | "." | "/" | ":" | ";" | ">" | "=" | "<" | "?" | "@" | "[" | "\\\\" | "]" | "^" | "_" | "`" | "{" | "}" | "~"\n\n<comment> ::= ">" " "* (<digit> | <letter> | " " | <symbol>)+\n<value> ::= "\\"" (<digit> | <letter> | " " | <symbol>)* "\\"" | <digit>+ | "."* <digit>+ "."* <digit>*\n<key> ::= <letter>+ "=" <value> " "* <comment>*\n```\n\n## **Syntax**\n**ZESL** supports strings, integers, and floats. **ZESL** also support usage of comments.\n```\n> This is a comment.\ncity="Salt Lake City, Utah"\narea=801\nprecipitation=50.0\n```\nThere are multiple ways to type a value, however there\'re some *big* **no-no(s)**.\n\n----\n\n#### The correct way to enclose an string in **ZESL** would be in *double quotes*. Attempting to use single quotes will result in an error.\n```\nquote=\'Do not fear mistakes. There are none. (Miles Davis)\' > Wrong way to write strings.\nquote="Do not fear mistakes. There are none. (Miles Davis)" > Correct way to write strings. Note the double quotes.\n```\n\n# Goals\n\nIf I do decide to at least dedicate **SOME** of my time to this project, here\'s what I would do.\n- Improve BNF grammar. Adding double-quotes and/or back-ticks for string would be nice. Make context a bit more loose.\n- Add `[]` and `{}`, allows for defining dicts and/or lists.\n- Syntax sugar!?\n',
    'author': 'Zayne Marsh',
    'author_email': 'None',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'None',
    'py_modules': modules,
    'install_requires': install_requires,
    'python_requires': '>=3.4,<4.0',
}


setup(**setup_kwargs)
