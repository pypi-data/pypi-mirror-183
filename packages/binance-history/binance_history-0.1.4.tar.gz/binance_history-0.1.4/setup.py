# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['binance_history']

package_data = \
{'': ['*']}

install_requires = \
['httpx>=0.23.1,<0.24.0',
 'loguru>=0.6.0,<0.7.0',
 'pandas>=1.5.2,<2.0.0',
 'pendulum>=2.1.2,<3.0.0']

entry_points = \
{'console_scripts': ['bh = binance_history.cli:main']}

setup_kwargs = {
    'name': 'binance-history',
    'version': '0.1.4',
    'description': 'Fetch binance historical klines or trades easily.',
    'long_description': '===============\nBinance History\n===============\n\n.. image:: https://img.shields.io/pypi/v/binance-history\n    :target: https://pypi.org/project/binance-history/\n    :alt: pypi\n\n.. image:: https://img.shields.io/pypi/pyversions/binance-history\n   :alt: PyPI - Python Version\n\n.. image:: https://img.shields.io/github/license/xzmeng/binance-history\n    :target: https://github.com/xzmeng/binance-history/blob/master/LICENSE\n    :alt: license - MIT\n\n.. image:: https://img.shields.io/codecov/c/github/xzmeng/binance-history\n    :target: https://codecov.io/github/xzmeng/binance-history\n    :alt: coverage\n\n.. image:: https://img.shields.io/github/actions/workflow/status/xzmeng/binance-history/tests.yml?label=tests\n    :target: https://github.com/xzmeng/binance-history/actions\n    :alt: tests\n\nFetch binance public data easily.\n\nSupports Python **3.10+**.\n\nInstallation\n============\n\n.. code-block:: bash\n\n    $ pip install binance-history\n\n**binance-history** comes with a command line interface,\nyou need to install some extra dependencies to use it:\n\n.. code-block:: bash\n\n    $ pip install \'binance-history[cli]\'\n\nUsage\n=====\n\n.. code-block:: python\n\n    >>> import binance_history as bh\n    >>> klines = bh.fetch_klines(\n    ...     asset_type="spot",\n    ...     symbol="BTCUSDT",\n    ...     timeframe="1m",\n    ...     start="2022-12-14",\n    ...     end="2022-12-24",\n    ...     tz="Asia/Shanghai"\n    ... )\n                                   open      high       low     close     volume  quote_volume  trades                   close_datetime\n    open_datetime\n    2022-12-14 00:00:00+08:00  17753.54  17768.41  17752.78  17766.99  240.82918  4.277685e+06    5241 2022-12-14 00:00:59.999000+08:00\n    2022-12-14 00:01:00+08:00  17766.99  17786.40  17764.37  17781.81  311.47670  5.536668e+06    6278 2022-12-14 00:01:59.999000+08:00\n    2022-12-14 00:02:00+08:00  17781.81  17790.54  17771.44  17785.37  372.12992  6.616562e+06    6911 2022-12-14 00:02:59.999000+08:00\n    2022-12-14 00:03:00+08:00  17786.23  17800.18  17774.63  17777.35  401.52223  7.142210e+06    6926 2022-12-14 00:03:59.999000+08:00\n    2022-12-14 00:04:00+08:00  17777.35  17785.98  17769.15  17781.93  218.03837  3.876373e+06    5519 2022-12-14 00:04:59.999000+08:00\n    ...                             ...       ...       ...       ...        ...           ...     ...                              ...\n    2022-12-23 23:56:00+08:00  16850.22  16850.22  16839.55  16842.59  146.38906  2.465894e+06    4229 2022-12-23 23:56:59.999000+08:00\n    2022-12-23 23:57:00+08:00  16842.59  16846.22  16839.00  16840.99   86.95440  1.464495e+06    3152 2022-12-23 23:57:59.999000+08:00\n    2022-12-23 23:58:00+08:00  16840.99  16843.61  16827.28  16830.27  208.41471  3.508642e+06    4918 2022-12-23 23:58:59.999000+08:00\n    2022-12-23 23:59:00+08:00  16830.27  16836.66  16824.41  16832.16  154.10833  2.593717e+06    4502 2022-12-23 23:59:59.999000+08:00\n    2022-12-24 00:00:00+08:00  16832.15  16833.62  16828.42  16830.52  119.28572  2.007721e+06    3725 2022-12-24 00:00:59.999000+08:00\n\n    [14401 rows x 8 columns]\n\n\nCommand Line\n============\n\n.. code-block:: bash\n\n    $ bh --help\n    Usage: bh [OPTIONS]\n\n    Options:\n      --data-type [klines|aggTrades]  choose klines or aggTrades to download,\n                                      default to \'klines\'\n      --asset-type [spot|futures-usd|futures-coin]\n                                      choose spot or futures data, default to\n                                      \'spot\'\n      --symbol TEXT                   The binance market pair name, e.g. BTCUSDT\n                                      [required]\n      --timeframe [1s|1m|3m|5m|15m|30m|1h|2h|4h|6h|8h|12h|1d|3d|1w|1M]\n                                      The timeframe of klines, default to \'15m\',\n                                      can be omitted if --data-type is not\n                                      \'klines\'\n      --start TEXT                    The start datetime, e.g. \'2022-1-2 5:20\'\n                                      [required]\n      --end TEXT                      The end datetime, e.g. \'2022-1-25\n                                      [required]\n      --tz TEXT                       The timezone, default to \'Asia/Shanghai\'\n      --output-path TEXT              The path you want to save the downloaded\n                                      data, support format: [csv, json, xlsx],\n                                      e.g. a.xlsx  [required]\n      --help                          Show this message and exit.\n\n    $ bh --start 2022-1-5 --end 2022-1-7 --symbol ETCBTC --output-path a.xlsx\n',
    'author': 'Meng Xiangzhuo',
    'author_email': 'aumo@foxmail.com',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'https://github.com/xzmeng/binance-history',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'entry_points': entry_points,
    'python_requires': '>=3.10,<4.0',
}


setup(**setup_kwargs)
