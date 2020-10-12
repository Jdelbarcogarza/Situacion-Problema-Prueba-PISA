from colorama import init, Fore, Back, Style
import random

'''
Programa que ayuda a los estudiantes a repasar los temas que se presentan en la prueba
PISA para ayudar a estudiar a niños de secundaria.


Reflexión:

Aprendí bastante en este curso sobre programación y del lenguaje python.
Estoy muy contento con mi desempeño en este curso pues, cumplí una de mis metas la cual era
fortalecer mis bases en el lenguaje de programación python. Aunque tal vez no tengo la calificación
que hubiera esperado debido a los quizzes, me voy contento con todo lo que aprendí. Sin duda me siento
listo para lo que viene que es programación orientada a objetos.

En lo personal, le dedique mucho de mi tiempo libre a este proyecto porque de verdad
me gusta programar y hacer que lo que construyo sea lo más eficiente e interactivo posible
para que el usuario no tenga problema a utilizarlo. Algunas de las cosas que aprendí por mi cuenta
fue utilizar el try except para evitar que crashee mi código si se pone un tipo de dato incorrecto
diferente al input que espera mi programa. además, por mi cuenta implementé el uso de archivos para
mostrar las frases motivacionales previo a que fuera visto en clase.

'''


# Nota importante - añadí las siguientes funciones para llamarlas desde el programa
init()

def negro():
    return Fore.BLACK

def azul():
    return Fore.BLUE

def celeste():
    return Fore.CYAN

def verde():
    return Fore.GREEN

def negro0():
    return Fore.LIGHTBLACK_EX

def azul0():
    return Fore.LIGHTBLUE_EX

def celeste0():
    return Fore.LIGHTCYAN_EX

def verde0():
    return Fore.LIGHTGREEN_EX

def magenta0():
    return Fore.LIGHTMAGENTA_EX

def rojo0():
    return Fore.LIGHTRED_EX

def blanco0():
    return Fore.LIGHTWHITE_EX

def amarillo0():
    return Fore.LIGHTYELLOW_EX

def magenta():
    return Fore.MAGENTA

def rojo():
    return Fore.RED

def reset():
    return Fore.RESET

def blanco():
    return Fore.WHITE 

def amarillo():
    return Fore.YELLOW


def kahoot(nombre):
    
    preguntas_correctas = 0
    preguntas_repasar = 0
    
    with open(nombre, encoding="utf-8") as archivo:
        #readline lee todo el archivo y lo deja en una lista de strings
        #donde cada linea del archivo es una pregunta
        lista_preg = archivo.readlines()
    
    random.shuffle(lista_preg)
    
    # En esta lista se almacenan las preguntas contesdadas incorrectamente para ser vistas
    # nuevamente en una sección de repaso
    lista_preg_repaso = []   
    
    # num_preg es el indice que indica el numero de la pregunta siendo respondida.
    # La variable "pregunta" es el string que está en ese índice.
    # 0, 1, 2, 3, 4
    for num_preg, pregunta in enumerate(lista_preg):
        
        # separar todas las partes de la pregunta, usando el separador "≤" y el
        # método split.  El split genera una lista de strings
        # La estructura de la lista generada es la siguiente [enunciado, op1, op2, op3, op4]
        lista = pregunta.split('≤')
        
        #imprimiendo primero el mensaje sin salto de línea nos permite colorear 'el mensaje del input'
        print(negro(),'Presiona <enter>',end ='')
        pausa = input()
        # utilizamos varios prints para despejarel shell y se despliege coon suficiente espacio
        # la siguiente pregunta
        print()
        print()
        print()
        # la función pop saca, borra o elimina el elemento subíndice[0] de la lista
        # para permitirnos imprimir el enunciado de la pregunta guardandolo en una variable
        enunciado_preg = lista.pop(0)
        print(negro(), f'{num_preg + 1}. {enunciado_preg}')
        
        # Crear la lista con las diferentes opciones y su respectivo valor boleano
        #que indica si es la opción correcta o incorrecta al enunciado de la pregunta
        lista_opciones = []
        for opcion in lista:
            lista_opciones.append(opcion.split('º'))
                
                
        # con la librería random y el método shuffle mezclamos el órden de las opciones
        # para que, en caso de repetir el questionario, no se representen las opciones
        # en el mismo orden.
        random.shuffle(lista_opciones)
        
        print('')
        # muestra las opciones de respuestas ya desordenadas con un inciso en cada opción
        # para facilitar la búsqueda de ese valor en la lista de opciones
        # con las respuestas correctas.
        for iK, valor in enumerate(lista_opciones):
            print(celeste(), f'{iK}. {valor[0]}')
            
        # leer la opción como entero (int) porque lo usaremos como index de la lista
        # con las respuestas
        print(magenta(),'Teclea la opcion correcta: ',end ='')
        
        #validamos el input del usuario
        respuesta = input()
        
        while(True):
            
            try:
                #si la respuesta es un número se sale del while continuamos
                respuesta = int(respuesta)
                break
            except:
                #en caso de que el usuario teclee un string se muestra el sig. mensaje
                print(reset(),"Teclea con dígitos la opción que deseas seleccionar")
                #pedimos nuevamente que teclee su respuesta
                respuesta = input()
        
        #ciclo centinela para revisar que el usuario siempre de un número del
        #0 a la longitud de la lista de las opciones -1 para evitar error en el código
                
        while(True):
        #con try y except validamos el input del usuario para asegurarnos que
        # en ningún momento haya un bug en el código si se escribe un string
        #por accidente
            try:
                respuesta = int(respuesta)
                
                if(respuesta >= 0 and respuesta <= len(lista_opciones)-1):
                    break
                else:
                    print(reset(),f"No hay un inciso con valor '{respuesta}'")
                    respuesta = input()
                    
            except:
                
                print(reset(),f"Asegurate de que tu respuesta sea un valor numérico.")
                respuesta = input("Teclea un inciso de los mostrados en las opciones: ")
            
        # analizar, revisar, comprender esta condición -, en el index 1 está la respuesta
        if lista_opciones[respuesta][1] == '1':
            print(verde(),'Respuesta correcta')
            preguntas_correctas = preguntas_correctas + 1
        else:
            print(rojo(),'Respuesta incorrecta')
            print(rojo(),'Repasa el tema!!')
            preguntas_repasar = preguntas_repasar + 1
            # agregar el num_preg a la lista de preguntas de repaso para
            # desplegarlas al usuario despúes.
            lista_preg_repaso.append(num_preg)
            
    
    # lista_preg_repaso.revere()
    
    # iniciar el repaso
    print()
    print()
    print('Repaso:')
    
    # recorrer la lista de preguntas de repaso
    for iK in lista_preg_repaso:
        pregunta = lista_preg[iK]
        
        # se separan el enunciado y las opciones en una lista con la estructura:
        # [enunciado, op1, op2, op3, op4]
        lista = pregunta.split('≤')
        
        # la función pop saca el enunciado de la pregunta, de la lista con las opciones
        enunciado_preg = lista.pop(0)
        print(rojo(), f'{iK + 1}. {enunciado_preg}')
        
        #se pasan las opciones a una lista de opciones para después comparar
        #si la respuesta seleccionada es la correcta.
        lista_opciones = []
        for index, opcion in enumerate(lista):
            lista_opciones.append(opcion.split('º'))
            
        # shuffle de la lista de opciones
        random.shuffle(lista_opciones)
        
        '''
        Aqui abrimos el archivo que contiene las preguntas motivacionales para que
        se despliegen en cada pregunta de repaso que el usuario tenga
        '''
        
        frases_motivacionales = open("Frases motivacionales Equipo 2.txt", encoding="utf-8")
        # inicializamos la lsita que contendrá nuestras frases
        lista_frases = []
        #iteramos sobre el archivo para obtener nuestras frases y
        #colocarlas en las lista de "lista_frases"
        for iK in frases_motivacionales:
            
            frase = frases_motivacionales.readline()
            #con esta línea quitamos el salto de línea que contenía cada elemento
            #de nuestra lista
            frase = frase[:-1]
            lista_frases.append(frase)
            
        #cerramos el archivo, pues ya contamos con nuestras frases almacenadas
        #en nuestra lista dentro del archivo de python
        frases_motivacionales.close()

        #mezclamos la lista de frases motivacionales para que no se repitan en el mismo orden
        #al usuario
        random.shuffle(lista_frases)
        
        print('')
        # muestra las opciones de respuestas ya desordenadas
        for iK, valor in enumerate(lista_opciones):
            print(amarillo(), f'{iK}. {valor[0]}')
        
        #iteramos sobre la lista de respuestas correctas para desplegarsela al usuario
        for index in range(len(lista_opciones)):
        #imprimir respuesta correcta checando el valor boleano (0 or 1) de la opción
            if(lista_opciones[index][1] == '1'):
                print(reset(),'La respuesta correcta es:')
                print(verde(),f'{lista_opciones[index][0]}')
                print(azul(), lista_frases[index])
        #imprimimos con el método choice una frase motivacional de nuestra lista.
                '''
                Podemos hacer que no se repitan las frases motivacionales pero me dio flo
                '''
                #print(azul(),random.choice(lista_frases))
                
        # Hacer una pausa - reflexione - sobre la respuesta - desplegar una frase motivacional o una imagen.
        print(negro(),'Presiona <enter>',end ='')
        pausa = input()
    
    
   



    #Se despliega el menú para que el usuario seleccione
    #el tema a estudiar
def menu():
    
    print(rojo(), 'Temas')
    print(rojo(), '1 - Química')
    print(rojo(), '2 - Gramática')
    print(rojo(), '3 - ')
    print(rojo(), '4 - Geografía')
    print(rojo(), '5 - Historia')
    print(rojo(), '6 - Matemáticas')
    print(rojo(), '7 - Artes')
    print(rojo(), '8 - Música')
    print(rojo(), '9 - Física')
    print(rojo(), '10 - Geometría')
    print(rojo(), '11 - Computación')
    print(rojo(), '12 - Biología')
    print(rojo(), '13 - Geografía')
    print(rojo(), '14 - Historia Universal')
    print(rojo(), '15 - Inglés')
    print(rojo(), '16 - Computación')
    print(rojo(), '17 - Ingresa el nombre del pool de preguntas')
    print(rojo(), '0 - Salir')
    return int(input('Teclea la opción:'))
    
def main():
    
    opcion = menu()
    #le pedimos al usuario un número para que elija el tema a estudiar
    while (opcion != 0):
        
        if(opcion >= 1 and opcion <= 16):
            #como tenemos archivos de texto en un formato estandar
            #solamente se concatena el número del archivo para que se pueda abrir
            #correctamente
            kahoot("Equipo" + str(opcion) + ".txt")
        elif(opcion == 18):
            kahoot(input("Teclea el nombre del archivo:"))
            
        else:
            print("Teclea una opción válida: ")
        
        #Actualizar la vcc
        opcion = menu()
        
        
        
        pausa = input("<enter>")
        
main()

