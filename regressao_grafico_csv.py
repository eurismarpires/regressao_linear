# -*- coding: utf-8 -*-
"""
Created on Mon Nov 21 01:10:38 2016

@author: Eurismar
"""

import numpy as np
from sklearn.linear_model import LinearRegression
import pandas as pd #pacote para ler os dados do arquivo csv
dados = pd.read_csv("d:\dados.csv")

matriz = np.matrix(dados)
X, Y = matriz[:,0], matriz[:,1]
print(matriz)
reg = LinearRegression().fit(X,Y)
m = reg.coef_[0]
b = reg.intercept_
formula = "y = {0}x + {1}".format(m, b)
print(formula)

from matplotlib import pyplot as pl

pl.xlim(0,np.amax(X))
pl.ylim(np.amin(Y) - 1,np.amax(Y)+1)
pl.xticks(np.arange(min(X), max(X)+1, 4.0)) #intervalo
p = pl.plot(X,Y,'o', color='darkblue')
x2 = np.array([0, max(X)])
pl.plot(x2, m * x2 + b, '-k')

pl.title("Título do Gráfico")
pl.grid(True)
pl.xlabel(dados.columns[0])
pl.ylabel(dados.columns[1])
pl.show()
