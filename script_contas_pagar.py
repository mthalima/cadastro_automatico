import pandas as pd
import pyautogui as pyg
from time import sleep

df = pd.read_excel('lista_pagamento.xlsx')

#print(df)

sleep(2)

s1 = sleep(0.5)
s2= sleep(0.3)

def cad_doc():
    pyg.click(226,182, duration=1)
    s1
    pyg.press('f2')
    pyg.write(str(i.nome))
    s1
    pyg.press('f4')
    pyg.doubleClick(620,428, duration=1)
    s1
    pyg.press('tab')
    pyg.write('0')
    s1
    pyg.press('tab')
    pyg.write(str(i.documento))
    s1
    pyg.press('tab')
    pyg.write('SAL')
    s1
    pyg.press('tab')
    pyg.write('1')
    s1
    pyg.press('tab')
    pyg.write('1')
    s1
    pyg.press('tab')
    s1
    pyg.press('tab')
    pyg.write('237')
    s1
    pyg.press('tab')
    pyg.press('tab')
    pyg.write('230520230800')
    s1
    pyg.press('tab')
    pyg.write('230520230800')
    s1
    pyg.press('tab')
    pyg.write(str(i.salario))
    s1
    pyg.click(408,525, duration=0.5)
    pyg.write('PAGAMENTO SALARIO 04/2023')
    pyg.click(755,79, duration= 1)
    
    cad_parc()
    cad_parc()
    
    pyg.press('enter')
    
def cad_parc():
    pyg.click(111,157, duration=0.5)
    s1
    pyg.click(22,183, duration=0.5)
    pyg.click(851,188, duration=0.5)
    
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

 
for i in df.itertuples(): 
    cad_doc()