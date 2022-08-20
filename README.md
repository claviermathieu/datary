# datary - Data for actuary


Datary is a python package resulting from the experience of an actuary gathering different useful functions to gain in work efficiency when it comes to processing data.

<br>

## Package installation

![Tests](https://github.com/claviermathieu/datary/actions/workflows/tests.yml/badge.svg)

To install the package, you juste need to run in your terminal the command:

 
 ```{dropdown} 
pip install git+https://github.com/claviermathieu/datary.git
```


<br>

After that you just need to import the library in your python code as


```{dropdown} 
import datary.interface as it
from datary.excel import ExcelReader
```


<br>

## What does datary do ?

Datary is composed of several modules responding to different needs.

* interface : shortcut to create a terminal interface for your program
* excel : read excel unstructured file calling directly tables, ranges and cells names
* utils
* template : not a program but a template file for good practices presentation (anyway, always use pep8 and check with flake8)

### Interface

#### To do what ?

When it comes to manage data with Python,  notebook are often a great idea. It allows to visualize in live how looks our data and treat them consequently.

So for exploration, notebooks are great, but when it comes to production notebooks are slighly less effective. Typically, when your script process some inputs that are periodically refresh. You don't want to enter in your notebook for change the input direction. Moreover, notebook is sligtly less portable and people not knowing python will have less

Now, some great text editor as [VS code](https://code.visualstudio.com/) allow to run interactiv jupyter window using script from a .py file. This is the perfect compromise!

At the end of the day, we only want a **.py** or **.bat** executable that open an interface as simple as possible showing only useful stuff and asking as few things as possible to be very simple even for someone knowing anything about Python.

<br>

### Excel


##