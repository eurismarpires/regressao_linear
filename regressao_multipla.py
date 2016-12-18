
import numpy as np
import statsmodels.api as sm
import statsmodels.formula.api as smf
import pandas as pd

reader = pd.read_csv('http://www-bcf.usc.edu/~gareth/ISL/Advertising.csv', index_col=0)
y = reader["Sales"]
x1 = reader["TV"]
x2 = reader["Radio"]
x3 = reader["Newspaper"]



x = np.column_stack((x1,x2,x3))
x = sm.add_constant(x, prepend=True)

results = smf.OLS(y,x).fit()
print(results.summary())
