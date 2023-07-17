# -*- coding: utf-8 -*-
"""¡MOVIE MENTOR: RECOMENDADOR DE PELÍCULAS!.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1ZJWm-HVowG5pKXcn_PW6uEU_nlz3EK8M

## ¡MOVIE MENTOR: RECOMENDADOR DE PELÍCULAS!

**Autómatas y Lenguajes Formales**

**Estudiantes: Cristian Solano_2211906, Anderson Lemus_Código, Santiago Ortega_Código**

**Profesor: Luis Carlos Guayacán**

**Escuela de Ingeniería de Sistemas e Informática**

_Julio de 2023_

<div style="height:100px;"></div>

<span style="font-size:20px;font-weight:bold;"><span style="background-color:#F00;color:#FFF;padding:10px;">Obligatorio</span> Ejecute estas celdas para iniciar el Proyecto:</span>
"""

!pip install automata-lib

"""<div style="height:100px;"></div>

1.   Se ejecutará la celda del autómata, la cual consiste en un autómata finito determinista que irá realizando una serie de preguntas, y según la respuesta del usuario, el autómata irá por uno de los posibles caminos y llegará a una película que probablemente le gustará:
"""

def Automata_Pelicula():
  from automata.fa.dfa import DFA #Librería para diseñar Autómatas Finitos Deterministas


  AutoPeli = DFA(
      states = {'q0', 'q1', 'q2', 'q3', 'q4', 'q5', 'q6', 'q7', 'q8', 'q9', 'q10', 'q11', 'q12', 'q13', 'q14', 'q15', 'q16', 'q17', 'q18', 'q19', 'q20', 'q21', 'q22', 'q23', 'q24', 'q25', 'q26',
                'q27', 'q28', 'q29', 'q30', 'q31', 'q32', 'q33', 'q34', 'q35', 'q36', 'q37', 'q38', 'q39', 'q40', 'q41', 'q42', 'q43', 'q44', 'q45', 'q46', 'q47', 'q48', 'q49', 'q50', 'q51', 'q52', 'q53', 'q54', 'q55',
                'qR1', 'qR2', 'qR3', 'qR4', 'qR5', 'qR6', 'qR7', 'qR8', 'qR9', 'qR10', 'qR11', 'qR12', 'qR13', 'qR14', 'qR15', 'qR16', 'qR17', 'qR18', 'qR19', 'qR20',
                'qR21', 'qR22', 'qR23', 'qR24', 'qR25', 'qR26', 'qR27', 'qR28', 'qR29', 'qR30', 'qR31', 'qR32', 'qR33', 'qR34', 'qR35', 'qR36', 'qR37', 'qR38', 'qR39', 'qR40',
                'qR41', 'qR42', 'qR43', 'qR44', 'qR45', 'qR46', 'qR47', 'qR48', 'qR49', 'qR50', 'qR51', 'qR52', 'qR53', 'qR54', 'qR55', 'qR56', 'qR57', 'qR58', 'qR59', 'qR60'}, #Estados del Automata
      input_symbols= {'f', 'v', 'an', 'c', 'ac', 't', 'r'}, #Lenguaje aceptado por el Automata
      transitions=
        {
            'q0':{'an': 'q1', 'c': 'q11', 'ac': 'q21', 't': 'q36', 'r': 'q46'},
            'q1':{'v': 'q2' , 'f': 'q3'},
            'q2':{'v': 'qR1' , 'f': 'qR2'},
            'q3':{'v': 'q4' , 'f': 'q5'},
            'q4':{'v': 'qR3' , 'f': 'qR4'},
            'q5':{'v': 'q6' , 'f': 'q7'},
            'q6':{'v': 'qR5' , 'f': 'qR6'},
            'q7':{'v': 'q8' , 'f': 'q9'},
            'q8':{'v': 'qR7' , 'f': 'qR8'},
            'q9':{'v': 'q10' , 'f': 'qR11'},
            'q10':{'v': 'qR9' , 'f': 'qR10'},
            'q11':{'v': 'q12' , 'f': 'q13'},
            'q12':{'v': 'qR12' , 'f': 'qR13'},
            'q13':{'v': 'q14' , 'f': 'q15'},
            'q14':{'v': 'qR14' , 'f': 'qR15'},
            'q15':{'v': 'q16' , 'f': 'q17'},
            'q16':{'v': 'qR16' , 'f': 'qR17'},
            'q17':{'v': 'q18' , 'f': 'q19'},
            'q18':{'v': 'qR18' , 'f': 'qR19'},
            'q19':{'v': 'q20' , 'f': 'qR22'},
            'q20':{'v': 'qR20' , 'f': 'qR21'},
            'q21':{'v': 'q22' , 'f': 'q29'},
            'q22':{'v': 'q23' , 'f': 'q28'},
            'q23':{'v': 'q24' , 'f': 'q27'},
            'q24':{'v': 'q25' , 'f': 'q26'},
            'q25':{'v': 'qR23' , 'f': 'qR24'},
            'q26':{'v': 'qR25' , 'f': 'qR26'},
            'q27':{'v': 'qR27' , 'f': 'qR28'},
            'q28':{'v': 'qR29' , 'f': 'qR30'},
            'q29':{'v': 'q30' , 'f': 'q31'},
            'q30':{'v': 'qR31' , 'f': 'qR32'},
            'q31':{'v': 'q32' , 'f': 'q33'},
            'q32':{'v': 'qR33' , 'f': 'qR34'},
            'q33':{'v': 'q34' , 'f': 'q35'},
            'q34':{'v': 'qR35' , 'f': 'qR36'},
            'q35':{'v': 'qR37' , 'f': 'qR38'},
            'q36':{'v': 'q37' , 'f': 'q38'},
            'q37':{'v': 'qR39' , 'f': 'qR40'},
            'q38':{'v': 'q39' , 'f': 'q40'},
            'q39':{'v': 'qR41' , 'f': 'qR42'},
            'q40':{'v': 'q41' , 'f': 'q42'},
            'q41':{'v': 'qR43' , 'f': 'qR44'},
            'q42':{'v': 'q43' , 'f': 'q44'},
            'q43':{'v': 'qR45' , 'f': 'qR46'},
            'q44':{'v': 'q45' , 'f': 'qR49'},
            'q45':{'v': 'qR47' , 'f': 'qR48'},
            'q46':{'v': 'q47' , 'f': 'q48'},
            'q47':{'v': 'qR50' , 'f': 'qR51'},
            'q48':{'v': 'q49' , 'f': 'q50'},
            'q49':{'v': 'qR52' , 'f': 'qR53'},
            'q50':{'v': 'q51' , 'f': 'q52'},
            'q51':{'v': 'qR54' , 'f': 'qR55'},
            'q52':{'v': 'q53' , 'f': 'q54'},
            'q53':{'v': 'qR56' , 'f': 'qR57'},
            'q54':{'v': 'q55' , 'f': 'qR60'},
            'q55':{'v': 'qR58' , 'f': 'qR59'}
        }, #Transiciones del Autómata

        initial_state = 'q0', #Estado Inicial
        final_states= {'qR1', 'qR2', 'qR3', 'qR4', 'qR5', 'qR6', 'qR7', 'qR8', 'qR9', 'qR10', 'qR11', 'qR12', 'qR13', 'qR14', 'qR15', 'qR16', 'qR17', 'qR18', 'qR19', 'qR20',
                       'qR21', 'qR22', 'qR23', 'qR24', 'qR25', 'qR26', 'qR27', 'qR28', 'qR29', 'qR30', 'qR31', 'qR32', 'qR33', 'qR34', 'qR35', 'qR36', 'qR37', 'qR38', 'qR39', 'qR40',
                       'qR41', 'qR42', 'qR43', 'qR44', 'qR45', 'qR46', 'qR47', 'qR48', 'qR49', 'qR50', 'qR51', 'qR52', 'qR53', 'qR54', 'qR55', 'qR56', 'qR57', 'qR58', 'qR59', 'qR60'}, #Estados de aceptación
        allow_partial = True
    )
  return AutoPeli #Devuelve el Autómata

"""<div style="height:100px;"></div>

2.   Se ejecutará la celda de las preguntas y las respuestas, es una función que va realizando las preguntas  a medida que va avanzando el autómata, hasta que encuentra una película que se adapte a la estructura de las respuestas del usuario:
"""

def Pregunta_Respuesta(estado, pregunta):

    if(estado=='q0'):
        print("Escoge la categoría de película que deseas ver:  ")

#Preguntas Animación.
    if(estado=='q1'):
       print("¿Deseas que la película tenga a alguna princesa como protagonista?")
    if(estado=='q2'):
       print("¿Te gustaría que sea una película de las princesas clásicas?")
    if(estado=='q3'):
        print("¿Deseas que la película sea de superheroes?")
    if(estado=='q4'):
        print("¿Te gustaría que la película tenga animación 2D?")
    if(estado=='q5'):
        print("¿Deseas que la película se vea ambientada en un mundo con todas las especies del mundo a excepción de los humanos?")
    if(estado=='q6'):
        print("Te gustaría que la película sea también un musical?")
    if(estado=='q7'):
        print("¿Deseas que la película sea exclusiva para los niños?")
    if(estado=='q8'):
        print("¿Te gustaría que la película tenga la temática de los juguetes con vida propia?")
    if(estado=='q9'):
        print("¿Deseas ver un clásico de las películas animadas?")
    if(estado=='q10'):
        print("¿Te gustaría que la película gire en torno a la exploración de una ciudad perdida?")

#Preguntas Comedia.
    if(estado=='q11'):
       print("¿Quieres que la película sea estrictamente para adultos?")
    if(estado=='q12'):
       print("¿Quieres que la película se vea desenvuelta por la despedida de soltero de uno de los personajes?")
    if(estado=='q13'):
        print("¿Deseas que la película tenga tintes absurdistas y sea una obra un tanto original?")
    if(estado=='q14'):
        print("¿Quieres que la película tenga humor negro?")
    if(estado=='q15'):
        print("¿Prefieres que la película tenga el estilo clásico del cine mudo?")
    if(estado=='q16'):
        print("¿Te gustaría que la película humorice temas relevantes?")
    if(estado=='q17'):
        print("Deserías que la película presente un contenido grotesco poco convencional")
    if(estado=='q18'):
        print("Quieres que la película presente humor mediante imágenes?")
    if(estado=='q19'):
        print("¿Te gustaría que la película sea parodia de otras películas?")
    if(estado=='q20'):
        print("¿Te gustaría que la película esté basada en películas de terror?")

#Preguntas Accion.
    if(estado=='q21'):
        print("¿Deseas que la película contenga acción constante y suspenso espontáneo?")
    if(estado=='q22'):
        print("¿Te gustaría que en la película, el protagonista deba infiltrarse para cumplir sus objetivos?")
    if(estado=='q23'):
        print("'¿Deseas que la película implemente la inclusión del código estricto para los asesinos (Basada en asesinos a sueldo)?")
    if(estado=='q24'):
        print("¿Te gustaría que el personaje se vea impulsado a cumplir sus metas por medio de la venganza?")
    if(estado=='q25'):
        print("¿Deseas que el personaje principal sea interpretado por Keanu Reeves?")
    if(estado=='q26'):
        print("¿Deseas que el personaje principal sea interpretado por Jean_Claude Van Damme?")
    if(estado=='q27'):
        print("¿Te gustaría que el personaje principal deba ser el conductor de algún personaje importante para la película?")
    if(estado=='q28'):
        print("¿Te parece interesante las películas donde el personaje es manipulado para cometer actos en contra de su voluntad?")
    if(estado=='q29'):
        print("¿Deseas que la película involucre catástrofes o eventos apocalípticos?")
    if(estado=='q30'):
        print("¿Te gustaría que la película involucre a la naturaleza como influencia para los eventos principales?")
    if(estado=='q31'):
        print("¿Deseas que la película  tenga como temática principal la aventura y los viajes a lugares desconocidos?")
    if(estado=='q32'):
        print("¿Te gustaría que la película involucre a los dinosaurios como personajes influyentes?")
    if(estado=='q33'):
        print("¿Deseas que la película  tenga como temática principal la guerra o los conflictos belícos/mílitares?")
    if(estado=='q34'):
        print("¿Te gustaría que la película esté basado en la Segunda Guerra Mundial?")
    if(estado=='q35'):
        print("¿Deseas que la película esté basada en temas de ciencia ficción o futuristas?")

#Preguntas Terror.
    if(estado=='q36'):
       print("¿Quieres que la película sea relacionada con algún animal asesino?")
    if(estado=='q37'):
       print("¿Te gustaría que la película esté ambientada en el oceano?")
    if(estado=='q38'):
        print("¿Quieres que la película esté relacionada con un asesino con poderes extraordinarios cuyas víctimas son  mayoritariamente jóvenes")
    if(estado=='q39'):
        print("¿Te gustaría que la película aborde el tema de un asesino con la capacidad de entrar en sueños?")
    if(estado=='q40'):
        print("¿Deseas que la película esté relacionada con espíritus de  ultratumba con la capacidad de interactuar con el mundo tangible que los rodea?")
    if(estado=='q41'):
        print("Desearías que en la película, el espírito atormente a la gente mediante un muñeco?")
    if(estado=='q42'):
        print("¿Te satisfacería ver un película de terror clásica? ")
    if(estado=='q43'):
        print("¿Te gustaría que en la película gire en torno a un psicópata con motosierra que busca asesinar personas?")
    if(estado=='q44'):
        print("¿Te gustaría que la película esté basada en algún libro?")
    if(estado=='q45'):
        print("¿Te interesan las películas de payasos asesinos? ")

#Preguntas-Romance.
    if(estado=='q46'):
        print("¿Te gustaría que la película sea un musical?")
    if(estado=='q47'):
        print("¿Te gustaría que la pareja de la película se vea envuelta en un dilema en la que decidan si vence su ambición de triunfo o el amor?")
    if(estado=='q48'):
        print("¿Te gustaría que la película esté basada en hechos reales?")
    if(estado=='q49'):
        print("¿Te gustaría que la película presente un romance que sobrepasa las clases sociales?")
    if(estado=='q50'):
        print("¿Deseas que la película este dirigida a un público más juvenil con un contenido cliché?")
    if(estado=='q51'):
        print("¿Te interesa que exista contraste de personalidades en la pareja que protagoniza la película?")
    if(estado=='q52'):
        print("¿Quieres que la película este ambientada en escenarios bélicos?")
    if(estado=='q53'):
        print("¿Quieres que la película este ambientada en la guerra civil estadounidense?")
    if(estado=='q54'):
        print("¿Quieres que la película tenga un ambiente de fantasía?")
    if(estado=='q55'):
        print("¿Deseas  la existencia de vampiros y lobos en la película?")


  #Respuestas Animación
    if(estado=='qR1'):
        print("Blancanieves")
    if(estado=='qR2'):
        print("La princesa y el sapo")
    if(estado=='qR3'):
        print("Spider_Man: Miles Morales (La saga)")
    if(estado=='qR4'):
        print("Grandes Heroes")
    if(estado=='qR5'):
        print("Sing")
    if(estado=='qR6'):
        print("La vida secreta de tus mascotas")
    if(estado=='qR7'):
        print("Toy Story (La saga)")
    if(estado=='qR8'):
        print("Wall-e")
    if(estado=='qR9'):
        print("Atlantis, El imperio perdido")
    if(estado=='qR10'):
        print("Peter Pan (1953)")
    if(estado=='qR11'):
        print("Shrek (La saga)")

  #Respuestas Comedia
    if(estado=='qR12'):
        print("Qué paso ayer (La saga)")
    if(estado=='qR13'):
        print("American Pie (La saga)")
    if(estado=='qR14'):
        print("A serious man")
    if(estado=='qR15'):
        print("Nacho Libre")
    if(estado=='qR16'):
        print("The kid (Charlie Chapling)")
    if(estado=='qR17'):
        print("Mr Bean (1997)")
    if(estado=='qR18'):
        print("The Naked Gun: Frome the Files of Police Squad")
    if(estado=='qR19'):
        print("The greasy stangler")
    if(estado=='qR20'):
        print("Scarie Movie")
    if(estado=='qR21'):
        print("Jhonny English Recargado")
    if(estado=='qR22'):
        print("La sociedad de los poetas muertos")

 #Respuestas Accion
    if(estado=='qR23'):
        print("Jhon Wick (La saga)")
    if(estado=='qR24'):
        print("Kate")
    if(estado=='qR25'):
        print("El ultimo mercenario")
    if(estado=='qR26'):
        print("El especialista")
    if(estado=='qR27'):
        print("Drive")
    if(estado=='qR28'):
        print("Vivir y morir en los Angeles")
    if(estado=='qR29'):
        print("Hitman: Agente 47")
    if(estado=='qR30'):
        print("Los infiltrados")
    if(estado=='qR31'):
        print("2012")
    if(estado=='qR32'):
        print("El planeta de los simios")
    if(estado=='qR33'):
        print("Jurassic Park (La saga)")
    if(estado=='qR34'):
        print("Piratas del Caribe (La saga)")
    if(estado=='qR35'):
        print("Salvar al soldado Ryan")
    if(estado=='qR36'):
        print("Lincoln")
    if(estado=='qR37'):
        print("Terminator (La saga)")
    if(estado=='qR38'):
        print("Batman: The Dark Knight (La saga)")

  #Respuestas Terror
    if(estado=='qR39'):
        print("Tiburón")
    if(estado=='qR40'):
        print("Anaconda")
    if(estado=='qR41'):
        print("Pesadilla en la calle Elm")
    if(estado=='qR42'):
        print("Viernes 13")
    if(estado=='qR43'):
        print("Annabelle (La saga)")
    if(estado=='qR44'):
        print("El conjuro (La saga)")
    if(estado=='qR45'):
        print("La Matanza de Texas")
    if(estado=='qR46'):
        print("Halloween")
    if(estado=='qR47'):
        print("It (La saga)")
    if(estado=='qR48'):
        print("El silencio de los inocentes")
    if(estado=='qR49'):
        print("Psycho")

  #Respuestas Romance
    if(estado=='qR50'):
        print("LA LA LAND")
    if(estado=='qR51'):
        print("Somos tus amigos")
    if(estado=='qR52'):
        print("Titanic")
    if(estado=='qR53'):
        print("La teoría de todo")
    if(estado=='qR54'):
        print("3 metros sobre el cielo")
    if(estado=='qR55'):
        print("Violet y Finch")
    if(estado=='qR56'):
        print("Lo que el viento se llevó")
    if(estado=='qR57'):
        print("Casablanca")
    if(estado=='qR58'):
        print("Crepúsculo")
    if(estado=='qR59'):
        print("En algún lugar del tiempo")
    if(estado=='qR60'):
        print("Eternal Sunshine of the Spotless Mind")

"""<div style="height:100px;"></div>

3.   Se ejecutará la celda del Compilador, es en resúmen el Main del proyecto:
"""

def compilador():
    from IPython.display import clear_output # Librería para limpiar la salida de la celda
    import time # Librería requerida para utilizar la función "time.sleep()"
    AutoPeli = Automata_Pelicula() # Llamado a la función del autómata para obtener el autómata de recomendación de películas

    print("¡Bienvenido a MovieMentor!") # Mensaje de bienvenida
    print("================================")
    print("Se realizarán una serie de preguntas para ayudarte a encontrar la película perfecta.")
    print("Por favor, responde las preguntas con 'sí' o 'no'. En la primera pregunta utiliza 'an' si quieres animación, 'c' si quieres comedia, 'ac' si quieres acción, 't' si quieres terror o 'r' si quieres romance. ¡Comencemos!")
    print("================================")

    time.sleep(5) # Pausa de 5 segundos para permitir al usuario leer la explicación antes de comenzar

    current_state = AutoPeli.initial_state # Estado actual del autómata
    pregunta_actual = 1 # Contador de la pregunta actual

    while current_state not in AutoPeli.final_states: # Bucle principal que se ejecuta hasta llegar a un estado final
        clear_output() # Limpiar la salida de la celda
        print("================================")
        print("Pregunta actual:", pregunta_actual)
        print("================================")
        Pregunta_Respuesta(current_state, f"Pregunta {pregunta_actual}:") # Mostrar la pregunta correspondiente al estado actual

        if pregunta_actual == 1: # Validar solo las respuestas de la primera pregunta
            input_symbol = input("Ingrese la respuesta: ").lower() # Obtener la respuesta del usuario en minúsculas

            while input_symbol not in ['an', 'c', 'ac', 't', 'r']: # Verificar si la respuesta es válida
                print("Respuesta no válida. Por favor, ingrese 'an', 'c', 'ac', 't' o 'r'.")
                input_symbol = input("Ingrese la respuesta: ").lower() # Solicitar al usuario que ingrese una respuesta válida

        else: # Validar las respuestas de las preguntas posteriores a la primera
            input_symbol = input("Ingrese la respuesta: ").lower() # Obtener la respuesta del usuario en minúsculas

            if input_symbol in ['sí', 'si', 's']: # Convertir respuestas afirmativas en 'v'
                input_symbol = 'v'
            elif input_symbol in ['no', 'n']: # Convertir respuestas negativas en 'f'
                input_symbol = 'f'
            else: # Si la respuesta no es válida, mostrar mensaje de error y solicitar respuesta válida
                print("Respuesta no válida. Por favor, ingrese 'sí' o 'no'.")
                time.sleep(2) # Pausa de 2 segundos para permitir que el usuario lea el mensaje de error
                continue # Volver al inicio del bucle sin incrementar el contador de pregunta

        try:
            next_state = AutoPeli.transitions[current_state].get(input_symbol) # Obtener el siguiente estado según la respuesta
            if next_state is None:
                raise KeyError
            pregunta_actual += 1 # Incrementar el contador de la pregunta actual
            current_state = next_state # Actualizar el estado actual con el siguiente estado
        except KeyError:
            print("Respuesta no válida. Por favor, ingrese 'sí' o 'no'.")
            time.sleep(2) # Pausa de 2 segundos para permitir que el usuario lea el mensaje de error

    clear_output() # Limpiar la salida de la celda
    print("================================")
    print("¡La película recomendada para ti es:")
    Pregunta_Respuesta(current_state, "Respuesta final:") # Mostrar la película recomendada según el estado final
    print("================================")
    print("¡Espero que disfrutes viendo la película! ¡Hasta pronto!")

compilador() # Llamar a la función principal para ejecutar el sistema de recomendación de películas