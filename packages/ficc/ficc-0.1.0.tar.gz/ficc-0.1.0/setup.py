# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['ficc']

package_data = \
{'': ['*']}

install_requires = \
['factorio-draftsman>=1.0.2,<2.0.0']

entry_points = \
{'console_scripts': ['ficc = ficc.__main__:main']}

setup_kwargs = {
    'name': 'ficc',
    'version': '0.1.0',
    'description': 'Generates factorio blueprints for inserter clocks.',
    'long_description': 'Factorio Inserter Clock Creator ("ficc")\n========================================\n\nGenerates factorio blueprints for inserter clocks. Automates an\nalgorithm from this `video guide <https://www.youtube.com/watch?v=kHvqxKLXs54>`__ by KnightElite.\n\nInstallation\n------------\n\n.. code:: console\n\n   pip install ficc\n\nUsage\n-----\n\n.. code:: console\n\n   $ ficc --help\n   usage: ficc [-h] --rate RATE [--stack STACK]\n\n   Generates factorio blueprints for inserter clocks.\n\n   options:\n     -h, --help            show this help message and exit\n     --rate RATE, -r RATE  Count of items to be carried per second (float) (default: None)\n     --stack STACK, -s STACK\n                           The item or inserter stack size, whichever is lower (default: 12)\n\nCalculate how many items per second you need your inserter to move. (A\ntool like `Rate Calculator <https://mods.factorio.com/mod/RateCalculator>`__ mod or\n`Factorio Lab <https://factoriolab.github.io/>`__ is recommended.) Pass\nthat value to the ``--rate`` argument. For example, iron plates (as\nshown in the `video guide <https://www.youtube.com/watch?v=kHvqxKLXs54>`__):\n\n.. code:: console\n\n   $ python3 -m ficc --rate \'5.025\'\n   0eNq1U8tO5DAQ/JWopb2Z2YmZB+TKac97hFXkJB1okdhR2xkxO8q/b9sZHtICAxJIkSPb5arqcvsAVTfiwGQDFAeggD0UL9YU7JA9OQuFvshX20u9XW/kW10o6EyFnaCvOlffC7JBXzMNIaHhl/XIATmr43bWOs7Wi6VeZ1HDZz8zj7WzzeLG/g5GAJ7+YpHlWojQBgqEHorrA1jTo9AJ1gdjw1nt+oqsCY4FOThPs94BHqBYLpYK9uk/iR9irOddrSKBnac+ovM43DKiTSpJcl9SM2OJ65FCmubTn2lKxwO7rqzwzuxIxOV4S50UONsk26A4yCNyjGFutgo83VrTReixinnh7Eqsh/0QV3bEYRTMJDLq0YYd+wo5aquno4Yp3PUYqH43Av0VEUjNChibE9Ho5FlHmtPgxPmq2vmHA3/OoIy9Q0+ltMQ+lJ+JW4EbkM2xWX8IYu7H8rHRoLjcLCVLN4Zh/Bz39P9N6hc32WBNDfK717j6hk7Wbwd7tPQFqUpRg+FUVAE3o9abFSh4DjU+ixORNi68QT3sy/S6ypZdX5IVFiha03l8JfLzWO4/XWio4w==\n\nIf you don’t have full stack size research or your recipe has a limited\nstack size, you will need to account for that. For example, if you\nwanted to clock unloading Rocket Fuel out of a fully moduled and\nbeaconed Assembler 3:\n\n.. code:: console\n\n   $ python3 -m ficc --rate \'0.4\' --stack 10\n   0eNq1U11vnDAQ/Ctopb45V3DIR3nNU5/zmFTIwJKsCjZam1OvJ/571+aSntQkl0iphADb45nZ8XoPzTDjxGQDVHuggCNUR3MKtsienIVKXxfl1Td9dXEpT3mtYDANDoK+GVz7U5Ad+pZpCgkN361HDshZG5ez3nGWb8osKvjsa+axdbbb3NvbYGTZ02+ssiIXGrSBAqGH6m4P1owoZIL1wdhw1rqxIWuCY0FOztOqtodfUOWbXMEufRdxQ4ztuqpVJLDr0Ed0EV8PjGiTSpLc1dStWOJ2ppCGxfJjWdL2wG6oG3w0WxJx2d7TIOWtNsl2KA6KiJxjlPLn6cGaISIPRawTZzfiPOymOLMlDrNgFlFRTy7sPDbIUVo9bzVM4XHEQO2bCejPSEBKVsDYnUhGJ8860pwGJ84X1c7fnfffDOrYOvRcSk/sQ/2RuBW4CdkcOvWLINZ2rJ/6TIxc5JKlm8M0f4x7+fck9dFJdthSh/zmMZb/oZH168EeLH1CqlLUZDgVVcH9rPVlCQqOQj2ZaOfCK8zTrk53q+7ZjTVZYYGqN4PHFxI/j9X+AU9dp/g=\n\nDevelopment\n-----------\n\nYou need `poetry <https://python-poetry.org/>`__:\n\n.. code:: console\n\n   poetry install && poetry shell\n',
    'author': 'Ryan Delaney',
    'author_email': 'ryan.patrick.delaney+git@protonmail.com',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'https://pypi.org/project/ficc',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'entry_points': entry_points,
    'python_requires': '>=3.10,<4.0',
}


setup(**setup_kwargs)
