# -*- coding: utf-8 -*-
"""
Created on Tue Nov 22 00:26:17 2016

@author: Eurismar
"""

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
p = np.array(np.transpose(X));
q = np.array(np.transpose(Y));


(a,b,c) = np.polyfit(n, o, 2)

yp = polyval([a,b,c],X)

formula = "y = {0}x^2 + {1}x + {2}".format(a, b,c)
print(formula)

from matplotlib import pyplot as pl

pl.xlim(0,np.amax(X))
pl.ylim(np.amin(Y) - 1,np.amax(Y)+1)
pl.xticks(np.arange(min(X), max(X)+1, 4.0)) #intervalo

p = pl.plot(X,yp)
scatter(X,Y)

pl.title("Título do Gráfico")
pl.grid(True)
pl.xlabel(dados.columns[0])
pl.ylabel(dados.columns[1])
pl.show()
