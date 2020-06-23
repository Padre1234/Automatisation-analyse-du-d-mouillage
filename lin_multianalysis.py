import os
import numpy as np
import matplotlib.pyplot as plt
from scipy import stats
import data_plot
from datetime import datetime


##### TIME SET

str_time = data_plot.run_time()


##### FILE CHECK

n_file = data_plot.check_files()

#abx_t = []
#ory_t = []


##### DATA&FIT PLOT / LOG SAVE

data_plot.plot(n_file)
