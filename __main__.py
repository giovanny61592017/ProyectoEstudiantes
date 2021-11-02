from src.modelo.Asignatura import Asignatura
from src.modelo.Profesor import Profesor
from src.modelo.Estudiante import Estudiante, Escala
from src.modelo.declarative_base import Session, engine, Base
from src.logica.coleccion import Coleccion


def anadir_album (nombre , ciclo , apellido , escala) :
   # Crea la BD
   Base.metadata.create_all ( engine )

   # Abre la sesion
   session = Session ( )
   coleccion = Coleccion ( )

   if coleccion.agregar_album ( nombre , ciclo , apellido , escala ) :
      print ( f"Se añadio nombre: {nombre}" )
   else :
      print ( f"El Nombre: {nombre}, ya existe" )
   session.close()

def editar_album (estudiante_id,nombre , ciclo , apellido , escala) :
   # Crea la BD
   Base.metadata.create_all ( engine )

   # Abre la sesion
   session = Session ( )
   coleccion = Coleccion ( )

   if coleccion.editar_album ( estudiante_id , nombre , ciclo , apellido , escala ) :
      print ( f"Se modifico el estudiante por el id: {estudiante_id}" )
   else :
      print ( f"El nuevo nombre '{nombre}' para el estudiante con id: {estudiante_id}, ya existe" )
   session.close()



def mostrar_album (estudiante_id) :
   # Crea la BD
   Base.metadata.create_all ( engine )

   # Abre la sesion
   session = Session ( )
   coleccion = Coleccion ( )

   student=coleccion.dar_album_por_id(estudiante_id)
   # print(student)
   print ( f"=======================================" )
   print ( f"Id Estudiante:   {student[ 'id' ]}" )
   print ( f"Nombre:          {student[ 'nombre' ]}" )
   print ( f"Ciclo:           {student[ 'ciclo' ]}" )
   print ( f"Apellidos:       {student[ 'apellido' ]}" )
   print ( f"Tercio Superior: {student[ 'escala' ]}" )
   print ( f"=======================================" )
   session.close()

def Anadir_registros():
   # Crea la BD
   Base.metadata.create_all ( engine )

   # Abre la sesion
   session = Session ( )

   # crear Profesores
   profesor1 = Profesor ( nombre = "Manuel Loza" , descripcion = "Profesor de Fisica" )
   profesor2 = Profesor ( nombre = "Emilio Jaime" , descripcion = "Profesor de Aritmetica" )
   profesor3 = Profesor ( nombre = "Caceres Rivera", descripcion= "Profesor de Ciencias Culturale")
   profesor4 = Profesor ( nombre = "Fresia Melinda" , descripcion = "Profesor de Ciencias Sociales" )
   session.add ( profesor1 )
   session.add ( profesor2 )
   session.add ( profesor3 )
   session.add ( profesor4 )
   session.commit ( )

   # Crear Estudiantes
   estudiante1 = Estudiante ( nombre = "Giovanny" , ciclo = 7 , apellido = "Camposano Iriarte" , escala = Escala.Escala1 )
   estudiante2 = Estudiante ( nombre = "Jheycit" , ciclo = 7 , apellido = "Cangalaya Antezano" , escala = Escala.Escala1 )
   session.add ( estudiante1 )
   session.add ( estudiante2 )

   # Crear Asignaturas
   asignatura1 = Asignatura ( asignatura = "Fisica" , hora = 1 , minuto = 30 , descripcion = "Clases de teoria y laboratorio" )
   asignatura2 = Asignatura ( asignatura = "Aritmetica " , hora = 3 , minuto = 00 , descripcion = "Clases practicas " )
   asignatura3 = Asignatura ( asignatura = "Ciencias" , hora = 4 , minuto = 30 , descripcion = "Clases de teoria y laboratorio" )
   session.add ( asignatura1 )
   session.add ( asignatura2 )
   session.add ( asignatura3 )

   # Relacionar Estudiante con asignatura
   estudiante1.Asignatura = [ asignatura1 , asignatura2 ]
   estudiante2.Asignatura = [ asignatura1 , asignatura3 ]

   # Relacionar Asignatura con profesores
   asignatura1.profesores = [ profesor1 ]
   asignatura2.profesores = [ profesor2 ]
   asignatura3.profesores = [ profesor3 , profesor4 ]
   session.commit ( )

   session.commit ( )
   session.close ( )

if __name__ == '__main__':
   Anadir_registros ( )

   anadir_album ( "Keysi" , 7 , "Simbron Guerra" , Escala.Escala1 )
   anadir_album ( "Jean" , 7 , "Torres Ricse" , Escala.Escala1 )
   anadir_album ( "Liz" , 7 , "Rock alternativo" , Escala.Escala1 )
   anadir_album ( "Miguelito" , 2 , "Poma Amop" , Escala.Escala1 )

   editar_album (2, "Jhon",7, "Camposano Iriarte",Escala.Escala1)
   editar_album ( 1 , "Pilar",7 , "Cangalaya Antezana" , Escala.Escala1)

   for i in [ 1 , 2 , 3, 4, 5] :
      mostrar_album ( i )

   i = 1
   while i <= 4:
      mostrar_album(i)
      i=i+1

