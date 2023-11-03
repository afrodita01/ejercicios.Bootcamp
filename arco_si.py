from cmu_graphics import*

Cristianismo=2300
Hinduismo=1200
Islam=1900
Budismo=520
ReligionesChinas=394
ReligionesAfroamericanas=100
Ateos=1200

totalDeReligiones = Cristianismo + Hinduismo + Islam + Budismo + ReligionesChinas + ReligionesAfroamericanas + Ateos
print(totalDeReligiones)
Aporcentaje=(Cristianismo/totalDeReligiones)
Bporcentaje=(Hinduismo/totalDeReligiones)
Cporcentaje=(Islam/totalDeReligiones)
Dporcentaje=(Budismo/totalDeReligiones)
Eporcentaje=(ReligionesChinas/totalDeReligiones)
Fporcentaje=(ReligionesAfroamericanas/totalDeReligiones)
Gporcentaje=(Ateos/totalDeReligiones)

AanguloDeBarrido = int(Aporcentaje * 360)
BanguloDeBarrido = int(Bporcentaje * 360)
CanguloDeBarrido = int(Cporcentaje * 360)
DanguloDeBarrido = int(Dporcentaje * 360)
EanguloDeBarrido = int(Eporcentaje * 360)
FanguloDeBarrido = int(Fporcentaje * 360)
GanguloDeBarrido = int(Gporcentaje * 360)

print (Aporcentaje)
print (Bporcentaje)
print (Cporcentaje)
print (Dporcentaje)
print (Eporcentaje)
print (Fporcentaje)
print (Gporcentaje)

print (AanguloDeBarrido)
print (BanguloDeBarrido)
print (CanguloDeBarrido)
print (DanguloDeBarrido)
print (EanguloDeBarrido)
print (FanguloDeBarrido)
print (GanguloDeBarrido)
print (AanguloDeBarrido)

Circulo(130,240,120,fill='lavanda',borde='negro')
Arc(130,240,240,240,0,AanguloDeBarrido,fill='naranja',borde='negro')
Arc(130,240,240,240,108,BanguloDeBarrido,fill='mocasín',borde='negro')
Arc(130,240,240,240,197,CanguloDeBarrido,fill='verdePálido',borde='negro')
Arc(130,240,240,240,253,DanguloDeBarrido,fill='violeta',borde='negro')
Arc(130,240,240,240,277,EanguloDeBarrido,fill='marrónRosado',borde='negro')
Arc(130,240,240,240,295,FanguloDeBarrido,fill='gris',borde='negro')
Arc(130,240,240,240,299,GanguloDeBarrido,fill='chocolate',borde='negro')

Rect(260,40,10,10,fill='naranja')
Rect(260,60,10,10,fill='mocasín')
Rect(260,80,10,10,fill='verdePálido')
Rect(260,100,10,10,fill='violeta')
Rect(260,120,10,10,fill='marrónRosado')
Rect(260,140,10,10,fill='gris')
Rect(260,160,10,10,fill='chocolate')

Rotulo('Cristianismo',310,42)
Rotulo('Hinduismo',310,62)
Rotulo('Islam',310,82)
Rotulo('Budismo',310,102)
Rotulo('ReligionesChinas',325,122)
Rotulo('Religiones',325,142)
Rotulo('Afroamericanas',325,150)
Rotulo('Ateos',305,165)

Rotulo('A',240,45,negrito=Verdadero)
Rotulo('B',240,65,negrito=Verdadero)
Rotulo('C',240,85,negrito=Verdadero)
Rotulo('D',240,105,negrito=Verdadero)
Rotulo('E',240,125,negrito=Verdadero)
Rotulo('F',240,145,negrito=Verdadero)
Rotulo('G',240,165,negrito=Verdadero)

cmu_graphics.run()