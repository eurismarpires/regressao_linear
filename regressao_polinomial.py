# -*- coding: utf-8 -*-
"""
Created on Wed Nov 23 01:31:11 2016

@author: Eurismar
"""

import pandas as pd
from matplotlib import pyplot as plt
import numpy as np

xl = pd.ExcelFile("D:/Mestrado/dados cachaça/dados2.xlsx")
df = xl.parse('orig') #planilha orig
#print(df.head())
amburana=df[0:9]
parametro = input('Informe o nome do parâmetro químico: ')


plt.plot(amburana["Mes"], amburana[parametro], 'ro')
plt.xticks(np.arange(0, 40, 4)) #intervalo
plt.grid(True)
plt.xlabel('Mes')
plt.ylabel(parametro)
plt.title('Regressão parâmetro ' + parametro )


print("------------Regressão Polinomial pelo método polyfit--------------")

##(a,b,c) = np.polyfit(amburana['Mes'],amburana[parametro],2)
#print ("Equação da Parábola: y = {0}x^2 + {1}x + {2}".format(a,b,c))

##yp = np.polyval([a,b,c],amburana["Mes"])

(a,b,c,d,e,f,g,h,i,j) = np.polyfit(amburana['Mes'],amburana[parametro],9)
print ("Equação: y = {0}x^9 + {1}x^8 + {2}x^7 + {3}x^6 + {4}x^5 + {5}x^4 + {6}x^3 + {7}x^2 + {8}x + {9}".format(a,b,c,d,e,f,g,h,i,j))

#grau = input('Informe o grau do polinomio: ')

yp = np.polyval(np.polyfit(amburana['Mes'],amburana[parametro],9),amburana["Mes"])

plt.plot(amburana["Mes"], yp, 'b')




