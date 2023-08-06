# -*- coding: utf-8 -*-
"""
Created on Wed Dec 28 16:22:06 2022

@author: ChiChun.Chen
"""


from .version import version as __version__

import numpy as np
import pandas as pd


def numpy_version():
    return np.__version__


def pandas_version():
    return pd.__version__