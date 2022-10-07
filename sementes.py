import random
import math


#------------------ Região 1 ------------------

saida1 = open("sementes1.dat", 'w')
saida1_1 = open("reta1.dat", 'w')

x0=2.1250000000
x1=2.1250000000
y0=0.0000000000
y1=2.5000000000

x1_1=x0-0.01
x1_2=x0+0.01


for i in range(0,8000):
	a = random.uniform(x1_1, x1_2)
	e = 0.1
	inc = random.uniform(y0, y1)
	w = random.uniform(0, 360)
	O = random.uniform(0, 360)
	M = random.uniform(0, 360)

	saida1.write("{:.10f}\t{:.10f}\t{:.10f}\t{:.10f}\t{:.10f}\t{:.10f}\n ".format(a, e, inc, w,O,M))

saida1_1.write("{:.10f}\t{:.10f}\t{:.10f}\t{:.10f}\n ".format(x0,x1,y0,y1))

saida1.close()
saida1_1.close()

#------------------ Região 2 --------------------------

saida2 = open("sementes2.dat", 'w')
saida2_1 = open("reta2.dat", 'w')

x2_0=2.1250000000
x2_1=2.1490000000
y2_0=2.5000000000
y2_1=5.0000000000

x1=x2_0-0.01
x2=x2_1+0.01

# Coeficiente angular da reta original da nu6

m2 = (y2_1 -y2_0)/(x2_1 - x2_0)



semi2 = []
incli2 = []
y_r2=[]
x_2=[]

for i in range(0,15000):
	semi2.append(random.uniform(x1, x2))
	incli2.append(random.uniform(y2_0, y2_1))

	x_2.append(random.uniform(0,100))

	y_r2.append(m2*(x_2[i] - x2_0) + y2_0)


# Calculando a distância do ponto gerado (xp,yp)=(sma, inc)

distancia2 = []

for i1 in range(len(semi2)):
	v1 = x2_1 - x2_0
	v2 = y2_1 - y2_0
	mod_v = math.sqrt(v1*v1+v2*v2)

	pip0_1 = (x2_0 - semi2[i1])
	pip0_2 = (y2_0 - incli2[i1])

	prod_vet = (v1*pip0_2) - (v2*pip0_1)

	mod_prod_vet = math.sqrt(prod_vet*prod_vet)

	distancia2.append(mod_prod_vet/mod_v)


i3 = 1
e = 0.1

w2 = []
O2 = []
M2 = []

for i in range(0,15000):
	w2.append(random.uniform(0, 360))
	O2.append(random.uniform(0, 360))
	M2.append(random.uniform(0, 360))

for i2 in range(len(semi2)):
	if (semi2[i2] >= x1 and incli2[i2] >= y2_0 and distancia2[i2]<=0.01):
		if i3 <= 4000:
			saida2.write("{:.10f}\t{:.10f}\t{:.10f}\t{:.10f}\t{:.10f}\t{:.10f}\n ".format(semi2[i2], e, incli2[i2], w2[i2],O2[i2],M2[i2]))
			i3 = i3+1
		

saida2_1.write("{:.10f}\t{:.10f}\t{:.10f}\t{:.10f}\n ".format(x2_0,x2_1,y2_0,y2_1))

	


saida2.close()
saida2_1.close()



#------------------ Região 3 ---------------------------

saida3 = open("sementes3.dat", 'w')
saida3_1 = open("reta3.dat", 'w')

x3_0=2.1490000000
x3_1=2.1840000000
y3_0=5.0000000000
y3_1=7.5000000000

x3=x3_0-0.01
x3_2=x3_1+0.01

# Coeficiente angular da reta original da nu6

m3 = (y3_1 -y3_0)/(x3_1 - x3_0)

semi3 = []
incli3 = []

x_3 = []
y_r3 = []

for i in range(0,15000):
	semi3.append(random.uniform(x3, x3_2))
	incli3.append(random.uniform(y3_0, y3_1))

	x_3.append(random.uniform(0,100))

	y3 = m3*(x_3[i] - x3_0) + y3_0

	y_r3.append(y3)




# Calculando a distância do ponto gerado (xp,yp)=(sma, inc)

distancia3 = []

for i1 in range(len(semi3)):
	v1 = x3_1 - x3_0
	v2 = y3_1 - y3_0
	mod_v = math.sqrt(v1*v1+v2*v2)

	pip0_1 = (x3_0 - semi3[i1])
	pip0_2 = (y3_0 - incli3[i1])

	prod_vet = (v1*pip0_2) - (v2*pip0_1)

	mod_prod_vet = math.sqrt(prod_vet*prod_vet)

	distancia3.append(mod_prod_vet/mod_v)


i3 = 1
e = 0.1

w3 = []
O3 = []
M3 = []

for i in range(0,15000):
	w3.append(random.uniform(0, 360))
	O3.append(random.uniform(0, 360))
	M3.append(random.uniform(0, 360))

for i2 in range(len(semi3)):
	if (semi3[i2] >= x3 and incli3[i2] >= y3_0 and distancia3[i2]<=0.01):
		if i3 <= 4000:
			saida3.write("{:.10f}\t{:.10f}\t{:.10f}\t{:.10f}\t{:.10f}\t{:.10f}\n ".format(semi3[i2], e, incli3[i2], w3[i2],O3[i2],M3[i2]))
			i3 = i3+1

saida3_1.write("{:.10f}\t{:.10f}\t{:.10f}\t{:.10f}\n ".format(x3_0,x3_1,y3_0,y3_1))
		
saida3.close()


	
#------------------ Região 4 ---------------------------

saida4 = open("sementes4.dat", 'w')
saida4_1 = open("reta4.dat", 'w')

x4_0=2.1840000000
x4_1=2.2150000000
y4_0=7.5000000000
y4_1=10.0000000000

x4=x4_0-0.01
x4_2=x4_1+0.01

# Coeficiente angular da reta original da nu6

m4 = (y4_1 -y4_0)/(x4_1 - x4_0)

semi4 = []
incli4 = []
x_4 = []
y_r4 = []

for i in range(0,15000):
	semi4.append(random.uniform(x4, x4_2))
	incli4.append(random.uniform(y4_0, y4_1))

	x_4.append(random.uniform(0,100))

	y4 = m4*(x_4[i] - x4_0) + y4_0

	y_r4.append(y4)



# Calculando a distância do ponto gerado (xp,yp)=(sma, inc)

distancia4 = []

for i1 in range(len(semi4)):
	v1 = x4_1 - x4_0
	v2 = y4_1 - y4_0
	mod_v = math.sqrt(v1*v1+v2*v2)

	pip0_1 = (x4_0 - semi4[i1])
	pip0_2 = (y4_0 - incli4[i1])

	prod_vet = (v1*pip0_2) - (v2*pip0_1)

	mod_prod_vet = math.sqrt(prod_vet*prod_vet)

	distancia4.append(mod_prod_vet/mod_v)


i3 = 1
e = 0.1

w4 = []
O4 = []
M4 = []

for i in range(0,15000):
	w4.append(random.uniform(0, 360))
	O4.append(random.uniform(0, 360))
	M4.append(random.uniform(0, 360))

for i2 in range(len(semi4)):
	if (semi4[i2] >= x4 and incli4[i2] >= y4_0 and distancia4[i2]<=0.01):
		if i3 <= 4000:
			saida4.write("{:.10f}\t{:.10f}\t{:.10f}\t{:.10f}\t{:.10f}\t{:.10f}\n ".format(semi4[i2], e, incli4[i2], w4[i2],O4[i2],M4[i2]))
			i3 = i3+1
		
saida4_1.write("{:.10f}\t{:.10f}\t{:.10f}\t{:.10f}\n ".format(x4_0,x4_1,y4_0,y4_1))

saida4_1.close()
saida4.close()

#------------------ Região 5 ---------------------------

saida5 = open("sementes5.dat", 'w')
saida5_1 = open("reta5.dat", "w")

x5_0=2.2150000000
x5_1=2.2790000000
y5_0=10.0000000000
y5_1=12.5000000000

x5=x5_0-0.01
x5_2=x5_1+0.01

# Coeficiente angular da reta original da nu6

m5 = (y5_1 -y5_0)/(x5_1 - x5_0)

semi5 = []
incli5 = []
x_5=[]
y_r5=[]

for i in range(0,15000):
	semi5.append(random.uniform(x5, x5_2))
	incli5.append(random.uniform(y5_0, y5_1))

	x_5.append(random.uniform(0,100))

	y5 = m5*(x_5[i] - x5_0) + y5_0

	y_r5.append(y5)


# Calculando a distância do ponto gerado (xp,yp)=(sma, inc)

distancia5 = []

for i1 in range(len(semi5)):
	v1 = x5_1 - x5_0
	v2 = y5_1 - y5_0
	mod_v = math.sqrt(v1*v1+v2*v2)

	pip0_1 = (x5_0 - semi5[i1])
	pip0_2 = (y5_0 - incli5[i1])

	prod_vet = (v1*pip0_2) - (v2*pip0_1)

	mod_prod_vet = math.sqrt(prod_vet*prod_vet)

	distancia5.append(mod_prod_vet/mod_v)


i3 = 1
e = 0.1

w5 = []
O5 = []
M5 = []

for i in range(0,15000):
	w5.append(random.uniform(0, 360))
	O5.append(random.uniform(0, 360))
	M5.append(random.uniform(0, 360))

for i2 in range(len(semi5)):
	if (semi5[i2] >= x5 and incli5[i2] >= y5_0 and distancia5[i2]<=0.01):
		if i3 <= 2000:
			saida5.write("{:.10f}\t{:.10f}\t{:.10f}\t{:.10f}\t{:.10f}\t{:.10f}\n ".format(semi5[i2], e, incli5[i2], w5[i2],O5[i2],M5[i2]))
			i3 = i3+1
		

saida5_1.write("{:.10f}\t{:.10f}\t{:.10f}\t{:.10f}\n ".format(x5_0,x5_1,y5_0,y5_1))

saida5_1.close()
saida5.close()


#------------------ Região 6 ---------------------------

saida6 = open("sementes6.dat", 'w')
saida6_1 = open("reta6.dat", "w")

x6_0=2.2790000000
x6_1=2.3480000000
y6_0=12.5000000000
y6_1=15.0000000000

x6=x6_0-0.01
x6_2=x6_1+0.01

# Coeficiente angular da reta original da nu6

m6 = (y6_1 -y6_0)/(x6_1 - x6_0)

semi6 = []
incli6 = []
x_6=[]
y_r6=[]

for i in range(0,15000):
	semi6.append(random.uniform(x6, x6_2))
	incli6.append(random.uniform(y6_0, y6_1))

	x_6.append(random.uniform(0,100))

	y6 = m6*(x_6[i] - x6_0) + y6_0

	y_r6.append(y6)


# Calculando a distância do ponto gerado (xp,yp)=(sma, inc)

distancia6 = []

for i1 in range(len(semi6)):
	v1 = x6_1 - x6_0
	v2 = y6_1 - y6_0
	mod_v = math.sqrt(v1*v1+v2*v2)

	pip0_1 = (x6_0 - semi6[i1])
	pip0_2 = (y6_0 - incli6[i1])

	prod_vet = (v1*pip0_2) - (v2*pip0_1)

	mod_prod_vet = math.sqrt(prod_vet*prod_vet)

	distancia6.append(mod_prod_vet/mod_v)


i3 = 1
e = 0.1

w6 = []
O6 = []
M6 = []

for i in range(0,15000):
	w6.append(random.uniform(0, 360))
	O6.append(random.uniform(0, 360))
	M6.append(random.uniform(0, 360))

for i2 in range(len(semi6)):
	if (semi6[i2] >= x6 and incli6[i2] >= y6_0 and distancia6[i2]<=0.01):
		if i3 <= 2000:
			saida6.write("{:.10f}\t{:.10f}\t{:.10f}\t{:.10f}\t{:.10f}\t{:.10f}\n ".format(semi6[i2], e, incli6[i2], w6[i2],O6[i2],M6[i2]))
			i3 = i3+1

saida6_1.write("{:.10f}\t{:.10f}\t{:.10f}\t{:.10f}\n ".format(x6_0,x6_1,y6_0,y6_1))
		
saida6_1.close()
saida6.close()

#------------------ Região 7 ---------------------------

saida7 = open("sementes7.dat", 'w')
saida7_1 = open("reta7.dat", "w")

x7_0=2.3480000000
x7_1=2.5000000000
y7_0=15.0000000000
y7_1=17.2000000000

x7=x7_0-0.01
x7_2=x7_1+0.01

# Coeficiente angular da reta original da nu6

m7 = (y7_1 -y7_0)/(x7_1 - x7_0)

semi7 = []
incli7 = []
x_7=[]
y_r7=[]

for i in range(0,30000):
	semi7.append(random.uniform(x7, x7_2))
	incli7.append(random.uniform(y7_0, y7_1))

	x_7.append(random.uniform(0,100))

	y7 = m7*(x_7[i] - x7_0) + y7_0

	y_r7.append(y7)



# Calculando a distância do ponto gerado (xp,yp)=(sma, inc)

distancia7 = []

for i1 in range(len(semi7)):
	v1 = x7_1 - x7_0
	v2 = y7_1 - y7_0
	mod_v = math.sqrt(v1*v1+v2*v2)

	pip0_1 = (x7_0 - semi7[i1])
	pip0_2 = (y7_0 - incli7[i1])

	prod_vet = (v1*pip0_2) - (v2*pip0_1)

	mod_prod_vet = math.sqrt(prod_vet*prod_vet)

	distancia7.append(mod_prod_vet/mod_v)


i7 = 1
e = 0.1

w7 = []
O7 = []
M7 = []

for i in range(0,30000):
	w7.append(random.uniform(0, 360))
	O7.append(random.uniform(0, 360))
	M7.append(random.uniform(0, 360))

for i2 in range(len(semi7)):
	if (semi7[i2] >= x7 and incli7[i2] >= y7_0 and distancia7[i2]<=0.01):
		if i7 <= 2000:
			saida7.write("{:.10f}\t{:.10f}\t{:.10f}\t{:.10f}\t{:.10f}\t{:.10f}\n ".format(semi7[i2], e, incli7[i2], w7[i2],O7[i2],M7[i2]))
			i7 = i7+1

saida7_1.write("{:.10f}\t{:.10f}\t{:.10f}\t{:.10f}\n ".format(x7_0,x7_1,y7_0,y7_1))
		
saida7_1.close()
saida7.close()
