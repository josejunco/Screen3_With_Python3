#josejunco
import os
import matplotlib.pyplot as plt # paquete matplotlib
#import pandas as pd  #paquete panda, estructura de datos
import numpy as np  # paquete numpy
from matplotlib import style
from scipy.interpolate import make_interp_spline, BSpline

style.use('fivethirtyeight')
#Abrir el archivo para modificarlo
f = open ('DFP.DAT','r')
m = f.read()
print(m)
f.close()
#Nombre deñ proyecto
N='JoseJunco'
#Tipo de fuente
Tso='P'
# Tasa de emision
Q='1300.00'
#Altura de chimenea
Hs='120.000'
Ds='1.20000'
Vs='10.00000'
Tf='588.000'
Ta='298.000'
Fp='0.00000'  #FLAGPOLE
Z_U_R='R'
Bd='N'
T_CX='N' #Terreno complejo
T_SP='N' #Terrenon simple sin elevacion
Met='3'
St='4'#Estabilidad
V_ane='3.100000' #Velocidad a la altura del anemometro
D_array='Y'
Min_Max_D='1000.00,3000.00'
D_D='N' #Distancia discreta
Fm='N' #Fumigación
Impr='Y' #Imprimir una copia


f = open('DFP.DAT','w')
f.write(N+'\n')
f.write(Tso+'          10.0\n')
f.write('   '+Q+'\n')
f.write('   '+Hs+'\n')
f.write('   '+Ds+'\n')
f.write('  '+Vs+'\n')
f.write('   '+Tf+'\n')
f.write('   '+Ta+'\n')
f.write('   '+Fp+'\n')
f.write(Z_U_R+'\n')
f.write(Bd+'\n')
f.write(T_CX+'\n')
f.write(T_SP+'\n')
f.write('           '+Met+'\n')
f.write('           '+St+'\n')
f.write('   '+V_ane+'\n')
f.write(D_array+'\n')
f.write('  '+Min_Max_D+'\n')
f.write(D_D+'\n')
f.write(Fm+'\n')
f.write(Impr+'\n')

f.close()

#EJECUTA EL SCREEN3
cmd = "SCREEN3 <DFP.DAT"
returned_value = os.system(cmd)


print ("*** Lectura archivo DAT ***")
d1 = []
d = []
cnc = []
data = []
with open("SCREEN.OUT") as f:
	for line in f:
		data.extend(line.split())
f.close()

j=179
for line in data:
	if data.index(line) >= 179 :
		d1.append(data[j])
		j=j+1

	if data[j] == 'MAXIMUM':
	#if data[j] == 'ITERATION':
		break

#d=float(d)
n=len(d1)/10
n=int(n)

m=0
for x in range(0,n):
	d.append(float(d1[m]))
	cnc.append(float(d1[m+1]))
	m=m+10


link=data.index('MAXIMUM')
dist=data[link+8]
conc=data[link+9]
dist=float(dist)
dist=int(dist)
dist=str(dist)
conc=float(conc)
conc=str(conc)


#Suavizado
ds = np.array(d)
x = np.linspace(ds.min(),ds.max(),300) #300 represents number of points to make between T.min and T.max
#QS
spl = make_interp_spline(ds, cnc, k=3) #BSpline object
y = spl(x)
#Grafica
fig, ax = plt.subplots(figsize=(9,5))
#Grillado
ax.grid (True)
ax.set_title("Concentración vs Distancia",fontsize=21)
axes = plt.gca()
ax.set(xlabel='Distancia (m)', ylabel='Concentración (ug/m3)')
axes.xaxis.label.set_size(17)
axes.yaxis.label.set_size(17)
#ax.plot(d,cnc,"-", alpha=0.8,linewidth=5,color='b', label='SCREEN3\nMáx. Conc.: '+conc+' ug/m3\nDist: '+dist+' m.')
plt.plot(x,y,linewidth=3,color='#ff3108',label='SCREEN3\nMáx. Conc.: '+conc+' ug/m3\nDistancia: '+dist+' m.')
ax.legend()
plt.tight_layout()
plt.savefig('screen3.png')
plt.show()








