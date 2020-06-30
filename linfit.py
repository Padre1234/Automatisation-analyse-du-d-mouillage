import os
import numpy as np
import matplotlib.pyplot as plt
from scipy import stats
import log_save
from datetime import datetime

c_time = datetime.now() 
str_time = c_time.strftime("%d%m%Y%H%M%S")
str_time2 = c_time.strftime("%d/%m/%Y %H:%M:%S")



print("\n****************** Python Plot - Linear Fit ******************\n########### RUN " + str_time2 + " GMT\n\n")




f = open("sauvegarde_trous.txt", "r")
abx = []
ory = []
i = 0
for x in f:
    c = f.readline()
    e = c.replace('\n','')
    g = e.replace(',','.')
    d = g.split(" ")
    
    if len(c) > 2:
        abx.append(float(d[0]))
        ory.append(float(d[1]))
        
f.close()
        
        
gradient, intercept, r_value, p_value, std_err = stats.linregress(abx,ory)
mn=min(abx)
mx=max(abx)
x1=np.linspace(mn,mx,500)
y1=gradient*x1+intercept

print('************************************************************************\n\n\n########### CALCULATED PARAMETERS ###########\n\tFit Function: f(t) = a * t + b\n\n\ta = ' + str(gradient) + '\n\tb = ' + str(intercept) + '\n\n\tR_squared = ' + str(r_value**2) + '\n')
    
plt.plot(abx, ory, '.', color='#09CF24', label = 'Points expérimentaux')
plt.plot(x1,y1,'-r', label = 'Equation du fit : $v =' + str(gradient) + 't + ' + str(intercept) + '$ \n R² = ' + str(r_value**2), color = '#AAAFFF')
plt.xlabel('$t(s)$')
plt.ylabel('$f(t) =$ Radius $(\mu m)$')
plt.legend()
plt.title('Agrandissement du rayon en fonction du temps', fontsize = 18)
plt.show()

print("\n************************************************************************\n\n")

fig_prompt = input("Save log file ? Y/N \n")


while True:    
    if fig_prompt == 'Y' :
        print("File saved in feiojfpo")
        break
    elif fig_prompt == 'N' :
        print("No log file has been saved for this run")
        break
    else:
        print("Input not understood ; Please answer Y or N")
        fig_prompt = input("Save log file ? Y/N \n")

