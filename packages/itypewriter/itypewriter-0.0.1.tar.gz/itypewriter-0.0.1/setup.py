# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['itypewriter']

package_data = \
{'': ['*']}

setup_kwargs = {
    'name': 'itypewriter',
    'version': '0.0.1',
    'description': 'iTypewriter - print text a character at a time,like typewriting.',
    'long_description': '### iTypeWriter\n+ A simple package for printing and displaying characters one at a time as if you were typing.\n+ With `itypewriter` you can display values as if you were typing a text.\n\n\n#### Installation\n```bash\npip install itypewriter\n```\n\n#### Usage\n`itypewriter` can be used either via the functional approach or via the object oriented approach.\n\n##### Via Functional Approach\n```python\n>>> import itypewriter\n>>> itypewriter.itype("Hello Sentient Typing")\n\n```\n\nThere is also the `iprint` option\n```python\n>>> from itypewriter import iprint\n>>> iprint("Hello Sentient Typing")\n\n>>> iprint("Hello",num_of_chars=3)\n```\n\nEach of these functions accepts optional params for customising the number of characters (`num_of_chars`)\nand the delay inbetween the appearance of characters (`delay`).\n\n##### Specifying the Delay Time\n\n```python\n>>> from itypewriter import iprint\n>>> iprint("Hello Sentient Typing",delay=0.2)\n```\n\n#### OOP Approach\n```python\n>>> from itypewriter import TypeText\n>>> docx = """Some wonderful text"""\n>>> tt = TypeText(docx,num_of_chars=1)\n>>> tt.iprint()\n```\n',
    'author': 'Jesse E.Agbe(JCharis)',
    'author_email': 'jcharistech@gmail.com',
    'maintainer': None,
    'maintainer_email': None,
    'url': 'https://github.com/Jcharis/itypewriter',
    'packages': packages,
    'package_data': package_data,
    'python_requires': '>=3.10,<4.0',
}


setup(**setup_kwargs)
