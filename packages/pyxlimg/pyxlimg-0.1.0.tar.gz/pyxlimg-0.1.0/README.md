# What is pyxlimg

Pyxlimg is for extracting images from xlsx. It has a high affinity with other libraries. This is because you can treat the image as an instance of Pillow.Image. I hope it will be incorporated into openpyxl and pylightxl in the future.

# Concept

Images are difficult to handle with xlwings, openpyxl, and pylightxl. Especially linter and type annotation are difficult. Complement these. And the goal is to make it easier to do OCR etc. using xlsx in Python.

# Install

Recommended to install using pip.

```sh
pip install pyxlimg
```

# Usage

```py
from PIL import Image
from pyxlimg import xlimg

TestBookName = "./your-test-data/TestBook.xlsx"


if __name__ == "__main__":
    TargetBook: xlimg.ImageBook = xlimg.ImageBook()
    TargetBook.open(TestBookName)
    print("This book named '" + TargetBook.name + "'.")
    print("This book has " + len(TargetBook.Sheets) + " sheets.")
    print("First sheet name is '" + TargetBook.Sheets[0].displayName + "'.")
    print("First sheet has " + len(TargetBook.Sheets[0].Pictures + " pictures.")
    TargetBook.Sheets[1].Pictures[0].Image().show() # Show you the Image
```

In this way, you can easily assign images to variable.

```py
    DisplayImage: Image = TargetBook.Sheets[1].Pictures[0].Image()
    DisplayImage.show() # Show you the Image too.
```

# FAQ

## What image format does this support?
If it is supported by Pillow, it can be supported. If the original image is in a commonly used format such as png, jpg, bmp when pasted or inserted into xlsx.

## What kind of library is this supposed to be used with?
For example, `Tesseract OCR`, `pylightxl`, `openpyxl`, `matplotlib`. It is also ideal for matching with other `pillow` related libraries.

# How to Contribute

Please do a git clone and pull request. The version control tool used in this repository is poetry.