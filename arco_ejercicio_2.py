from cmu_graphics import *
Rect(0,0,400,400,relleno=gradiente('azulMediaNoche','cian'))
#Religiones        
cristianismo = 2300
islam = 1900
hinduismo = 1200
budismo = 520 
religionesTradicionalesChina = 394
religionesAfroamericanas = 100
personasNoReligiosas = 1200

totalDeReligiones= cristianismo + islam + hinduismo + budismo + religionesTradicionalesChina+ religionesAfroamericanas+ personasNoReligiosas
print(totalDeReligiones)
porcentaje1 = (cristianismo /totalDeReligiones)
porcentaje2 = (islam /totalDeReligiones)
porcentaje3 = (hinduismo /totalDeReligiones)
porcentaje4 = (budismo /totalDeReligiones)
porcentaje5 = (religionesTradicionalesChina /totalDeReligiones)
porcentaje6 = (religionesAfroamericanas /totalDeReligiones)
porcentaje7 = (personasNoReligiosas /totalDeReligiones)

anguloDeBarrido1= int(porcentaje1*360)
anguloDeBarrido2= int(porcentaje2*360)
anguloDeBarrido3= int(porcentaje3*360)
anguloDeBarrido4= int(porcentaje4*360)
anguloDeBarrido5= int(porcentaje5*360)
anguloDeBarrido6= int(porcentaje6*360)
anguloDeBarrido7= int(porcentaje7*360)

print(porcentaje1)
print(porcentaje2)
print(porcentaje3)
print(porcentaje4)
print(porcentaje5)
print(porcentaje6)
print(porcentaje7)

print(anguloDeBarrido1)
print(anguloDeBarrido2)
print(anguloDeBarrido3)
print(anguloDeBarrido4)
print(anguloDeBarrido5)
print(anguloDeBarrido6)
print(anguloDeBarrido7)

Circle(130,240,120)
Arc(130,240,240,240,0,anguloDeBarrido1,relleno="azul")
Arc(130,240,240,240,108,anguloDeBarrido2,relleno="rojo")
Arc(130,240,240,240,197,anguloDeBarrido3,relleno="verde")
Arc(130,240,240,240,253,anguloDeBarrido4,relleno="oro")
Arc(130,240,240,240,277,anguloDeBarrido5,relleno="cian")
Arc(130,240,240,240,295,anguloDeBarrido6,relleno="purpura")
Arc(130,240,240,240,299,anguloDeBarrido7,relleno="naranja")

Rect(260,40,10,10,relleno="azul")
Rect(260,60,10,10,relleno="rojo")
Rect(260,80,10,10,relleno="verde")
Rect(260,100,10,10,relleno="oro")
Rect(260,20,10,10,relleno="cian")
Rect(260,120,10,10,relleno="purpura")
Rect(260,140,10,10,relleno="naranja")

Rotulo("cristianismo",310,42)
Rotulo("islam",310,62)
Rotulo("hinduismo",310,82)
Rotulo("budismo",310,102)
Rotulo("TradicionalesChina",330,22)
Rotulo("Afroamericanas",320,122)
Rotulo("personasNoReligiosas",338,142)                                                                                                                                                                  

cmu_graphics.run()