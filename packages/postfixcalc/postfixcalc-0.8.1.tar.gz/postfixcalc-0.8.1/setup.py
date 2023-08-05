# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['postfixcalc']

package_data = \
{'': ['*']}

install_requires = \
['black>=22.12.0,<23.0.0']

setup_kwargs = {
    'name': 'postfixcalc',
    'version': '0.8.1',
    'description': 'the stupid postfix evaluator',
    'long_description': '# `postfixcalc`\n\nSimple, stupid but easy and powerful infix expression evaluator using [_postfix_](https://en.wikipedia.org/wiki/Reverse_Polish_notation) notation.\n\n# User Guide\n\n## How to use?\n\n\n```python\nfrom postfixcalc import Calc\n```\n\n\n```python\nexpr = "(-1) ^ 2 + 3 - 4 * 8 - 2 ^ 3"\ncalc = Calc(expr)\n```\n\n\n```python\nprint(calc.answer)\nprint(type(calc.answer))\n```\n\n    -36\n    <class \'int\'>\n\n\n### Explanation\n```\nexpression: (-1) ^ 2 + 3 - 4 * 8 - 2 ^ 3\n```\n\nwhich with the math operator precedence is:\n\n```\nexpression: ((-1) ^ 2) + 3 - (4 * 8) - (2 ^ 3)\n            = (1) + 3 - (32) - (8)\n            = 4 - 32 - 8\n            = -28 - 8\n            = -36\n```\n\n## Initialization\n\n\n```python\ncalc = Calc(\n    \'(2 ^ 32) ^ (2 ^ 15) + -1\',\n    calc_timeout=1,         # timeout for the calculation (in seconds)\n    str_repr_timeout=1.5    # timeout to generate the string representation (in seconds)\n)\n```\n\n\n```python\nprint(f"\'(2 ^ 32) ^ (2 ^ 15)\'s answer has \'{len(calc.stranswer)}\' digits")\n```\n\n    \'(2 ^ 32) ^ (2 ^ 15)\'s answer has \'315653\' digits\n\n\n\n```python\nprint(f\'answer is: {calc.stranswer[:5]}...{calc.stranswer[-5:]}\')\n```\n\n    answer is: 67411...79135\n\n\n## Other Attributes\n\n\n```python\nfrom rich.pretty import Pretty\nfrom rich import print as rprint\n```\n\n\n```python\nrprint(calc.parsed)\n```\n\n\n<pre style="white-space:pre;overflow-x:auto;line-height:normal;font-family:Menlo,\'DejaVu Sans Mono\',consolas,\'Courier New\',monospace"><span style="font-weight: bold">&lt;</span><span style="color: #ff00ff; text-decoration-color: #ff00ff; font-weight: bold">ast.BinOp</span><span style="color: #000000; text-decoration-color: #000000"> object at </span><span style="color: #008080; text-decoration-color: #008080; font-weight: bold">0x7f93380b1330</span><span style="font-weight: bold">&gt;</span>\n</pre>\n\n\n\n\n```python\nrprint(calc.extracted)\n```\n\n\n<pre style="white-space:pre;overflow-x:auto;line-height:normal;font-family:Menlo,\'DejaVu Sans Mono\',consolas,\'Courier New\',monospace"><span style="font-weight: bold">[</span>\n    <span style="font-weight: bold">(</span>\n        <span style="font-weight: bold">[</span>\n            <span style="font-weight: bold">(</span>\n                <span style="font-weight: bold">[([</span><span style="color: #008080; text-decoration-color: #008080; font-weight: bold">2</span><span style="font-weight: bold">]</span>, <span style="font-weight: bold">&lt;</span><span style="color: #ff00ff; text-decoration-color: #ff00ff; font-weight: bold">ast.Pow</span><span style="color: #000000; text-decoration-color: #000000"> object at </span><span style="color: #008080; text-decoration-color: #008080; font-weight: bold">0x7f933cc8d150</span><span style="font-weight: bold">&gt;</span>, <span style="font-weight: bold">[</span><span style="color: #008080; text-decoration-color: #008080; font-weight: bold">32</span><span style="font-weight: bold">])]</span>,\n                <span style="font-weight: bold">&lt;</span><span style="color: #ff00ff; text-decoration-color: #ff00ff; font-weight: bold">ast.Pow</span><span style="color: #000000; text-decoration-color: #000000"> object at </span><span style="color: #008080; text-decoration-color: #008080; font-weight: bold">0x7f933cc8d150</span><span style="font-weight: bold">&gt;</span>,\n                <span style="font-weight: bold">[([</span><span style="color: #008080; text-decoration-color: #008080; font-weight: bold">2</span><span style="font-weight: bold">]</span>, <span style="font-weight: bold">&lt;</span><span style="color: #ff00ff; text-decoration-color: #ff00ff; font-weight: bold">ast.Pow</span><span style="color: #000000; text-decoration-color: #000000"> object at </span><span style="color: #008080; text-decoration-color: #008080; font-weight: bold">0x7f933cc8d150</span><span style="font-weight: bold">&gt;</span>, <span style="font-weight: bold">[</span><span style="color: #008080; text-decoration-color: #008080; font-weight: bold">15</span><span style="font-weight: bold">])]</span>\n            <span style="font-weight: bold">)</span>\n        <span style="font-weight: bold">]</span>,\n        <span style="font-weight: bold">&lt;</span><span style="color: #ff00ff; text-decoration-color: #ff00ff; font-weight: bold">ast.Add</span><span style="color: #000000; text-decoration-color: #000000"> object at </span><span style="color: #008080; text-decoration-color: #008080; font-weight: bold">0x7f933cc8cf10</span><span style="font-weight: bold">&gt;</span>,\n        <span style="font-weight: bold">[(&lt;</span><span style="color: #ff00ff; text-decoration-color: #ff00ff; font-weight: bold">ast.USub</span><span style="color: #000000; text-decoration-color: #000000"> object at </span><span style="color: #008080; text-decoration-color: #008080; font-weight: bold">0x7f933cc8d570</span><span style="font-weight: bold">&gt;</span>, <span style="font-weight: bold">[</span><span style="color: #008080; text-decoration-color: #008080; font-weight: bold">1</span><span style="font-weight: bold">])]</span>\n    <span style="font-weight: bold">)</span>\n<span style="font-weight: bold">]</span>\n</pre>\n\n\n\n\n```python\nrprint(calc.flattened)\n```\n\n\n<pre style="white-space:pre;overflow-x:auto;line-height:normal;font-family:Menlo,\'DejaVu Sans Mono\',consolas,\'Courier New\',monospace"><span style="font-weight: bold">(</span>\n    <span style="font-weight: bold">(</span>\n        <span style="font-weight: bold">(([</span><span style="color: #008080; text-decoration-color: #008080; font-weight: bold">2</span><span style="font-weight: bold">]</span>, <span style="font-weight: bold">&lt;</span><span style="color: #ff00ff; text-decoration-color: #ff00ff; font-weight: bold">ast.Pow</span><span style="color: #000000; text-decoration-color: #000000"> object at </span><span style="color: #008080; text-decoration-color: #008080; font-weight: bold">0x7f933cc8d150</span><span style="font-weight: bold">&gt;</span>, <span style="font-weight: bold">[</span><span style="color: #008080; text-decoration-color: #008080; font-weight: bold">32</span><span style="font-weight: bold">])</span>,<span style="font-weight: bold">)</span>,\n        <span style="font-weight: bold">&lt;</span><span style="color: #ff00ff; text-decoration-color: #ff00ff; font-weight: bold">ast.Pow</span><span style="color: #000000; text-decoration-color: #000000"> object at </span><span style="color: #008080; text-decoration-color: #008080; font-weight: bold">0x7f933cc8d150</span><span style="font-weight: bold">&gt;</span>,\n        <span style="font-weight: bold">(([</span><span style="color: #008080; text-decoration-color: #008080; font-weight: bold">2</span><span style="font-weight: bold">]</span>, <span style="font-weight: bold">&lt;</span><span style="color: #ff00ff; text-decoration-color: #ff00ff; font-weight: bold">ast.Pow</span><span style="color: #000000; text-decoration-color: #000000"> object at </span><span style="color: #008080; text-decoration-color: #008080; font-weight: bold">0x7f933cc8d150</span><span style="font-weight: bold">&gt;</span>, <span style="font-weight: bold">[</span><span style="color: #008080; text-decoration-color: #008080; font-weight: bold">15</span><span style="font-weight: bold">])</span>,<span style="font-weight: bold">)</span>\n    <span style="font-weight: bold">)</span>,\n    <span style="font-weight: bold">&lt;</span><span style="color: #ff00ff; text-decoration-color: #ff00ff; font-weight: bold">ast.Add</span><span style="color: #000000; text-decoration-color: #000000"> object at </span><span style="color: #008080; text-decoration-color: #008080; font-weight: bold">0x7f933cc8cf10</span><span style="font-weight: bold">&gt;</span>,\n    <span style="font-weight: bold">(&lt;</span><span style="color: #ff00ff; text-decoration-color: #ff00ff; font-weight: bold">ast.USub</span><span style="color: #000000; text-decoration-color: #000000"> object at </span><span style="color: #008080; text-decoration-color: #008080; font-weight: bold">0x7f933cc8d570</span><span style="font-weight: bold">&gt;</span>, <span style="font-weight: bold">[</span><span style="color: #008080; text-decoration-color: #008080; font-weight: bold">1</span><span style="font-weight: bold">])</span>\n<span style="font-weight: bold">)</span>\n</pre>\n\n\n\n\n```python\nrprint(calc.strparenthesized)\n```\n\n\n<pre style="white-space:pre;overflow-x:auto;line-height:normal;font-family:Menlo,\'DejaVu Sans Mono\',consolas,\'Courier New\',monospace"><span style="font-weight: bold">(((</span><span style="color: #008080; text-decoration-color: #008080; font-weight: bold">2</span> ^ <span style="color: #008080; text-decoration-color: #008080; font-weight: bold">32</span><span style="font-weight: bold">))</span> ^ <span style="font-weight: bold">((</span><span style="color: #008080; text-decoration-color: #008080; font-weight: bold">2</span> ^ <span style="color: #008080; text-decoration-color: #008080; font-weight: bold">15</span><span style="font-weight: bold">)))</span> + <span style="font-weight: bold">(</span><span style="color: #008080; text-decoration-color: #008080; font-weight: bold">-1</span><span style="font-weight: bold">)</span>\n</pre>\n\n\n\n\n```python\nrprint(calc.listparenthesized)\n```\n\n\n<pre style="white-space:pre;overflow-x:auto;line-height:normal;font-family:Menlo,\'DejaVu Sans Mono\',consolas,\'Courier New\',monospace"><span style="font-weight: bold">[</span><span style="color: #008000; text-decoration-color: #008000">\'(\'</span>, <span style="color: #008000; text-decoration-color: #008000">\'(\'</span>, <span style="color: #008000; text-decoration-color: #008000">\'(\'</span>, <span style="color: #008080; text-decoration-color: #008080; font-weight: bold">2</span>, <span style="color: #008000; text-decoration-color: #008000">\'^\'</span>, <span style="color: #008080; text-decoration-color: #008080; font-weight: bold">32</span>, <span style="color: #008000; text-decoration-color: #008000">\')\'</span>, <span style="color: #008000; text-decoration-color: #008000">\')\'</span>, <span style="color: #008000; text-decoration-color: #008000">\'^\'</span>, <span style="color: #008000; text-decoration-color: #008000">\'(\'</span>, <span style="color: #008000; text-decoration-color: #008000">\'(\'</span>, <span style="color: #008080; text-decoration-color: #008080; font-weight: bold">2</span>, <span style="color: #008000; text-decoration-color: #008000">\'^\'</span>, <span style="color: #008080; text-decoration-color: #008080; font-weight: bold">15</span>, <span style="color: #008000; text-decoration-color: #008000">\')\'</span>, <span style="color: #008000; text-decoration-color: #008000">\')\'</span>, <span style="color: #008000; text-decoration-color: #008000">\')\'</span>, <span style="color: #008000; text-decoration-color: #008000">\'+\'</span>, <span style="color: #008000; text-decoration-color: #008000">\'(\'</span>, <span style="color: #008000; text-decoration-color: #008000">\'-1\'</span>, <span style="color: #008000; text-decoration-color: #008000">\')\'</span><span style="font-weight: bold">]</span>\n</pre>\n\n\n\n\n```python\nrprint(calc.numerized)\n```\n\n\n<pre style="white-space:pre;overflow-x:auto;line-height:normal;font-family:Menlo,\'DejaVu Sans Mono\',consolas,\'Courier New\',monospace"><span style="font-weight: bold">[</span><span style="color: #008000; text-decoration-color: #008000">\'(\'</span>, <span style="color: #008000; text-decoration-color: #008000">\'(\'</span>, <span style="color: #008000; text-decoration-color: #008000">\'(\'</span>, <span style="color: #008080; text-decoration-color: #008080; font-weight: bold">2</span>, <span style="color: #008000; text-decoration-color: #008000">\'^\'</span>, <span style="color: #008080; text-decoration-color: #008080; font-weight: bold">32</span>, <span style="color: #008000; text-decoration-color: #008000">\')\'</span>, <span style="color: #008000; text-decoration-color: #008000">\')\'</span>, <span style="color: #008000; text-decoration-color: #008000">\'^\'</span>, <span style="color: #008000; text-decoration-color: #008000">\'(\'</span>, <span style="color: #008000; text-decoration-color: #008000">\'(\'</span>, <span style="color: #008080; text-decoration-color: #008080; font-weight: bold">2</span>, <span style="color: #008000; text-decoration-color: #008000">\'^\'</span>, <span style="color: #008080; text-decoration-color: #008080; font-weight: bold">15</span>, <span style="color: #008000; text-decoration-color: #008000">\')\'</span>, <span style="color: #008000; text-decoration-color: #008000">\')\'</span>, <span style="color: #008000; text-decoration-color: #008000">\')\'</span>, <span style="color: #008000; text-decoration-color: #008000">\'+\'</span>, <span style="color: #008000; text-decoration-color: #008000">\'(\'</span>, <span style="color: #008080; text-decoration-color: #008080; font-weight: bold">-1</span>, <span style="color: #008000; text-decoration-color: #008000">\')\'</span><span style="font-weight: bold">]</span>\n</pre>\n\n\n\n\n```python\nrprint(calc.postfix)\n```\n\n\n<pre style="white-space:pre;overflow-x:auto;line-height:normal;font-family:Menlo,\'DejaVu Sans Mono\',consolas,\'Courier New\',monospace"><span style="font-weight: bold">[</span><span style="color: #008080; text-decoration-color: #008080; font-weight: bold">2</span>, <span style="color: #008080; text-decoration-color: #008080; font-weight: bold">32</span>, <span style="color: #008000; text-decoration-color: #008000">\'^\'</span>, <span style="color: #008080; text-decoration-color: #008080; font-weight: bold">2</span>, <span style="color: #008080; text-decoration-color: #008080; font-weight: bold">15</span>, <span style="color: #008000; text-decoration-color: #008000">\'^\'</span>, <span style="color: #008000; text-decoration-color: #008000">\'^\'</span>, <span style="color: #008080; text-decoration-color: #008080; font-weight: bold">-1</span>, <span style="color: #008000; text-decoration-color: #008000">\'+\'</span><span style="font-weight: bold">]</span>\n</pre>\n\n\n\n\n```python\nrprint(f\'{calc.stranswer[:5]}...{calc.stranswer[-5:]}\')\n```\n\n\n<pre style="white-space:pre;overflow-x:auto;line-height:normal;font-family:Menlo,\'DejaVu Sans Mono\',consolas,\'Courier New\',monospace"><span style="color: #008080; text-decoration-color: #008080; font-weight: bold">67411</span><span style="color: #808000; text-decoration-color: #808000">...</span><span style="color: #008080; text-decoration-color: #008080; font-weight: bold">79135</span>\n</pre>\n\n\n\n# `Calc` Documentation\n',
    'author': 'Mahdi Haghverdi',
    'author_email': 'mahdihaghverdiliewpl@gmail.com',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'None',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.10,<4.0',
}


setup(**setup_kwargs)
