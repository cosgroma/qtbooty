# from scipy.stats import norm
# from numpy import linspace
# from pylab import plot,show,hist,figure,title

y = [10,13,11,15,10,12,10,11,12,9,11,16,10,10,14,17,8,13,14,15,11,15,23,12,13,13,11,10,16,11,17,16,19,11,12,11,9,15,17,19,14,16,20,11,8,6,12,9,16,13,8,14,8,19,15,9,9,7,11,20,12,15,21,12,8,19,19,14,15,17,19,17,10,9,16,15,10,10,15,14,15,14,13,11,16,15,12,10,17,9,12,13,21,15,9,9,6,14,16,16]

# param = norm.fit(samp) # distribution fitting

# # now, param[0] and param[1] are the mean and
# # the standard deviation of the fitted distribution
# x = linspace(-5,5,100)
# # fitted distribution
# pdf_fitted = norm.pdf(x,loc=param[0],scale=param[1])
# # original distribution
# pdf = norm.pdf(x)

# title('Normal distribution')
# plot(x,pdf_fitted,'r-',x,pdf,'b-')
# hist(samp,normed=1,alpha=.3)
# show()

import matplotlib.pyplot as plt
import scipy
import scipy.stats
from statsmodels.stats.gof import *
size = len(y)
x = scipy.arange(size)
#y = scipy.int_(scipy.round_(scipy.stats.vonmises.rvs(5,size=size)*47))
h = plt.hist(y, bins=range(48), color='w')

#dist_names = ['gamma', 'beta', 'rayleigh', 'norm', 'pareto']
continuous = ['alpha',
              #'anglit',
              #'arcsine',
              'beta',
              #'betaprime',
              #'bradford',
              #'burr',
              'cauchy',
              'chi',
              'chi2',
              #'cosine',
              #'dgamma',
              #'dweibull',
              #'erlang',
              'expon',
              #'exponweib',
              'exponpow',
              #'f',
              #'fatiguelife',
              #'fisk',
              #'foldcauchy',
              #'foldnorm',
              #'frechet_r',
              #'frechet_l',
              #'genlogistic',
              #'genpareto',
              #'genexpon',
              #'genextreme',
              #'gausshyper',
              #'gamma',
              #'gengamma',
              #'genhalflogistic',
              #'gilbrat',
              #'gompertz',
              #'gumbel_r',
              #'gumbel_l',
              #'halfcauchy',
              #'halflogistic',
              #'halfnorm',
              #'hypsecant',
              #'invgamma',
              #'invgauss',
              #'invweibull',
              #'johnsonsb',
              #'johnsonsu',
              #'ksone',
              #'kstwobign',
              #'laplace',
              #'logistic',
              #'loggamma',
              #'loglaplace',
              'lognorm',
              #'lomax',
              #'maxwell',
              #'mielke',
              #'nakagami',
              #'ncx2',
              #'ncf',
              #'nct',
              'norm',
              #'pareto',
              #'pearson3',
              #'powerlaw',
              'powerlognorm',
              'powernorm',
              #'rdist',
              #'reciprocal',
              'rayleigh',
              #'rice',
              #'recipinvgauss',
              #'semicircular',
              #'t',
              #'triang',
              #'truncexpon',
              #'truncnorm',
              #'tukeylambda',
              #'uniform',
              #'vonmises',
              #'wald',
              #'weibull_min',
              #'weibull_max',
              'wrapcauchy'
              ]
discrete = ['bernoulli'	,
			'binom',
			#'boltzmann',
			#'dlaplace',
			#'geom',
			#'hypergeom',
			'logser',
			'nbinom',
			#'planck',
			'poisson',
			'randint',
			#'skellam',
			'zipf'
			]
for dist_name in continuous:
	dist = getattr(scipy.stats, dist_name)
	# param = dist.fit(y)
	#if gof_chisquare_discrete(dist, 'arg', y, .1, dist_name) == 1:
	print 'passed',dist_name
	param = dist.fit(y)
	pdf_fitted = dist.pdf(x, *param[:-2], loc=param[-2], scale=param[-1]) * size
	plt.plot(pdf_fitted, label=dist_name)
	plt.xlim(0,47)
	# else:
	# 	pass
plt.legend(loc='upper right')
plt.show()

# for dist_name in discrete:
#     dist = getattr(scipy.stats, dist_name)
#     param = dist.fit(y)
#     pdf_fitted = dist.pdf(x, *param[:-2], loc=param[-2], scale=param[-1]) * size
#     plt.plot(pdf_fitted, label=dist_name)
#     plt.xlim(0,47)
# plt.legend(loc='upper right')
# plt.show()

