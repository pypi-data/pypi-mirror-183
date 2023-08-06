# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['myriade', 'myriade.multiclass']

package_data = \
{'': ['*']}

install_requires = \
['scikit-learn>=1.2.0,<2.0.0', 'scipy>=1.9.3,<2.0.0']

setup_kwargs = {
    'name': 'myriade',
    'version': '0.1.0',
    'description': 'Extreme multiclass and multi-label classification',
    'long_description': '# myriad\n\nMulticlass classification with tens of thousands of classes\n\n## Usage\n\n## Datasets\n\n| Name | Function    | Size     | Samples | Features | Labels     | Multi-label    | Labels/sample |\n|:----:|:-----------:|:---------|:-------:|:--------:|:----------:|:--------------:|:-------------:|\n| DMOZ | `load_dmoz` | 614,8 MB | 394,756 | 833,484  | 36,372     | ✓              | 1.02          |\n| Wikipedia (small) | `load_wiki_small` | 135,5 MB | 456,886 | 2,085,165  | 36,504     | ✓              | 1.84          |\n| Wikipedia (large) | `load_wiki_large` | 1,01 GB | 2,365,436 | 2,085,167  | 325,056     | ✓              | 3.26          |\n\nEach `load_*` function returns two arrays which contain the features and the target classes, respectively. In the multi-label case, the target array is 2D. The arrays are sparse when applicable.\n\n```py\n>>> from myriad import datasets\n\n>>> X, y = datasets.load_dmoz()\n>>> X\n\n>>> y\n\n```\n\nThe first time you call a `load_*` function, the data will be downloaded and saved into a `.svm` file that adheres to the [LIBSVM format convention](https://www.csie.ntu.edu.tw/~cjlin/libsvm/faq.html#/Q03:_Data_preparation). The loaders will restart from scratch if you interrupt them during their work.\n\nAll of the datasets are loaded in memory with the [`svmloader`](https://github.com/yoch/svmloader/) library. The latter is much faster than the [`load_svmlight_file`](https://scikit-learn.org/stable/modules/generated/sklearn.datasets.load_svmlight_file.html) function from scikit-learn. However, when working repeatedly on the same dataset, it is recommended to wrap the dataset loader with [`joblib.Memory.cache`](https://joblib.readthedocs.io/en/latest/memory.html) to store a memmapped backup of the results of the first call. This enables near instantaneous loading for subsequent calls.\n\nYou can see where the datasets are stored as so:\n\n```py\n>>> datasets.get_data_home()\n\n```\n\n## Benchmarks\n',
    'author': 'Max Halford',
    'author_email': 'maxhalford25@gmail.com',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'None',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.10,<4.0',
}


setup(**setup_kwargs)
