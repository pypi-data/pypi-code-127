# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['pytest_lambda']

package_data = \
{'': ['*']}

install_requires = \
['pytest>=3.6,<8', 'wrapt>=1.11.0,<2.0.0']

entry_points = \
{'pytest11': ['lambda = pytest_lambda.plugin']}

setup_kwargs = {
    'name': 'pytest-lambda',
    'version': '2.0.0',
    'description': 'Define pytest fixtures with lambda functions.',
    'long_description': "# pytest-lambda\n\nDefine pytest fixtures with lambda functions.\n\n\n# Quickstart\n\n```bash\npip install pytest-lambda\n```\n\n```python\n# test_the_namerator.py\n\nfrom pytest_lambda import lambda_fixture, static_fixture\n\nfirst = static_fixture('John')\nmiddle = static_fixture('Jacob')\nlast = static_fixture('Jingleheimer-Schmidt')\n\n\nfull_name = lambda_fixture(lambda first, middle, last: f'{first} {middle} {last}')\n\n\ndef test_the_namerator(full_name):\n    assert full_name == 'John Jacob Jingleheimer-Schmidt'\n```\n\n\n# Cheatsheet\n\n ```python\nimport asyncio\nimport pytest\nfrom pytest_lambda import (\n    disabled_fixture,\n    error_fixture,\n    lambda_fixture,\n    not_implemented_fixture,\n    static_fixture,\n)\n\n# Basic usage\nfixture_name = lambda_fixture(lambda other_fixture: 'expression', scope='session', autouse=True)\n\n# Async fixtures (awaitables automatically awaited) — requires an async plugin, like pytest-asyncio\nfixture_name = lambda_fixture(lambda: asyncio.sleep(0, 'expression'), async_=True)\n\n# Request fixtures by name\nfixture_name = lambda_fixture('other_fixture')\nfixture_name = lambda_fixture('other_fixture', 'another_fixture', 'cant_believe_its_not_fixture')\n\n# Reference `self` inside a class\nclass TestContext:\n    fixture_name = lambda_fixture(lambda self: self.__class__.__name__, bind=True)\n\n# Parametrize\nfixture_name = lambda_fixture(params=['a', 'b'])\nfixture_name = lambda_fixture(params=['a', 'b'], ids=['A!', 'B!'])\nfixture_name = lambda_fixture(params=[pytest.param('a', id='A!'),\n                                      pytest.param('b', id='B!')])\n\n# Use literal value (not lazily evaluated)\nfixture_name = static_fixture(42)\nfixture_name = static_fixture('just six sevens', autouse=True, scope='module')\n\n# Raise an exception if fixture is requested\nfixture_name = error_fixture(lambda: ValueError('my life has no intrinsic value'))\n\n# Or maybe don't raise the exception\nfixture_name = error_fixture(lambda other_fixture: TypeError('nope') if other_fixture else None)\n\n# Create an abstract fixture (to be overridden by the user)\nfixture_name = not_implemented_fixture()\nfixture_name = not_implemented_fixture(autouse=True, scope='session')\n\n# Disable usage of a fixture (fail early to save future head scratching)\nfixture_name = disabled_fixture()\n```\n\n\n# What else is possible?\n\nOf course, you can use lambda fixtures inside test classes:\n```python\n# test_staying_classy.py\n\nfrom pytest_lambda import lambda_fixture\n\nclass TestClassiness:\n    classiness = lambda_fixture(lambda: 9000 + 1)\n\n    def test_how_classy_we_is(self, classiness):\n        assert classiness == 9001\n```\n\n\n### Aliasing other fixtures\n\nYou can also pass the name of another fixture, instead of a lambda:\n```python\n# test_the_bourne_identity.py\n\nfrom pytest_lambda import lambda_fixture, static_fixture\n\nagent = static_fixture('Bourne')\nwho_i_am = lambda_fixture('agent')\n\ndef test_my_identity(who_i_am):\n    assert who_i_am == 'Bourne'\n```\n\n\nEven multiple fixture names can be used:\n```python\n# test_the_bourne_identity.py\n\nfrom pytest_lambda import lambda_fixture, static_fixture\n\nagent_first = static_fixture('Jason')\nagent_last = static_fixture('Bourne')\nwho_i_am = lambda_fixture('agent_first', 'agent_last')\n\ndef test_my_identity(who_i_am):\n    assert who_i_am == ('Jason', 'Bourne')\n```\n\n\n#### Annotating aliased fixtures\n\nYou can force the loading of fixtures without trying to remember the name of `pytest.mark.usefixtures`\n```python\n# test_garage.py\n\nfrom pytest_lambda import lambda_fixture, static_fixture\n\ncar = static_fixture({\n    'type': 'Sweet-ass Cadillac',\n    'is_started': False,\n})\nturn_the_key = lambda_fixture(lambda car: car.update(is_started=True))\n\npreconditions = lambda_fixture('turn_the_key', autouse=True)\n\ndef test_my_caddy(car):\n    assert car['is_started']\n```\n\n\n### Declaring abstract things\n\n`not_implemented_fixture` is perfect for labeling abstract parameter fixtures of test mixins\n```python\n# test_mixinalot.py\n\nimport pytest\nfrom pytest_lambda import static_fixture, not_implemented_fixture\n\nclass Dials1900MixinALot:\n    butt_shape = not_implemented_fixture()\n    desires = not_implemented_fixture()\n\n    def it_kicks_them_nasty_thoughts(self, butt_shape, desires):\n        assert butt_shape == 'round' and 'triple X throw down' in desires\n\n\n@pytest.mark.xfail\nclass DescribeMissThing(Dials1900MixinALot):\n    butt_shape = static_fixture('flat')\n    desires = static_fixture(['playin workout tapes by Fonda'])\n\n\nclass DescribeSistaICantResista(Dials1900MixinALot):\n    butt_shape = static_fixture('round')\n    desires = static_fixture(['gettin in yo Benz', 'triple X throw down'])\n```\n\n\nUse `disabled_fixture` to mark a fixture as disabled. Go figure.\n```python\n# test_ada.py\n\nimport pytest\nfrom pytest_lambda import disabled_fixture\n\nwheelchair = disabled_fixture()\n\n@pytest.mark.xfail(strict=True)\ndef test_stairs(wheelchair):\n    assert wheelchair + 'floats'\n```\n\n\n### Raising exceptions\n\nYou can also raise an arbitrary exception when a fixture is requested, using `error_fixture`\n```python\n# test_bikeshed.py\n\nimport pytest\nfrom pytest_lambda import error_fixture, not_implemented_fixture, static_fixture\n\nbicycle = static_fixture('a sledgehammer')\n\ndef it_does_sweet_jumps(bicycle):\n    assert bicycle + 'jump' >= '3 feet'\n\n\nclass ContextOcean:\n    depth = not_implemented_fixture()\n    bicycle = error_fixture(lambda bicycle, depth: (\n        RuntimeError(f'Now is not the time to use that! ({bicycle})') if depth > '1 league' else None))\n\n\n    class ContextDeep:\n        depth = static_fixture('20,000 leagues')\n\n        @pytest.mark.xfail(strict=True, raises=RuntimeError)\n        def it_doesnt_flip_and_shit(self, bicycle):\n            assert bicycle + 'floats'\n\n\n    class ContextBeach:\n        depth = static_fixture('1 inch')\n\n        def it_gets_you_all_wet_but_otherwise_rides_like_a_champ(self, bicycle):\n            assert 'im wet'\n```\n\n\n### Async fixtures\n\nBy passing `async_=True` to `lambda_fixture`, the fixture will be defined as an async function, and if the returned value is awaitable, it will be automatically awaited before exposing it to pytest. This allows the usage of async things while only being slightly salty that Python, TO THIS DAY, still does not support `await` expressions within lambdas! Yes, only slightly salty!\n\nNOTE: an asyncio pytest plugin is required to use async fixtures, such as [pytest-asyncio](https://github.com/pytest-dev/pytest-asyncio)\n\n```python\n# test_a_sink.py\n\nimport asyncio\nimport pytest\nfrom pytest_lambda import lambda_fixture\n\nasync def hows_the_sink():\n    await asyncio.sleep(1)\n    return 'leaky'\n\na_sink = lambda_fixture(lambda: hows_the_sink(), async_=True)\n\nclass DescribeASink:\n    @pytest.mark.asyncio\n    async def it_is_leaky(self, a_sink):\n        assert a_sink is 'leaky'\n```\n\n\n# Development\n\nHow can I build and test the thing locally?\n\n1. Create a virtualenv, however you prefer. Or don't, if you prefer.\n2. `pip install poetry`\n3. `poetry install` to install setuptools entrypoint, so pytest automatically loads the plugin (otherwise, you'll have to run `py.test -p pytest_lambda.plugin`)\n4. Run `py.test`. The tests will be collected from the README.md (thanks to [pytest-markdown](https://github.com/Jc2k/pytest-markdown)).\n",
    'author': 'Zach "theY4Kman" Kanzler',
    'author_email': 'they4kman@gmail.com',
    'maintainer': None,
    'maintainer_email': None,
    'url': 'https://github.com/theY4Kman/pytest-lambda',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'entry_points': entry_points,
    'python_requires': '>=3.7.0,<4.0.0',
}


setup(**setup_kwargs)
