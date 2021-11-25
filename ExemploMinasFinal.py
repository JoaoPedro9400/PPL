#%matplotlib inline
import matplotlib.pyplot as plt # plotting - é util para fazer gráficos
import seaborn as sns           # nicer plots- por mais bonito
sns.set_style('whitegrid')      # plot styling - estilo do plot

import numpy as np


import bayesloop as bl

#Study é uma classe
#S é um objecto da classe Study 
S = bl.Study()

'''
Os dados seguintes são todos os acidentes que houveram em minas em UK por ano,
desde 1851 a 1962.
'''

#data é um array em que cada elemento é o numero de acidentes no ano respetivo
data = np.array([5, 4, 1, 0, 4, 3, 4, 0, 6, 3, 3, 4, 0, 2, 6, 3, 3, 5, 4, 5, 3, 1, 4,
                 4, 1, 5, 5, 3, 4, 2, 5, 2, 2, 3, 4, 2, 1, 3, 2, 2, 1, 1, 1, 1, 3, 0,
                 0, 1, 0, 1, 1, 0, 0, 3, 1, 0, 3, 2, 2, 0, 1, 1, 1, 0, 1, 0, 1, 0, 0,
                 0, 2, 1, 0, 0, 0, 1, 1, 0, 2, 3, 3, 1, 1, 2, 1, 1, 1, 1, 2, 3, 3, 0,
                 0, 0, 1, 4, 0, 0, 0, 1, 0, 0, 0, 0, 0, 1, 0, 0, 1, 0])



#object.load(data,data time) => len(data)=len(data time)
time = np.arange(1851, 1961)
S.load(data, timestamps=time) # timestamps é opcional


#Como são eventos discretos, usamos a dist de poisson
L = bl.observationModels.Poisson('taxaAcidentes', bl.oint(0, 6, 1000))

#Com o método set correspondemos o modelo de observação ao nosso estudo
S.set(L)


# ========= PARTE 1 ==========

'''
#Variação do parametro segundo uma gaussiana
T = bl.transitionModels.GaussianRandomWalk('sigma', 0.2, target='taxaAcidentes')

S.set(T)

#Implementar o algoritmo de inferencia
S.fit()


plt.figure(figsize=(8, 4))

# plot dos dados iniciais
plt.bar(S.rawTimestamps, S.rawData, align='center', facecolor='r', alpha=.5)


# plot da variação do parametro
S.plot('taxaAcidentes')

plt.xlim([1851, 1962])#limitar o eixo do x
plt.xlabel('ano');#legendar o eixo do x
plt.ylabel('Numero de acidentes')
plt.show()

#calcular a probabilidade de a taxa de acidentes em 1960 ser maior que a taxa de acidentes em 1860.

S.eval('taxaAcidentes@1960 > taxaAcidentes@1860')


plt.show()

'''
#========= PARTE 2 ==========

'''
#Variação do parametro segundo uma gaussiana
T = bl.transitionModels.GaussianRandomWalk('sigma', 0.2, target='taxaAcidentes')

S.set(T)

#Implementar o algoritmo de inferencia
S.fit()

#Imaginemos agora que queremos ver a probabilidade da taxa de acidentes ser maior do que 2, para todo o tempo entre 1851 e 1961:

P = bl.Parser(S)

p_ar = []

for tempo in time:
	p_ar.append(P('taxaAcidentes > 2',t=tempo, silent=True)) 
#o silent é apenas para nao printar na linha de comandos


plt.figure(figsize=(10, 6))

# Grafico com a variação do parametro
plt.subplot2grid((2, 1), (0, 0))
S.plot('taxaAcidentes')
plt.axhline(y=2, c='0.2', ls='dashed', lw=1)
plt.xlim([1851, 1962])

#grafico com a probabilidade
plt.subplot2grid((2, 1), (1, 0))
plt.plot(p_ar, c='0.3', lw=2)
plt.fill_between(time, p_ar, 0, color='k', alpha=0.2)
plt.xlim([1851, 1962])
plt.ylim([-0.05, 1.05])
plt.xlabel('Time')
plt.ylabel('p(taxaAcidentes > 2)');

plt.show()


'''
# ========= PARTE 3 ========== Parametros invariantes no tempo


#obj

'''
#Agora vamos considerar o caso em que o parametro não varia com o tempo e vamos querer saber a distribuição do parametro que origina os resultados mostrados anteriormente.


#Static => parametros invariantes no tempo
T = bl.transitionModels.Static()
S.set(T)

S.fit()

# Figura 1

plt.figure(figsize=(10, 6))
plt.subplot2grid((2, 1), (0, 0))
plt.xlim([1,3])
plt.ylim([0,3.5])

#t = tempo para o qual a dist. do parametro é calculada
#density=True => é plotada a dens de prob
S.plot('taxaAcidentes',t=1860,color='r',density=True)
# ou 
#S.getParameterDistribution(1860,'taxaAcidentes',plot=True,density=True)
plt.ylabel('dens. probabilidade(t=1860)')


plt.subplot2grid((2, 1), (1, 0))
plt.xlim([1,3])
plt.ylim([0,3.5])
#Para t=1960 tem de dar o mesmo
S.plot('taxaAcidentes',t=1960)
plt.ylabel('dens. probabilidade(t=1960)')

# Figura 2

plt.figure(figsize=(10, 6))
plt.subplot2grid((2, 1), (0, 0))
plt.xlim([1,3])
plt.ylim([0,3.5])

#t = tempo para o qual a dist. do parametro é calculada
#density=True => é plotada a dens de prob
S.plot('taxaAcidentes',t=1860,color='r',density=True)
plt.ylabel('dens. probabilidade(t=1860)')


plt.subplot2grid((2, 1), (1, 0))
plt.xlim([1,3])
plt.ylim([0,0.2])
#Como temos density=false fornece os valores das probabilidades
S.plot('taxaAcidentes',t=1860,color='g',density=False)
plt.ylabel('probabilidade(t=1860)')

plt.show()

'''
