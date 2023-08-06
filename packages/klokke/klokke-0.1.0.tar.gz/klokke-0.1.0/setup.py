# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['klokke']

package_data = \
{'': ['*']}

setup_kwargs = {
    'name': 'klokke',
    'version': '0.1.0',
    'description': 'A small library for high level measurement of code execution time',
    'long_description': '# klokke\nklokke is a small library for high level measurement of code execution time. klokke keeps track of running timers, and nests them according to execution order. This allows you to keep track of which sub-sections of code contributes the most to your overall time spent.\nIn addition, a decorator `@timed` is provided for timing function execution.\n\n## Examples\nTiming a snippet of code:\n```python\n>>> from time import sleep\n>>> from klokke import Timer\n>>> with Timer("Something expensive") as timer:\n...     sleep(5)\n... \n>>> print(timer)\nSomething expensive: 5.004069805145264 seconds\n```\n\nNesting timers:\n```python\n>>> from time import sleep\n>>> from klokke import Timer\n>>> with Timer("outer") as outer:\n...     with Timer("inner") as inner:\n...         sleep(1)\n...     sleep(2)\n... \n>>> print(outer)\nouter: 3.0084269046783447 seconds\nOf which:\n  inner: 1.0031757354736328 seconds\n```\n\nUsing a decorator:\n```python\n>>> from time import sleep\n>>> from klokke import Timer, timed\n>>> @timed\n... def foo():\n...     sleep(2)\n...     return 5\n... \n>>> with Timer("bar") as t:\n...     x = foo() + foo()\n... \n>>> print(t)\nbar: 4.010395050048828 seconds\nOf which:\n  __main__.foo: 4.010124683380127 seconds\n```\n\nSetting up timers to automatically print on completion:\n```python\n>>> from time import sleep\n>>> from klokke import Timer\n>>> with Timer("Something expensive", autoprint=print) as timer:\n...     sleep(5)\n... \nSomething expensive: 5.000231981277466 seconds\n```\n\nAll keyword arguments to `Timer` can also be passed through the `@timed` decorator:\n```python\n>>> from time import sleep\n>>> from klokke import timed\n>>> import logging\n>>> logger = logging.getLogger("foo")\n>>> @timed(name="foo_log", autoprint=logger.warning)\n... def foo():\n...     sleep(1)\n... \n>>> foo()\nfoo_log: 1.0042669773101807 seconds\n```\n',
    'author': 'Magnus Heskestad Waage',
    'author_email': 'magnushwaage@gmail.com',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'None',
    'packages': packages,
    'package_data': package_data,
    'python_requires': '>=3.8,<4.0',
}


setup(**setup_kwargs)
