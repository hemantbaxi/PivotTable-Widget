# PivotTable-Widget

This package provides ipywidget wrapper around Pivot Table package from https://pypi.org/project/pivottablejs/  
The wrapper is needed to render Pivot Table in webpage via servers like voila.  
The wrapper is written using Iframe widget provided by package - https://pypi.org/project/ipyiframe/.  

Build:

python3 -m build

Install:

pip3 install --user ./dist/ptwidget-0.1.0-py3-none-any.whl


Example:
import pandas as pd  
import numpy as np  
from ptwidget import pivottable as wd  
df = pd.DataFrame(np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]]),columns=['a', 'b', 'c'])  
wd.ptwidget(df)  
