import pandas as pd
import pyautogui as pyg
import PySimpleGUI as psg
import xlrd, os
from time import sleep


working_directory = os.getcwd()

#simple GUI interface
layout = [
    [psg.Text('Abrir arquivo:'), psg.InputText(key="-FILE_PATH-"), psg.FileBrowse(initial_folder=working_directory, file_types = [("CSV File", "xlsx")])],
    [psg.Button('->'), psg.Exit()]
]

window = psg.Window("PagAUTO", layout, keep_on_top=True)

#take the file in the directory and turn in to a dataframe
def get_df(file_address):
    df = pd.read_excel(file_address)
    return df

#main loop
while True:
    event, values = window.read()
    if event in (psg.WIN_CLOSED, 'Exit'):
        exit()
    
    elif event == "->":
        file_address = values["-FILE_PATH-"]
        print(get_df(file_address))
         
window.close()
         
def cad_doc():  
    pyg.click(704,77) #click em incluir
    sleep(0.3)
    pyg.click(226,182, duration=1)
    pyg.press('f2')
    pyg.write(str(i.nome))
    sleep(0.3)
    pyg.press('f4')
    sleep(1)
    
    if check_situac() != None:
        pyg.doubleClick(620,428, duration=1)
        sleep(0.3)
        pyg.press('tab')
        pyg.write('0')
        sleep(0.3)
        pyg.press('tab')
        pyg.write(str(i.documento))
        sleep(0.3)
        pyg.press('tab')
        pyg.write('SAL')
        sleep(0.3)
        pyg.press('tab')
        pyg.write('1')
        sleep(0.3)
        pyg.press('tab')
        pyg.write('1')
        sleep(0.3)
        pyg.press('tab')
        sleep(0.3)
        pyg.press('tab')
        pyg.write('237')
        sleep(0.3)
        pyg.press('tab')
        pyg.press('tab')
        pyg.write('250520230800')
        sleep(0.3)
        pyg.press('tab')
        pyg.write('250520230800')
        sleep(0.3)
        pyg.press('tab')
        pyg.write(str(i.salario))
        sleep(0.3)
        pyg.click(408,525, duration=0.5)
        pyg.write('PAGAMENTO SALARIO 04/2023')
        sleep(0.3)
        pyg.press('tab')
        pyg.write('24')
        pyg.click(755,79, duration= 1) # click em salvar
        sleep(0.3)
        cad_parc()
    else:
        log_erro()
        pyg.click(1046,181, duration=0.5)
              
def cad_parc():
    pyg.click(111,157, duration=0.5)
    sleep(0.3)
    pyg.click(22,183, duration=0.5)
    sleep(0.3)
    pyg.click(851,188, duration=0.5)
    sleep(0.3)

def pag_clas():
    pyg.click(29,205, duration=0.5)
    pyg.write('3')
    s2
    pyg.press('tab')
    pyg.write('1')
    s2
    pyg.press('tab')
    pyg.write('3')
    s2
    pyg.press('tab')
    pyg.write('44')
    s2
    pyg.press('tab')
    pyg.write('45')
    s2
    pyg.press('tab')
    pyg.write(str(i.salario))

def check_situac():
    situac = pyg.locateOnScreen('func_ativo.png', region=(294,398, 350,440))
    return situac

def log_erro():
    with open("log_erro.txt", "a") as arquivo:
        arquivo.write(i.nome)
        arquivo.write('\n')
 

for i in df.itertuples(): 
    documento = cad_doc()
