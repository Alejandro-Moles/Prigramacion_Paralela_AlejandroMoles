from time import sleep
from random import randint
from multiprocessing import Process
import sys
from io import open
from time import time

class Proceso(Process):

    def __init__(self, Archivo, letra):
        Process.__init__(self)
        self.Archivo = Archivo #le paso de parametro el nombre del archivo
        self.letra = letra #le paso de parametro la vocal que quiero que lea

    def run(self):
        #hace un print con los datos
        print("El numero de las vocales de " +self.letra + " que tiene el texto es de " +str(self.contarVocal()))

    def contarVocal (self):
        contador = 0
        #hago que se abra el fichero para leerlo
        archivo_texto = open(self.Archivo, "r")
        #mientras sea verdadero ejecuto el bucle,hasta que salte la condicion y me lo cierre con el break
        while True:
            #meto en una variable la vocal que se lee
            comprobar = archivo_texto.read(1)
            if not comprobar:
                break
            #si la letra esla que buesco me lo suma en un contador
            if(self.letra == comprobar):
                contador = contador + 1

        archivo_texto.close()
        return contador


if __name__ == '__main__':
    #compruebo el numero de parametros
    if len(sys.argv) >= 2:
        #le paso el  nombre del fichero
        Archivo = sys.argv[1]

        #creo el proceso y lo inicio
        proceso = Proceso(Archivo, "a")
        proceso.start()

        #inicio el temporiador
        tiempoini = time()

        # creo el proceso y lo inicio
        proceso2 = Proceso(Archivo, "e")
        proceso2.start()

        # creo el proceso y lo inicio
        proceso3 = Proceso(Archivo, "i")
        proceso3.start()

        # creo el proceso y lo inicio
        proceso4 = Proceso(Archivo, "o")
        proceso4.start()

        # creo el proceso y lo inicio
        proceso5 = Proceso(Archivo, "u")
        proceso5.start()

        #finalizo los procesos
        proceso.join()
        proceso2.join()
        proceso3.join()
        proceso4.join()
        proceso5.join()

        # finalizo el temporiador
        tiempofin = time()
        #saco el tiempo que ha tardado en ejecutarse
        tiempofinal = tiempofin - tiempoini

        print("El programa ha tardado " + str(tiempofinal) + " en encontrar todas las vocales")

