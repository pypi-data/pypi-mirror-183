# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['pyxlimg']

package_data = \
{'': ['*']}

install_requires = \
['Pillow>=8.1.2,<9.0.0']

setup_kwargs = {
    'name': 'pyxlimg',
    'version': '0.1.0',
    'description': 'Image Extractor for XLSX files',
    'long_description': '# What is pyxlimg\n\nPyxlimg is for extracting images from xlsx. It has a high affinity with other libraries. This is because you can treat the image as an instance of Pillow.Image. I hope it will be incorporated into openpyxl and pylightxl in the future.\n\n# Concept\n\nImages are difficult to handle with xlwings, openpyxl, and pylightxl. Especially linter and type annotation are difficult. Complement these. And the goal is to make it easier to do OCR etc. using xlsx in Python.\n\n# Install\n\nRecommended to install using pip.\n\n```sh\npip install pyxlimg\n```\n\n# Usage\n\n```py\nfrom PIL import Image\nfrom pyxlimg import xlimg\n\nTestBookName = "./your-test-data/TestBook.xlsx"\n\n\nif __name__ == "__main__":\n    TargetBook: xlimg.ImageBook = xlimg.ImageBook()\n    TargetBook.open(TestBookName)\n    print("This book named \'" + TargetBook.name + "\'.")\n    print("This book has " + len(TargetBook.Sheets) + " sheets.")\n    print("First sheet name is \'" + TargetBook.Sheets[0].displayName + "\'.")\n    print("First sheet has " + len(TargetBook.Sheets[0].Pictures + " pictures.")\n    TargetBook.Sheets[1].Pictures[0].Image().show() # Show you the Image\n```\n\nIn this way, you can easily assign images to variable.\n\n```py\n    DisplayImage: Image = TargetBook.Sheets[1].Pictures[0].Image()\n    DisplayImage.show() # Show you the Image too.\n```\n\n# FAQ\n\n## What image format does this support?\nIf it is supported by Pillow, it can be supported. If the original image is in a commonly used format such as png, jpg, bmp when pasted or inserted into xlsx.\n\n## What kind of library is this supposed to be used with?\nFor example, `Tesseract OCR`, `pylightxl`, `openpyxl`, `matplotlib`. It is also ideal for matching with other `pillow` related libraries.\n\n# How to Contribute\n\nPlease do a git clone and pull request. The version control tool used in this repository is poetry.',
    'author': 'ShortArrow',
    'author_email': 'bamboogeneral@live.jp',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'None',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.8,<4.0',
}


setup(**setup_kwargs)
