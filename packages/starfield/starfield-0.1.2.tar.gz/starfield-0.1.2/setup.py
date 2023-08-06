# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['starfield']

package_data = \
{'': ['*']}

install_requires = \
['attrs>=22.2.0,<23.0.0']

setup_kwargs = {
    'name': 'starfield',
    'version': '0.1.2',
    'description': '',
    'long_description': 'Lets you define `attrs` classes with a single non-keyword-only field that can be initialised using\nvar-positional (i.e. star `*`) arguments.\n\n## Installation\n\n```bash\npip install starfield\n```\n\n## Usage\n\n```python\nfrom attrs import define, field\nfrom starfield import starfield\n\n\n@define(field_transformer=starfield)\nclass SantaList:\n    names: list = field(init="*")\n    is_naughty_list: bool = field()\n\n\nnaughty_list = SantaList("Bob", "Alice", is_naughty_list=True)\n```\n\n## Why?\n\nSometimes you want to define a class that behaves like a list with some extra fields.\nWithout an initializer with var-positional arguments, you would have to explicitly pass a list to the initializer:\n\n```python\nfrom attrs import define, field\n\n\n@define\nclass SantaList:\n    names: list = field()\n    is_naughty_list: bool = field()\n\n\nnaughty_list = SantaList(["Bob", "Alice"], is_naughty_list=True)\n```\n\nThis can get messy, especially if you have lots of nested fields.\n\n`attrs`\'s documentation [recommends](https://www.attrs.org/en/stable/init.html#) explains why it\'s usually better to use a `classmethod` than to\nmodify the initializer.\n\n> Passing complex objects into __init__ and then using them to derive data for the class unnecessarily couples your new class with the old class which makes it harder to test and also will cause problems later.\n\n> Generally speaking, the moment you think that you need finer control over how your class is instantiated than what attrs offers, it’s usually best to use a classmethod factory or to apply the builder pattern.\n\n\n\n### Nested fields\n\nTo motivate `starfield` more strongly, let\'s look at a more complex example involving nested fields.\n\nSuppose we want to create a data structure to represent a simple grammatical expression:\n\n```text\n"I" ( "love" | "hate" ) ( "cats" | "dogs" )\n```\n\nWe can define a class to represent this expression with `attrs`:\n\n```python\nfrom attrs import define, field\n\n\n@define\nclass And:\n    children: list = field()\n\n\n@define\nclass Or:\n    children: list = field()\n\n\nexpr = And(["I", Or(["love", "hate"]), Or(["cats", "dogs"])])\n```\n\nThis works but it\'s a bit awkward to have to manually pass the list at every level.\n\nUsing `starfield` we can define the same class but with a much simpler initializer:\n\n```python\nfrom attrs import define, field\nfrom starfield import starfield\n\n\n@define(field_transformer=starfield)\nclass And:\n    children: list = field(init="*")\n\n\n@define(field_transformer=starfield)\nclass Or:\n    children: list = field(init="*")\n\n\nexpr = And("I", Or("love", "hate"), Or("cats", "dogs"))\n```\n\n## How?\n\nThe `starfield` adds to the class an `__init__` method that accepts variadic positional arguments.\nThe `__init__` method calls `__attrs_init__` with the variadic positional arguments passed as a tuple to the field with `init="*"`.\n\n### String representation\n\nTo make the string representation of the class more readable, `starfield` also adds a `__rich_repr__` method to the class. However, this only works if you\'re using [rich](https://github.com/Textualize/rich) to stringify your objects.\n\nTo add a `__repr__` method as well, you can pass `repr=True` to `starfield`.\nHowever, its behaviour may be inconsistent with the [`attrs`-generated `__repr__` methods](https://github.com/python-attrs/attrs/blob/9fd0f82ff0d632136b95e1b8737b081e537aaaee/src/attr/_make.py#L1833)\nwhich are more complicated than one might expect (and may change without warning - hence why `starfield` doesn\'t touch it unless you explicitly ask it to).\n\n## Notes\n\n- `starfield` will make all non-star fields keyword-only.\n\n- You can still set the star field using a keyword argument (e.g. `SantaList(names=["Bob", "Alice"], is_naughty_list=True)`).\n\n## Similar projects\n\n- This feature has been [requested and discussed here](https://github.com/python-attrs/attrs/issues/110). The use of `init="*"` is also proposed. \n\n- [`pydantic`](https://docs.pydantic.dev/usage/models/#custom-root-types)\'s root types serve a similar purpose. Notable, however, a class with a root type cannot have any other fields.\n\nPlease let me know if I\'ve missed any.',
    'author': 'IsaacBreen',
    'author_email': '57783927+IsaacBreen@users.noreply.github.com',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'None',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.9,<4.0',
}


setup(**setup_kwargs)
