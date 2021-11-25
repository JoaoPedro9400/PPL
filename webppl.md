#Poisson
#Acidentes nas minas

~~~~
/*
Objetivo: Distribuiçao do parametro mais provavel para obter os dados acidentesPorAno.
*/

var acidentesPorAno =[5, 4, 1, 0, 4, 3, 4, 0, 6, 3, 3, 4, 0, 2, 6, 3, 3, 5, 4, 5, 3, 1, 4,
                      4, 1, 5, 5, 3, 4, 2, 5, 2, 2, 3, 4, 2, 1, 3, 2, 2, 1, 1, 1, 1, 3, 0,
                      0, 1, 0, 1, 1, 0, 0, 3, 1, 0, 3, 2, 2, 0, 1, 1, 1, 0, 1, 0, 1, 0, 0,
                      0, 2, 1, 0, 0, 0, 1, 1, 0, 2, 3, 3, 1, 1, 2, 1, 1, 1, 1, 2, 3, 3, 0,
                      0, 0, 1, 4, 0, 0, 0, 1, 0, 0, 0, 0, 0, 1, 0, 0, 1, 0]

var mediaAcidentesPorAno = sum(acidentesPorAno)/acidentesPorAno.length
console.log('mediaAcidentesPorAno:',mediaAcidentesPorAno)


var modelo = function(){
  var lambda = uniform({a:0,b:6})
  map(function(x){observe(Poisson({mu:lambda}), x)}, acidentesPorAno)
  return {'taxaAcidentes':lambda}
}

Infer({method: 'MCMC', samples: 80000, model: modelo})

//Temos na maior parte dos casos o valor máximo em 1.7 que corresponde aprox à média de 
//acidentes por ano= 1.6909
~~~~

#Gaussiana
#Altura dos alunos de uma turma - Parte 1

~~~~
/*
Objetivo: Calcular a distribuição dos parametros(media e desvio padrao) 
dadas as alturas de uma turma. 
*/

var alturas = [1.7,1.65,1.8,2.0,1.56,1.62,1.75,1.68,1.5,1.82,1.72,1.69,1.66,1.72,1.75,1.87]

console.log('media',sum(alturas)/alturas.length)
console.log('desvio padrao',listStdev(alturas))

//_.min(array) calcula o minimo de um array - javascript

var modelo = function() {
   var mu = uniform(_.min(alturas), _.max(alturas)) // da-nos um valor REAL entre min e max com = prob
   var sigma = uniform(0,0.3)
   map(function(a) {observe(Gaussian({mu, sigma}), a)}, alturas)
  //Podemos pensar nas linhas anteriores como:
  /*
  var alturasExp = mapN(function(x){ return sample(Gaussian(mu,sigma))}, alturas.length)
  condition(alturasExp==alturas)
  */
   return {'mean':mu,'std':sigma}
}


viz.marginals(Infer({method: 'MCMC', samples: 80000, model: modelo}))
~~~~

#Altura dos alunos de uma turma - Parte 2

~~~~
/*
Objetivo: Calcular a distribuição do parametro desvio padrao considerando a média fixa(4)
dadas as alturas de uma turma. 
*/

var alturas = [1.7,1.65,1.8,2.0,1.56,1.62,1.75,1.68,1.5,1.82,1.72,1.69,1.66,1.72,1.75,1.87]


var modelo = function() {
   var mu = 4
   var sigma = uniform(1,5)
   map(function(a) {observe(Gaussian({mu, sigma}), a)}, alturas)
   return {'std':sigma}
}

//Como sabemos o valor medio dos dados é 1.72 aprox.
//Uma vez que fixamos a média da distribuição em 4, então é de esperar que tenhamos aproximadamente
//em 4 - 1.72 = 2.28 o pico maximo da densidade de prob. 
viz.marginals(Infer({method: 'MCMC', samples: 50000, model: modelo}))
~~~~
