import os
import numpy as np
import matplotlib.pyplot as plt
from scipy import stats
from datetime import datetime
import log_save
import xlsxwriter


def run_time():


    c_time = datetime.now() 
    str_time = c_time.strftime("%d%m%Y%H%M%S")
    str_time2 = c_time.strftime("%d/%m/%Y %H:%M:%S")
    print("\n################## Python Plot - Linear Fit ##################\n*********** RUN " + str_time2 + " GMT\n\n")
    return (str_time)

def check_files():
    i=1

    while True:
        if os.path.isfile("sauvegarde_trous" + str(i) + ".txt"):
            print("sauvegarde_trous" + str(i) + ".txt exists")
            i = i+1
        else:
            print("sauvegarde_trous" + str(i) + ".txt doesn't exist")
            n_file = i
            break
    print("\nThere are " + str(n_file-1) + " files analyzable\n")
    file_prompt = input("How many file do you want to analyze? 1 - " + str(n_file-1) + "\n")

    list_files = list(range(1, n_file))
    
    while True:
        try:
           value = int(file_prompt)
           if int(file_prompt) in list_files :
               n_analyzed = file_prompt
               break
           else:
               print("Input not understood ; Please answer an integer between 1 and " + str(n_file-1) + "\n")
               file_prompt = input("How many file do you want to analyze? 1 - " + str(n_file-1) + "\n")

        except ValueError:
           print("Input not understood ; Please answer an INTEGER between 1 and " + str(n_file-1) + "\n")
           file_prompt = input("How many file do you want to analyze? 1 - " + str(n_file-1) + "\n")

    return (n_analyzed)

def plot(n_file):



    log_i = input("\nSave log file? Y/N")

    while True:
        if log_i == 'Y':
            log_save = 0
        elif log_i != 'N':
            print("Input not understood ; Please answer Y or N")
            log_i = input("Save Excel file? Y/N")
        else:
            log_save = 1
            
    excel_i = input("\nSave Excel file? Y/N")

    while True:
        if excel_i == 'Y':
            excel_save = 0
        elif excel_i != 'N':
            print("Input not understood ; Please answer Y or N")
            excel_i = input("Save Excel file? Y/N")
        else:
            excel_save = 1
        
    n_sheet = []
    n_source = []

    for i in range(1, int(n_file)+1):
     #n_line = 0.
      #  f1 = open("sauvegarde_trous" + str(i) + ".txt"
      #for line in f:
       # count += 1.
        #print("Total number of lines is:", count)
        f = open("sauvegarde_trous" + str(i) + ".txt", "r")
        abx = []
        ory = []
        j = 0
        b = []
        for x in f:
            if j == 0:
                c = x
                e = c.replace('\n','')
                g = e.replace(',','.')
                d = g.split(" ")
                n_sheet = str(d[0])
                n_source = str(d[1])
                j = j+1
            else:
                c = x
                e = c.replace('\n','')
                g = e.replace(',','.')
                d = g.split(" ")
                   
                if len(c) > 2:
                    abx.append(float(d[0]))
                    ory.append(float(d[1]))
                j = j+1
    
        f.close()
        gradient, intercept, r_value, p_value, std_err = stats.linregress(abx,ory)
        mn=min(abx)
        mx=max(abx)
        x1=np.linspace(mn,mx,500)
        y1=gradient*x1+intercept
    
        print('\n########################################################################\n\n\n*********** CALCULATED PARAMETERS ***********\n\tFILE // SHEET: ' + n_source + ' // ' + n_sheet + '\n\tFit Function: f(t) = a * t + b\n\n\ta = ' + str(gradient) + '\n\tb = ' + str(intercept) + '\n\n\tR_squared = ' + str(r_value**2) + '\n')
        
        plt.plot(abx, ory, '.', label = n_sheet + ' // Points expérimentaux')
        plt.plot(x1,y1,'-r', label = n_sheet + ' // Equation du fit : $v =' + str(gradient) + 't + ' + str(intercept) + '$ \n R² = ' + str(r_value**2))

        #####################


        
        #abx_t.append(abx)
        #ory_t.append(ory)
        
    plt.xlabel('$t(s)$')
    plt.ylabel('$f(t) =$ Radius $(\mu m)$')
    plt.legend()
    plt.title('Agrandissement du rayon en fonction du temps', fontsize = 18)
    plt.show()    
    print("\n########################################################################\n\n")
    
    
            
