import numpy as np


n = 1
total = 5000


for i in range(n,total):


	t = np.genfromtxt(str(i)+'.aei', usecols=0,unpack=False)
	a = np.genfromtxt(str(i)+'.aei', usecols=1,unpack=False)
	e = np.genfromtxt(str(i)+'.aei', usecols=2,unpack=False)
	incli = np.genfromtxt(str(i)+'.aei', usecols=3,unpack=False)
	d = np.genfromtxt(str(i)+'.aei', usecols=4,unpack=False)
	outputFilep = open('outMillena/pequeno_'+str(i)+'.aei',"w")
	outputFilem = open('outMillena/medio_'+str(i)+'.aei',"w")
	outputFileg = open('outMillena/grande_'+str(i)+'.aei',"w")

	for j in range(len(t)):
		# Intervalo pequeno
		if ((a[j] >= 1.18 and a[j]<=1.20) and (e[j]>=0.18 and e[j]<=0.20) and (incli[j]>=5.8 and incli[j]<=6.0)):
			outputFilep.write("%10f  %10f  %10f  %10f  %10f\n" % (t[j], a[j], e[j], incli[j], d[j]))
		# Intervalo médio
		elif ((a[j] >= 1.17 and a[j]<=1.21) and (e[j]>=0.17 and e[j]<=0.21) and (incli[j]>=5.7 and incli[j]<=6.1)):
			outputFilem.write("%10f  %10f  %10f  %10f  %10f\n" % (t[j], a[j], e[j], incli[j], d[j]))
		#Intervalo grande
		elif ((a[j] >= 1.14 and a[j]<=1.24) and (e[j]>=0.14 and e[j]<=0.24) and (incli[j]>=5.4 and incli[j]<=6.4)):
			outputFileg.write("%10f  %10f  %10f  %10f  %10f\n" % (t[j], a[j], e[j], incli[j], d[j]))



	outputFilep.close()
	outputFilem.close()
	outputFileg.close()


# t = None
# a = None
# e = None
# incli = None
# d = None
# del t
# del a
# del e
# del incli
# del d
