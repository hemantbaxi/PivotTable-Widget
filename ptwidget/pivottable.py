from ipyiframe import Iframe
from IPython.display import HTML
import IPython.core.display as display
import ipywidgets as widgets
from pivottablejs import pivot_ui

""" Pandas Dataframe Pivot Table Widget
    df: Pandas Dataframe
    width: Width of the frame (default = 1800)
    height: Height of the frame (default=1000)
    scrolling: Enable scroll in the frame (default = 'yes')
    border: Border of the frame (default = '1px gray solid')
    Returns custom Iframe object from ipyiframe renderable in voila
"""
def ptwidget(df, width=1800, height=1000, scrolling ='yes', border='1px gray solid'):
    filename = "dfpivotjs.html"
    pivot_ui(df, outfile_path=filename)
    htmlfile = open(filename)
    content = htmlfile.read()
    frame = Iframe(
            # url - default to None
            # content - default to None
            # exactly one of src and srcdoc can be passed
            srcdoc=content,
            # width in CSS px - from the content page
            width=width,
            # height in CSS px - from the content page
            height=height,
            # CSS for iframe border attr
            border='1px gray solid',
            # CSS for iframe margin attr
            margin='',
            # CSS for iframe padding attr
            padding='1px',
            # iframe scrolling attr
            scrolling='yes',
            # transform-origin param - default to 'top left'
            transform_origin='top center'
        )
    return frame

"""
Example :

import pandas as pd
import numpy as np
from ptwidget import pivottable as wd
df = pd.DataFrame(np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]]),columns=['a', 'b', 'c'])
wd.ptwidget(df)

"""

