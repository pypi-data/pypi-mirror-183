# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['com2fun', 'com2fun.simulated_function']

package_data = \
{'': ['*']}

install_requires = \
['openai>=0.25.0,<0.26.0']

setup_kwargs = {
    'name': 'com2fun',
    'version': '0.1.2',
    'description': '',
    'long_description': '# com2fun - Transform document into function.\n\nThis liabrary leverages [OpenAI API](https://github.com/openai/openai-python) to predict the output of a function based on its documentation.\n\n## Install\n\n```\npip install --upgrade com2fun\n```\n\n## Usage\n\n```\n@com2fun.com2fun\ndef top(category: str, n) -> [str]:\n    """Return a list of top-n items in a category."""\n\nIn [1]: top("fish", 5)\nOut[1]: [\'salmon\', \'tuna\', \'cod\', \'halibut\', \'mackerel\']\nIn [2]: top("Pen Brand", 3)\nOut[2]: [\'Pilot\', \'Uni-ball\', \'Zebra\']\n```\n\n## Add Example\n\n```\n@com2fun.com2fun\ndef bill2beancount(bill):\n    """Transform a bill for a transaction in credit card website into a transaction in beancoun."""\n\nIn [3]: bill2beancount.add_example(r"""\nBACKBLAZE 8778877815 CA\nDec 21, 2022$0.96\nMerchant Contact Information\n500 BEN FRANKLIN CT, CA 94401\nCall us at(877) 887 - 7815\nAdditional Information\nTransaction Details\nMerchant Category\tCOMPUTER PROGRAMMING, DATA PROCESSING\nTransaction Date\tWED, 12/21/2022\nPurchase Method\tCARD INFORMATION STORED ON FILE\nPost Date\tWED, 12/21/2022\nRecurring Billing Indicator\tY\nCash Back Earned\t$ 0.01\n""")(r"""2022-11-21 * "backblaze"\n  Expenses:Backup:Backblaze                                        0.96-0.01 USD\n  Income:CreditCard:Discover:Cashback                              0.01 USD\n  Liabilities:CreditCard:Discover                                  -0.96 USD\n""")\n\nIn [4]: bill2beancount( r"""\nPP*APPLE.COM/BILL 402-935-7733 CA\nDec 10, 2022$2.99\nMerchant Contact Information\n2211 NORTH FIRST STREE, CA 95131\nCall us at402-935-7733\nAdditional Information\nTransaction Details\nMerchant Category       RECORD STORES\nTransaction Date        SAT, 12/10/2022\nPurchase Method MANUALLY KEYED\nPost Date       SAT, 12/10/2022\nPhone Number    4029357733\nPoint Of Sale Zip Code  95131\nCash Back Earned        $ 0.03\n"""\n    )\n)\n\n2022-11-10 * "pp*apple.com/bill"\n  Expenses:Shopping:Apple                                         2.99-0.03 USD\n  Income:CreditCard:Discover:Cashback                              0.03 USD\n  Liabilities:CreditCard:Discover                                  -2.99 USD\n```\n',
    'author': 'xiaoniu',
    'author_email': 'hzmxn@mail.ustc.edu.cn',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'None',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.10,<4.0',
}


setup(**setup_kwargs)
