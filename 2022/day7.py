"""
--- Day 7: No Space Left On Device ---
You can hear birds chirping and raindrops hitting leaves as the expedition proceeds.
Occasionally, you can even hear much louder sounds in the distance; how big do the animals get out here, anyway?

The device the Elves gave you has problems with more than just its communication system. You try to run a system update:

$ system-update --please --pretty-please-with-sugar-on-top
Error: No space left on device
Perhaps you can delete some files to make space for the update?

More details in the puzzle description: https://adventofcode.com/2022/day/7
"""

def parsear(data):
    data = data.split("$ ")
    comandos = []
    for cosa in data:
        cosa = cosa.split("\n")
        cosa = [x for x in cosa if x != ""]
        if len (cosa) == 1:
            command = cosa[0].split(" ")
            command = {command[0]: command[1]}
            comandos.append(command)
        elif len(cosa) > 1:
            command = cosa[0]
            result = cosa[1:]
            comandos.append({command: result})
    return comandos

def crear_archivos(comandos):
    directorios = {}
    route = ""
    saved_routes = []
    for comando in comandos:
        (comando, resultado) = comando.popitem()
        if comando == 'cd':
            if resultado == "..":
                route = route[:route.rfind("/")]
                route = route[:route.rfind("/")] + "/"
            else:
                if route == "":
                    route = resultado
                else:
                    route += resultado + "/"
                    if route not in saved_routes:
                        saved_routes.append(route)
                        actual_route = route.split("/")
                        actual_route = [x for x in actual_route if x != ""]
                        # Modificación: usamos un ciclo for para recorrer todos los niveles de carpetas
                        # y agregar cada uno al diccionario
                        directorio_actual = directorios
                        for i in range(len(actual_route)):
                            nombre_carpeta = actual_route[i]
                            if nombre_carpeta not in directorio_actual:
                                directorio_actual[nombre_carpeta] = {}
                            directorio_actual = directorio_actual[nombre_carpeta]

        elif comando == 'ls':
            # acceder a la ruta actual
            actual_route = route.split("/")
            actual_route = [x for x in actual_route if x != ""]
            directorio_actual = directorios
            for i in range(len(actual_route)):
                nombre_carpeta = actual_route[i]
                directorio_actual = directorio_actual[nombre_carpeta]
            for archivo_carpeta in resultado:
                tipo, nombre = archivo_carpeta.split(" ")
                if tipo == "dir":
                    if nombre not in directorio_actual:
                        directorio_actual[nombre] = {}
                else:
                    directorio_actual[nombre] = tipo
    return directorios

def second_part(data):
    pass

if __name__ == "__main__":
    with open("example/day7.txt") as f: data = f.read()
    comandos = parsear(data)
    directorios = crear_archivos(comandos)
    print(directorios)