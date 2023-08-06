# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['binance_history']

package_data = \
{'': ['*']}

install_requires = \
['httpx>=0.23.1,<0.24.0', 'loguru>=0.6.0,<0.7.0', 'pandas>=1.5.2,<2.0.0']

setup_kwargs = {
    'name': 'binance-history',
    'version': '0.1.1',
    'description': 'Fetch binance historical klines or trades easily.',
    'long_description': '===============\nBinance History\n===============\n\n.. image:: https://img.shields.io/pypi/v/binance-history\n    :target: https://pypi.org/project/binance-history/\n\n.. image:: https://img.shields.io/codecov/c/github/xzmeng/binance-history\n    :target: https://codecov.io/github/xzmeng/binance-history\n\n.. image:: https://img.shields.io/github/actions/workflow/status/xzmeng/binance-history/tests.yml?label=tests\n    :target: https://github.com/xzmeng/binance-history/actions\n\nFetch binance public data easily.\n\nUsage\n=====\n\n.. code-block:: python\n\n    >>> import binance_history as bh\n    >>> klines = bh.fetch_klines(\n    ...     asset_type="spot",\n    ...     symbol="BTCUSDT",\n    ...     timeframe="1m",\n    ...     start="2022-12-14",\n    ...     end="2022-12-24",\n    ...     tz="Asia/Shanghai"\n    ... )\n                                   open      high       low     close     volume  quote_volume  trades                   close_datetime\n    open_datetime\n    2022-12-14 00:00:00+08:00  17753.54  17768.41  17752.78  17766.99  240.82918  4.277685e+06    5241 2022-12-14 00:00:59.999000+08:00\n    2022-12-14 00:01:00+08:00  17766.99  17786.40  17764.37  17781.81  311.47670  5.536668e+06    6278 2022-12-14 00:01:59.999000+08:00\n    2022-12-14 00:02:00+08:00  17781.81  17790.54  17771.44  17785.37  372.12992  6.616562e+06    6911 2022-12-14 00:02:59.999000+08:00\n    2022-12-14 00:03:00+08:00  17786.23  17800.18  17774.63  17777.35  401.52223  7.142210e+06    6926 2022-12-14 00:03:59.999000+08:00\n    2022-12-14 00:04:00+08:00  17777.35  17785.98  17769.15  17781.93  218.03837  3.876373e+06    5519 2022-12-14 00:04:59.999000+08:00\n    ...                             ...       ...       ...       ...        ...           ...     ...                              ...\n    2022-12-23 23:56:00+08:00  16850.22  16850.22  16839.55  16842.59  146.38906  2.465894e+06    4229 2022-12-23 23:56:59.999000+08:00\n    2022-12-23 23:57:00+08:00  16842.59  16846.22  16839.00  16840.99   86.95440  1.464495e+06    3152 2022-12-23 23:57:59.999000+08:00\n    2022-12-23 23:58:00+08:00  16840.99  16843.61  16827.28  16830.27  208.41471  3.508642e+06    4918 2022-12-23 23:58:59.999000+08:00\n    2022-12-23 23:59:00+08:00  16830.27  16836.66  16824.41  16832.16  154.10833  2.593717e+06    4502 2022-12-23 23:59:59.999000+08:00\n    2022-12-24 00:00:00+08:00  16832.15  16833.62  16828.42  16830.52  119.28572  2.007721e+06    3725 2022-12-24 00:00:59.999000+08:00\n\n    [14401 rows x 8 columns]\n\n',
    'author': 'Meng Xiangzhuo',
    'author_email': 'aumo@foxmail.com',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'https://github.com/xzmeng/binance-history',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.11,<4.0',
}


setup(**setup_kwargs)
