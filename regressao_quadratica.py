#http://conteudo.icmc.usp.br/pessoas/andretta/ensino/aulas/sme0500-1-09/MinimosQuadradosDiscreto.pdf
>>> import numpy as np
>>> xi=np.array([-2.00,-1.00,0.00,1.00,2.00,3.00])
>>> x2=(xi*xi)
>>> x2
array([ 4.,  1.,  0.,  1.,  4.,  9.])
>>> x3=(xi*xi*xi)
>>> x3
array([ -8.,  -1.,   0.,   1.,   8.,  27.])
>>> x4=(x2*x2)
>>> x4
array([ 16.,   1.,   0.,   1.,  16.,  81.])
>>> f_xi=np.array([19.01,3.99,-1,4.01,18.99,45.00])
>>> f_xi
array([ 19.01,   3.99,  -1.  ,   4.01,  18.99,  45.  ])
>>> xi_fxi=(xi*f_xi)
>>> xi_fxi
array([ -38.02,   -3.99,   -0.  ,    4.01,   37.98,  135.  ])
>>> x2_fxi=(xi*f_xi)
>>> x2_fxi
array([ -38.02,   -3.99,   -0.  ,    4.01,   37.98,  135.  ])
>>> x2_fx2=(x2 * f_xi)
array([  76.04,    3.99,   -0.  ,    4.01,   75.96,  405.  ])

