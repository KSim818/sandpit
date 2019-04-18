# -*- coding: utf-8 -*-
"""
Created on Thu Apr 18 16:14:01 2019

@author: KatieSi
"""

# https://jakevdp.github.io/PythonDataScienceHandbook/03.09-pivot-tables.html

import numpy as np
import pandas as pd
import seaborn as sns
titanic = sns.load_dataset('titanic')
titanic.head()
titanic.groupby(['sex', 'class'])['survived'].aggregate('mean').unstack()

titanic.groupby(['sex', 'class'])['survived'].aggregate('count').unstack()