# -*- coding: utf-8 -*-
"""
Created on Mon Dec 19 19:36:05 2016

@author: Eurismar
"""
import pandas as pd
import numpy as np
xl = pd.ExcelFile("D:/dados2.xlsx")
df = xl.parse('orig')
barril1 = df[:9]
dados = np.column_stack((barril1["Mes"],barril1["AlcoolAp"]))
texto = []
arq = open('D:/teste/panda.txt','w')
for e in dados:
    linha = str(e[0]) +"," + str(e[1]) + "\n"      
    texto.append(linha)
print(texto)

arq.writelines(texto) 
arq.close()

print("terminou!!!")
