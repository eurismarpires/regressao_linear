# coding: iso-8859-1 -*-
import numpy as np
x=np.array([ 128,  256,  384,  512,  640,  768,  896, 1024])
y=np.array([375,805,1444,1323,2339,3067,2458,3329])
print(x)
print(y)
y_t=y.transpose()
n=np.dot(y_t,y)
q=np.ones((8,2)) #cria uma matriz de 8 linhas e 2 colunas prenchendo com uns
i=0
while i < 8:
	q[i][1]=x[i]
	i=i+1
q_t=q.transpose() #cria uma matris transposta de q
m=np.dot(q_t,q) #multiplica a transportas pela matris normal
r=np.dot(q_t,y) #multiplica a matriz q_t por y e coloca o resultado em r
s = np.linalg.inv(m) #cria a matriz inversa de m e coloca em s
t = np.dot(r,s) #o primeiro numero é o parâmetro alfa e o segundo é o beta
print('-------REGRESSAO-------------')
print(t)

