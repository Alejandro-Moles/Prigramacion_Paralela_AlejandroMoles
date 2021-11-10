
from multiprocessing import Process
import sys
from io import open
from time import time

class Proceso(Process):

    def __init__(self, Archivo, letra):
        Process.__init__(self)
        self.Archivo = Archivo#le paso de parametro el nombre del archivo
        self.letra = letra #le paso de parametro la vocal que quiero que lea

    def run(self):
        # hace un print con los datos
        print("El numero de las vocales de " +self.letra + " que tiene el texto es de " +str(self.contarVocal()))

    def contarVocal (self):
        contador = 0
        #hago que se abra el fichero para leerlo
        archivo_texto = open(self.Archivo, "r")
        # mientras sea verdadero ejecuto el bucle,hasta que salte la condicion y me lo cierre con el break
        while True:
            # meto en una variable la vocal que se lee
            comprobar = archivo_texto.read(1)
            # si la letra esla que buesco me lo suma en un contador
            if not comprobar:
                break
            if(self.letra == comprobar):
                contador = contador + 1

        archivo_texto.close()
        return contador


if __name__ == '__main__':

    if len(sys.argv) >= 2:
        # le paso el  nombre del fichero
        Archivo = sys.argv[1]

        # creo el proceso y lo inicio y lo termino
        proceso = Proceso(Archivo, "a")
        proceso.start()
        # inicio el temporiador
        tiempoini = time()
        proceso.join()

        # creo el proceso y lo inicio y lo termino
        proceso = Proceso(Archivo, "e")
        proceso.start()
        proceso.join()

        # creo el proceso y lo inicio y lo termino
        proceso = Proceso(Archivo, "i")
        proceso.start()
        proceso.join()

        # creo el proceso y lo inicio y lo termino
        proceso = Proceso(Archivo, "o")
        proceso.start()
        proceso.join()

        # creo el proceso y lo inicio y lo termino
        proceso = Proceso(Archivo, "u")
        proceso.start()
        proceso.join()

        tiempofin = time()

        tiempofinal = tiempofin - tiempoini

        print("El programa ha tardado " +str(tiempofinal) +" en encontrar todas las vocales")
