from cmu_graphics import *

def onMouseMove(x, y):
    

    app.fondo = 'negro'

Rótulo('*No a escala', 340, 370, relleno='blanco', tamaño=16)

sol = Estrella(200, 200, 35, 400, relleno=gradiente('naranja', 'amarillo', 'rojoNaranja'))

venus = Grupo(
     Círculo(200,200,100,relleno=None,borde='grisOscuro'),
     Círculo(200,100,10,relleno=gradiente('verde','azulReal',inicio='izquierda-superior'))   
)

marte = Grupo(
    Círculo(200,200,200,relleno=None,borde='grisOscuro'),
    Círculo(200,10,20,relleno=gradiente('rojo','naranja',inicio='izquierda-superior'))
)
tierra = Grupo(
    Círculo(200, 200, 150, relleno=None, borde='grisOscuro'),
    Círculo(200, 50, 10, relleno=gradiente('verde', 'azulReal', inicio='izquierda-superior'))
    ) 
tierra.dirección = 'sentido-horario'

cometa = Group(
    Circle(10,10,10,relleno=gradient('gris','pink')),
    Estrella(10,10,13,5,relleno='cian'),
    Polygon(0,0,9,9,9,11,relleno=gradient('azul','cian','blanco'))
    )

cometa.dx=10
cometa. dy=5

estrella = Estrella(320,40,5,5,filll= 'amarillo')
Aestrella = Estrella(200,40,5,5,fill= 'amarillo')
Bestrella = Estrella(320,160,5,5,fill= 'amarillo')
fugaz = Línea(320,40,350,20,fill='blanco')
fugazA = Línea(200,40,230,20,fill='blanco')
fugazB = Línea(320,160,350,20,fill='blanco')

Aestrella.dx=-10
Bestrella.dx=-10
estrella.dx=-10
estrella.dy=+10
Aestrella.dy=+10
Bestrella.dy=+10
fugaz.dx=-10
fugazA.dx=-10
fugazB.dx=-10
fugaz.dy=+10
fugazA.dy=+10
fugazB.dy=+10


def enTeclaPresionada(tecla):
    # Cambie la dirección basado en la tecla.
    if (tecla == 'derecha'):
        tierra.dirección = 'sentido-horario'
        marte.dirección = 'sentido-horario'
        venus.dirección = 'sentido-horario'
    elif (tecla == 'izquierda'):
        tierra.dirección = 'sentido-antihorario'
        marte.dirección = 'sentido-antihorario'
        venus.dirección = 'sentido-antihorario'

def enPaso():
    # Si la dirección de la tierra es en sentido horario, agregue 3 al rotarÁngulo.
    # Si no, reste 3.
    if (tierra.dirección == 'sentido-horario'):
        tierra.rotarÁngulo += 3
        marte.rotarÁngulo += 5
        venus.rotarÁngulo += 4
    else:
        tierra.rotarÁngulo -= 3
        marte.rotarÁngulo -= 5
        venus.rotarÁngulo -= 4

    cometa.centroX +=3 
    cometa.centroY +=3 
    # Incremente el número de puntos del sol por 1.
    sol.puntos += 1
   
cmu_graphics.run()