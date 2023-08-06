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
    'version': '0.2.0',
    'description': '',
    'long_description': '# starfield\n\n`starfield` is a Python package that allows you to create `attrs` classes with a single field that can be initialized using variadic positional arguments (i.e. the star `*`). This makes it easier to initialise list-like structures with `attrs` without having to explicitly pass a list to the initializer.\n\n## Installation\n\nTo install `starfield`, run the following command in your terminal:\n\n```bash\npip install starfield\n```\n\n## Examples\n\nThe following example shows how to use `starfield` to create a class that behaves like a list with some extra fields:\n\n```python\nfrom attrs import define, field\nfrom starfield import starfield\n\n\n@define(field_transformer=starfield)\nclass ShoppingList:\n    items: list = field(init="*")\n    store: str = field()\n\n\ngrocery_list = ShoppingList("Milk", "Bread", "Eggs", store="Supermarket")\n```\n\nWithout `starfield`, you would have to explicitly pass a list to the initializer:\n\n```python\nfrom attrs import define, field\n\n\n@define\nclass ShoppingList:\n    items: list = field()\n    store: str = field()\n\n\ngrocery_list = ShoppingList(["Milk", "Bread", "Eggs"], store="Supermarket")\n```\n\nTo illustrate the power of `starfield`, let\'s look at a more complex example involving nested fields. Suppose we want to create a data structure to represent a simple grammatical expression:\n\n```text\n"I" ( "love" | "hate" ) ( "cats" | "dogs" )\n```\n\nWe can define a class to represent this expression with `attrs` and `starfield`:\n\n```python\nfrom attrs import define, field\nfrom starfield import starfield\n\n\n@define(field_transformer=starfield)\nclass And:\n    children: list = field(init="*")\n\n\n@define(field_transformer=starfield)\nclass Or:\n    children: list = field(init="*")\n\n\nexpr = And("I", Or("love", "hate"), Or("cats", "dogs"))\n```\n\nWithout `starfield`, you would have to explicitly pass a list to the initializer:\n\n```python\nfrom attrs import define, field\n\n\n@define\nclass And:\n    children: list = field()\n\n\n@define\nclass Or:\n    children: list = field()\n\n\nexpr = And(["I", Or(["love", "hate"]), Or(["cats", "dogs"])])\n```\n\n## Why Use `starfield`?\n\nNested fields can quickly become unwieldy when initializing objects with `attrs`. `attrs`\'s documentation [explains](https://www.attrs.org/en/stable/init.html#) why it\'s usually better to use a `classmethod` than to modify the initializer. But this can make initialization even more verbose.\n\n`starfield` provides an alternative to using a `classmethod` by allowing you to define a single field that can be initialized using variadic positional arguments (i.e. the star `*`).\n\n\n## Features\n\n- `starfield` will make all non-star fields keyword-only.\n\n- You can still set the star field using a keyword argument (e.g. `expr = And("I", items=[Or("love", "hate"), Or("cats", "dogs")])`).\n\n- To make the string representation of the class more readable, `starfield` adds a `__rich_repr__` method to the class. However, this only works if you\'re using [rich](https://github.com/Textualize/rich) to stringify your objects. To add a `__repr__` method as well, you can pass `repr=True` to `starfield`.\n\n## Limitations\n\n- `starfield` only works with classes that use `attrs`.\n\n- The behaviour of `starfield`\'s `__repr__` method may be inconsistent with the [`attrs`-generated `__repr__` methods](https://github.com/python-attrs/attrs/blob/9fd0f82ff0d632136b95e1b8737b081e537aaaee/src/attr/_make.py#L1833) which are more complicated than one might expect.\n\n## Related Projects\n\n- This feature has been [requested and discussed here](https://github.com/python-attrs/attrs/issues/110). The use of `init="*"` is also proposed. \n\n- [`pydantic`](https://docs.pydantic.dev/usage/models/#custom-root-types)\'s root types serve a similar purpose. Notable, however, a class with a root type cannot have any other fields.\n\nPlease let me know if I\'ve missed any.\n\n## Dependencies\n\n`starfield` requires Python 3.9 or later and `attrs >= 22.2.0`.\n\n## Authors\n\n- [Isaac Breen](https://github.com/IsaacBreen)\n',
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
