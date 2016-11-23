import pandas as pd
import statsmodels.formula.api as sm
from matplotlib import pyplot as plt
import numpy as np

xl = pd.ExcelFile("D:/Mestrado/dados cachaça/dados2.xlsx")
df = xl.parse('orig') #planilha orig
#print(df.head())
amburana=df[0:9]
parametro = input('Informe o nome do parâmetro químico: ')

model = sm.ols(formula=parametro +' ~ Mes', data=amburana)
fitted = model.fit()
print(fitted.summary())

plt.plot(amburana["Mes"], amburana[parametro], 'ro')
plt.plot(amburana["Mes"], fitted.fittedvalues, 'b')
plt.xticks(np.arange(0, 40, 4)) #intervalo
plt.grid(True)
plt.xlabel('Mes')
plt.ylabel(parametro)
plt.title('Regressão parâmetro ' + parametro )






