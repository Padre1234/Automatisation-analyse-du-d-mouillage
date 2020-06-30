import os
import math
import numpy as np
import matplotlib.pyplot as plt
from scipy import stats
from datetime import datetime
import xlsxwriter

def run_time():


    c_time = datetime.now() 
    str_time = c_time.strftime("%d%m%Y%H%M%S")
    str_time2 = c_time.strftime("%d/%m/%Y %H:%M:%S")
    print("\n################## Python Plot - Linear Fit ##################\n*********** RUN " + str_time2 + " GMT\n\n")
    return (str_time)

str_time = run_time()

def csv_check():
    n_csv=0

    for f_name in os.listdir('./csv_logs/Trous'):
        if f_name.endswith('.csv'):
            print (f_name + "\tTRUE")
            n_csv = n_csv + 1

    if n_csv > 0:
        print ("\nThere are " + str(n_csv) + " files analyzable")
        file_prompt = input("How many files do you want to analyze? 1 - " + str(n_csv) + "\t")
        
    else:
        print("\nThere is no .csv log file in /csv_logs. Please add .csv logs and run the program")
        exit()

    while True:
            try:
               value = int(file_prompt)
               if int(file_prompt) in list(range(1, n_csv+1)) :
                   n_analyzed = file_prompt
                   break
               else:
                   print("Input not understood ; Please answer an integer between 1 and " + str(n_csv) + "\n")
                   file_prompt = input("How many file do you want to analyze? 1 - " + str(n_csv) + "\t")

            except ValueError:
                print("Input not understood ; Please answer an INTEGER between 1 and " + str(n_csv) + "\n")
                file_prompt = input("How many file do you want to analyze? 1 - " + str(n_csv) + "\t")

    return (n_analyzed)

n_analyzed = csv_check()

def plot(n_file, str_time):

    xl_trous = []

    xl_trous.append("Type de PS")
    xl_trous.append("Type de PMMA")
    xl_trous.append("RPM (tr/min)")
    xl_trous.append("APM (tr/min)")
    xl_trous.append("Temps (s)")
    xl_trous.append("Epaisseur PS")
    xl_trous.append("Epaisseur PMMA")
    xl_trous.append("Température (°C)")
    xl_trous.append("Gap (um)")
    
    run_dir = os.path.dirname(__file__)
    
    log_i = input("\nSave log file? Y/N\t")

    while True:
        if log_i == 'Y':
            log_save = 0
            log_dir = 'Analysis/log_saves'
            log_path = os.path.join(run_dir, log_dir)
            break
        elif log_i != 'N':
            print("Input not understood ; Please answer Y or N")
            log_i = input("Save log file? Y/N")
        else:
            log_save = 1
            break
            
    excel_i = input("\nSave Excel file? Y/N\t")

    while True:
        if excel_i == 'Y':
            excel_save = 0
            excel_dir = 'Analysis/xls_saves'
            excel_path = os.path.join(run_dir, excel_dir)
            w_sheet = []
            break
        elif excel_i != 'N':
            print("Input not understood ; Please answer Y or N")
            excel_i = input("Save Excel file? Y/N")
        else:
            excel_save = 1
            break
 
    files_list = os.listdir('./csv_logs/Trous')



    for i in range(1, int(n_file)+1):
     #n_line = 0.
      #  f1 = open("sauvegarde_trous" + str(i) + ".txt"
      #for line in f:
       # count += 1.
        #print("Total number of lines is:", count)

        
        n_source = str(files_list[i-1].replace(".csv", ""))
        rel_path = "csv_logs/Trous/" + str(files_list[i-1])
        csv_path = os.path.join(run_dir, rel_path)
        f = open(csv_path, "r")
        
        j = 1
        time = []
        radius = []


        for x in f:
            if j == 1:
                first_line = x
                line1 = x.split(",")


                ##### EXCEL FILE #####




                
                if excel_save ==0:
                    if i ==1:
                        if not os.path.exists(excel_dir):
                            os.makedirs(excel_dir)
                            print("Directory " , str(excel_dir) ,  " created ")
                        else:    
                            print("Directory " , str(excel_dir) ,  " already exists") 
                        workbook = xlsxwriter.Workbook(excel_dir + '/xls_' + str_time + '.xlsx')
                        
                    w_sheet.append(workbook.add_worksheet(str(files_list[i-1]).replace('.csv', '')))
                        # openpyxl module : workbook.save(os.path.join(excel_dir, 'xls_' + str_time + '.xlsx'), as_template = False)
                    
                    cell_format = workbook.add_format()

                    cell_format.set_align('center')
                    cell_format.set_align('vcenter')
                    

       
                    for z in range(0, len(line1)):
                        w_sheet[i-1].write(12+j-1, z, str(line1[z]).replace('.', ','), cell_format)
                        w_sheet[i-1].set_column(z, z, 16)

                    w_sheet[i-1].write(12+j-1, len(line1), "Radius (um)", cell_format)
                    w_sheet[i-1].set_column(len(line1), len(line1), 16)

                   






                        
                for k in range(0, len(line1)):
                    if line1[k] == "Area":
                        number_area = k
                        print("AREA =>> " + str(k) + "\n")
                        break
                j = j+1
            else:
                line = x
                el_line = x.split(",")
                time.append(int(el_line[0])-1)
                radius.append(math.sqrt(float(el_line[number_area])/(math.pi)))
                

                if excel_save ==0:
                    for z in range(0, len(line1)):
                        w_sheet[i-1].write(12+j-1, z, str(el_line[z]).replace('.', ','), cell_format)
                    w_sheet[i-1].write(12+j-1, len(line1), str((float(el_line[number_area])/float((math.pi)))**(0.5)), cell_format)
                    # w_sheet[i-1].write(12+j-1, len(line1), (el_line[1]/(math.pi))**(0.5), cell_format)

                    
                j = j+1


        if excel_save ==0:
            bold_format = workbook.add_format({'bold': True})
            w_sheet[i-1].set_column(0,0,25, bold_format)
            w_sheet[i-1].set_column(len(line1),len(line1),18, bold_format)
                    
            #w_sheet[i-1].write(12+j-1, len(line1), str((line1[1]/(math.pi))**(0.5)), cell_format)


            for ii in range(0, 9):
                w_sheet[i-1].write(ii, 0, str(xl_trous[ii]), cell_format)
            if i == int(n_file):
                workbook.close()
        f.close()
        
        gradient, intercept, r_value, p_value, std_err = stats.linregress(time,radius)
        mn=min(time)
        mx=max(time)
        x1=np.linspace(mn,mx,500)
        y1=gradient*x1+intercept
    
        print('\n########################################################################\n\n\n*********** CALCULATED PARAMETERS ***********\n\tFILE: ' + n_source + '\n\tFit Function: f(t) = a * t + b\n\n\ta = ' + str(gradient) + '\n\tb = ' + str(intercept) + '\n\n\tR_squared = ' + str(r_value**2) + '\n')
        
        plt.plot(time, radius, '.', label = n_source + ' // Points expérimentaux')
        plt.plot(x1,y1,'-r', label = n_source + ' // Equation du fit : $v =' + str(gradient) + 't + ' + str(intercept) + '$ \n R² = ' + str(r_value**2))

        #####################

        ##### LOG FILE #####



        if log_save == 0:
            print("\n*********** LOG FILE SAVE ***********\n\n\t")
            
            
            if not os.path.exists(log_dir):
                os.makedirs(log_dir)
                print("Directory " , str(log_dir) ,  " created ")
            else:    
                print("Directory " , str(log_dir) ,  " already exists") 

            logfilename = str(files_list[i-1]).replace('.csv', '.txt')
            f2 = open(log_path + '/log_' + logfilename, 'a')
            f2.write("########################################################################\n\n\t***********\tLOG FILE\t***********\n\n##### RUN DATE: " + str_time + '\n##### ANALYZED FILE: ' + str(files_list[i-1]) + '\n\n\n########################################################################\n\n\n*********** CALCULATED PARAMETERS ***********\n\tFILE: ' + n_source + '\n\tFit Function: f(t) = a * t + b\n\n\ta = ' + str(gradient) + '\n\tb = ' + str(intercept) + '\n\n\tR_squared = ' + str(r_value**2) + '\n\n########################################################################')
            f2.close()





            
        #time_t.append(time)
        #radius_t.append(radius)




        
    plt.xlabel('$t(s)$')
    plt.ylabel('$f(t) =$ Radius $(\mu m)$')
    plt.legend()
    plt.title('Agrandissement du rayon en fonction du temps', fontsize = 18)
    plt.show()    
    print("\n########################################################################\n\n")
    
    
            
plot(n_analyzed, str_time)
