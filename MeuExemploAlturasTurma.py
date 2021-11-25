#%matplotlib inline
import matplotlib.pyplot as plt # plotting - é util para fazer gráficos
import seaborn as sns           # nicer plots- por mais bonito
sns.set_style('whitegrid')      # plot styling - estilo do plot

import bayesloop as bl
import numpy as np
import sympy.stats
import scipy.stats


#S é um objecto da classe Study 
S = bl.Study()

alturas =np.array( [1.7,1.65,1.8,2.0,1.56,1.62,1.75,1.68,1.5,1.82,1.72,1.69,1.66,1.72,1.75,1.87])


S.load(alturas)


# ========== Parte 1 ======= dist da mean + std

'''
#Comparar com webppl

#Definimos que o nosso modelo de observação é a gaussiana.
#Deixamos o bayesloop definir o intervalo por nos 
O = bl.om.Gaussian('media',None,'desvioPadrao',None)

#Seguidamente, correspondemos o nosso modelo de observação ao nosso estudo.
S.set(O)

#Usamos o Static para casos em que os parametros não variam com o tempo
T = bl.tm.Static()

#Seguidamente, atribuimos o nosso modelo de transição ao nosso estudo.
S.set(T)

#O algoritmo de inferencia é implementado pelo método fit
S.fit()


plt.figure(figsize=(8, 3))


# plot
plt.subplot2grid((1, 3), (0, 0), colspan=2)
S.plot('media', t=2)

plt.subplot2grid((1, 3), (0, 2))
S.plot('desvioPadrao', t=2)

#média dos dados: 1.718
#Calcular a probabilidade de a média ser > 1,718(é de esperar que a prob seja aproximadamente 50%)
S.eval('media > 1.718', t=2)
S.eval('media@2 > 1.718') #Tem o mesmo significado que o anterior

#mostrar
plt.show()

'''

# ========== Parte 2 ======= Sympy 


#'''
#Consideremos que queremos uma média fixa de 4 e queremos estudar o parametro std
#Uma vez que a média dos dados anda à volta de 1.7, é de esperar que o desvio padrao para uma media de 4, fique 'mais largo'.
media = 4
std = sympy.Symbol('desvioPadrao', positive=True)# temos de indicar que é positivo para não existir a possibilidade de existir erros

MinhaNormal = sympy.stats.Normal('normal', media, std)
O = bl.om.SymPy(MinhaNormal, 'desvioPadrao', bl.oint(0, 5, 50000))


#Seguidamente, correspondemos o nosso modelo de observação ao nosso estudo.
S.set(O)

#Usamos o Static para casos em que os parametros não variam com o tempo
T = bl.tm.Static()

#Seguidamente, atribuimos o nosso modelo de transição ao nosso estudo.
S.set(T)

#O algoritmo de inferencia é implementado pelo método fit
S.fit()


plt.figure(figsize=(8, 3))


# plot
S.plot('desvioPadrao', t=8)


#mostrar
plt.show()

#'''



