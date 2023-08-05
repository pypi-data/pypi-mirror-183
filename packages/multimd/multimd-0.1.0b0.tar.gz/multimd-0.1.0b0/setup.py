# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['multimd']

package_data = \
{'': ['*']}

install_requires = \
['natsort>=7.1.1,<8.0.0']

setup_kwargs = {
    'name': 'multimd',
    'version': '0.1.0b0',
    'description': 'This project makes it possible to write separated pieces of `MD` files that will be merged to produce one single final `MD` file.',
    'long_description': "The `Python` module `multimd`\n=============================\n\n\n> **I beg your pardon for my english...**\n>\n> English is not my native language, so be nice if you notice misunderstandings, misspellings, or grammatical errors in my documents and codes.\n\n\nAbout `multimd`\n---------------\n\nWorking with `MD` documents of moderate size in a single file can becomes quickly painful. This project makes it possible to write separated pieces of `MD` files that will be merged to produce one single  `MD` file.\n\n\n`README.md` part by part\n------------------------\n\nThanks to `multimd`, you can write a `MD` document typing small section like parts that are easy to maintain. Let's consider the `README.md` of the `src2prod` project that was written using the following tree structure on August 22, 2021. Just note that there are only `MD` files directly inside the same folder (the purpose of `multimd` is to ease the writting of realtively small documents and not books).\n\n~~~\n+ src2prod\n    + readme\n        * about.yaml\n        * build.md\n        * cli.md\n        * example-used.md\n        * only-files.md\n        * prologue.md\n        * readme-splitted.md\n\n    * README.md\n~~~\n\nThe special file `about.yaml` allows to indicate the order to use to merge the different `MD` files. Its content was the following one.\n\n~~~yaml\ntoc:\n  - prologue\n  - example-used\n  - build\n  - only-files\n  - readme-splitted\n  - cli\n~~~\n\nHere how `README.md` was built. We will suppose the use of the `cd` command to go inside the parent folder of `scr2prod` before launching the following script where we use instances of `Path` from `pathlib`.\n\n~~~python\nfrom multimd import Builder\n\nmybuilder = Builder(\n    output  = Path('README.md'),\n    content = Path('readme'),\n)\n\nmybuilder.build()\n~~~\n\n\nWithout the special `about.yaml` file\n-------------------------------------\n\nIf you don't use the `about.yaml` file, the class `Builder` looks for all the `MD` files and then merges. The ordred used is the one given by `natsorted` from the package `natsort`.\n",
    'author': 'Christophe BAL',
    'author_email': 'None',
    'maintainer': 'Christophe BAL',
    'maintainer_email': 'None',
    'url': 'https://github.com/bc-tools/for-dev/tree/main/multimd',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.8,<4.0',
}


setup(**setup_kwargs)
