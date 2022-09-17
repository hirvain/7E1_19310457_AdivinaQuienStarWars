#Sistemas Expertos Parcial 1
#Oscar Antonio García Avila 19310457  7E1
#STAR WARS ADIVINA QUIEN

#Declaramos la base de datos de nuestro arbol inicial
database = [
    ['Qui Gon Jin','ssss'],
    ['Mace Windu','sssnss'],
    ['Anakin','sssnsn'],
    ['Yoda','sssnn'],
    ['Luke Skywalker','ssns'],
    ['Kit Fisto','ssnn'],
    ['Darth Sidious','snsss'],
    ['General Grievous','snssns'],
    ['Darth Vader','snssnns'],
    ['Conde Dooku','snssnnn'],
    ['Darth Maul','snsn'],
    ['Leia Organa','snn'],
    ['Han Solo','nss'],
    ['Boba Fett','nsns'],
    ['Lando Calrissian','nsnn'],
    ['C-3PO','nnss'],
    ['R2-D2','nnsn'],
    ['Chewbacca','nnns'],
    ['Jabba the Hutt','nnnn'],
]

#Leemos el archivo de la base de datos de nuestros personajes agregados por el ususario
conti = 'y'
while(conti!='n'):
  archivo = open(r'extras.txt', 'r+')
  extras = []
  cont=0
  cont2=0
  filas = []
  for line in archivo.readlines():
    if(cont==0):
      filas.append(line.replace("\n",""))
      cont = 1
    else:
      filas.append(line.replace("\n",""))
      extras.append(filas)
      cont = 0
      filas = []

  class nodo(object):
    def __init__(self):
      self.der = None
      self.izq  = None
      self.dato  = None

  #Funciones para encontrar al personaje dentro de nuestra base de datos

  def match_db(answers):
    for i in range(len(database)):
      if(answers==database[i][1]):
        return database[i][0]

  def match_extras(answers):
    for i in range(len(extras)):
      if(answers==extras[i][1]):
        return extras[i][0]
    return None

  #Creamos nuestro árbol binario con las preguntas que planteamos###############
  raiz = nodo()
  raiz.dato = 'Tu personaje es sintiente a la fuerza?'
  raiz.izq = nodo()
  raiz.izq.dato = 'Tu personaje es un jedi?'
  raiz.izq.izq = nodo()
  raiz.izq.izq.dato = 'Tu personaje aparece en el episodio 1?'
  raiz.izq.izq.izq = nodo()
  raiz.izq.izq.izq.dato = 'Tu personaje tiene cabello largo?'
  raiz.izq.izq.izq.izq = nodo()
  raiz.izq.izq.izq.der = nodo()
  raiz.izq.izq.izq.der.dato= 'Tu personaje es humano?'
  raiz.izq.izq.izq.der.izq = nodo()
  raiz.izq.izq.izq.der.izq.dato= 'Tu personaje tiene un lightsaber morado?'
  raiz.izq.izq.izq.der.der = nodo()
  raiz.izq.izq.izq.der.izq.izq = nodo()
  raiz.izq.izq.izq.der.izq.der = nodo()
  raiz.izq.izq.der = nodo()
  raiz.izq.izq.der.dato = 'Tu personaje es hijo de Anakin Skywalker?'
  raiz.izq.izq.der.izq = nodo()
  raiz.izq.izq.der.der = nodo()
  raiz.izq.der = nodo()
  raiz.izq.der.dato = 'Tu personaje es un SITH?'
  raiz.izq.der.der = nodo()
  raiz.izq.der.izq = nodo()
  raiz.izq.der.izq.dato = 'Tu personaje aparece en el episodio 3?'
  raiz.izq.der.izq.der = nodo()
  raiz.izq.der.izq.izq = nodo()
  raiz.izq.der.izq.izq.dato = 'Tu personaje es parte del senado?'
  raiz.izq.der.izq.izq.izq = nodo()
  raiz.izq.der.izq.izq.der = nodo()
  raiz.izq.der.izq.izq.der.dato = 'Tu personaje usa 4 sables de luz?'
  raiz.izq.der.izq.izq.der.izq = nodo()
  raiz.izq.der.izq.izq.der.der = nodo()
  raiz.izq.der.izq.izq.der.der.dato = 'Tu personaje aparece en el episodio 4?'
  raiz.izq.der.izq.izq.der.der.izq = nodo()
  raiz.izq.der.izq.izq.der.der.der = nodo()
  raiz.der = nodo()
  raiz.der.dato = 'Tu personaje es un contrabandista?'
  raiz.der.izq = nodo()
  raiz.der.izq.dato = 'Tu personaje pilota el Halcon Milenario?'
  raiz.der.izq.izq = nodo()
  raiz.der.izq.der = nodo()
  raiz.der.izq.der.dato = 'Tu personaje usa casco?'
  raiz.der.izq.der.izq = nodo()
  raiz.der.izq.der.der = nodo()

  raiz.der.der = nodo()
  raiz.der.der.dato = 'Tu personaje es un androide?'
  raiz.der.der.izq = nodo()
  raiz.der.der.izq.dato = 'Tu personaje domina seis millones de formas de comunicacion?'
  raiz.der.der.izq.izq = nodo()
  raiz.der.der.izq.der = nodo()
  raiz.der.der.der = nodo()
  raiz.der.der.der.dato = 'Tu personaje es un Wokke?'
  raiz.der.der.der.izq = nodo()
  raiz.der.der.der.der = nodo()

  #############################################################################

  print("STAR WARS Adivina Quien")

  resuls = ''
  actual = raiz
  while actual.izq != None :
    ans = input(actual.dato + "(s,n)")
    resuls+=ans
    if(ans == 's'):
      actual = actual.izq
    elif(ans == 'n'):
      actual = actual.der

  ans = input("Tu personaje es " + match_db(resuls) + "?(s,n)")

  if(ans == 's'):
    print("Personaje adivinado")
  elif(ans == 'n'):
    while ans == 'n':
      resuls+=ans
      if(match_extras(resuls)==None):
        nuevo = input("Cuál era tu personaje?")
        archivo.write(nuevo + "\n" + resuls +"\n")
        ans = 's'
      else:
        ans = input("Tu personaje es " + match_extras(resuls) + "?(s,n)")
  archivo.close()
  conti = input("Volver a jugar?(s,n)")
print("Gracias por jugar")


