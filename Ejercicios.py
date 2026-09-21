# Ejercicios de taller
class Calificador:
    def __init__(self):
        self.notas = []
    def validar_nota(self, nota):
        return 0 <= nota <= 100
    def cargar_notas(self, *args):
        for nota in args:
            if self.validar_nota(nota):
                self.notas.append(nota)
        return self.notas
    def promedio(self):
        return sum(self.notas) / len(self.notas)
c = Calificador()
print(c.cargar_notas(85, 92, 110, 78, -5, 88))
print(c.promedio())

class AnalizadorTexto:
    def __init__(self):
        self.palabras_unicas = set()
        self.orden_palabras = []
    def agregar_palabra(self, palabra):
        if palabra not in self.palabras_unicas:
            self.palabras_unicas.add(palabra)
            self.orden_palabras.append(palabra)
    def contar_palabras(self):
        return len(self.palabras_unicas)
    def agregar_multiples(self, *args):
        for palabra in args:
            self.agregar_palabra(palabra)
at = AnalizadorTexto()
at.agregar_multiples("hola","mundo","hola")
print(at.contar_palabras())

class CarroCompras:
    def __init__(self):
        self.articulos = {}
    def agregar_articulo(self, nombre, precio):
        self.articulos[nombre] = precio
    def total_carrito(self):
        return sum(self.articulos.values())
    def articulos_por_rango(self, precio_min, precio_max):
        resultado = []
        for nombre, precio in self.articulos.items():
            if precio_min <= precio <= precio_max:
                resultado.append(nombre)
        return resultado
c = CarroCompras()
c.agregar_articulo("pan",2.50)
c.agregar_articulo("leche",3.00)
print(c.total_carrito())

class InversorSecuencia:
    def invertir_lista(self, lista):
        invertida = []
        indice = len(lista) - 1
        while indice >= 0:
            invertida.append(lista[indice])
            indice -= 1
        return invertida
    def invertir_multiples(self, *listas):
        resultado = {}
        for lista in listas:
            original = tuple(lista)
            invertida = self.invertir_lista(lista)
            resultado[original] = invertida
        return resultado
inv = InversorSecuencia()
print(inv.invertir_lista([1,2,3]))

class AnalizadorNumeros:
    def __init__(self):
        self.pares = []
        self.impares = []
    def es_par(self, numero):
        return numero % 2 == 0
    def separar(self, *numeros):
        self.pares = []
        self.impares = []
        for numero in numeros:
            if self.es_par(numero):
                self.pares.append(numero)
            else:
                self.impares.append(numero)
        return {
            "pares": self.pares,
            "impares": self.impares
        }
    def cantidad_pares_impares(self):
        return len(self.pares), len(self.impares)
an = AnalizadorNumeros()
print(an.separar(1,2,3,4,5))

class GestorTemperatura:
    def __init__(self):
        self.temperaturas = []
    def registrar_temperatura(self, temp):
        self.temperaturas.append(temp)
    def registrar_multiples(self, *temps):
        for temp in temps:
            self.registrar_temperatura(temp)
    def minima(self):
        return min(self.temperaturas)
    def maxima(self):
        return max(self.temperaturas)
    def promedio(self):
        if len(self.temperaturas) == 0:
            return 0
        return sum(self.temperaturas) / len(self.temperaturas)
gt = GestorTemperatura()
gt.registrar_multiples(20, 25, 18, 30)
print(gt.promedio())

class GestorPersonas:
    def __init__(self):
        self.personas = {}
    def agregar_persona(self, nombre, edad):
        self.personas[nombre] = edad
    def personas_mayores(self, edad_minima):
        resultado = []
        for nombre, edad in self.personas.items():
            if edad >= edad_minima:
                resultado.append(nombre)
        return resultado
    def edad_promedio(self):
        if len(self.personas) == 0:
            return 0
        return sum(self.personas.values()) / len(self.personas)
gp = GestorPersonas()
gp.agregar_persona("Ana",28)
gp.agregar_persona("Bob",17)
print(gp.personas_mayores(18))

class Equipos:
    def __init__(self):
        self.equipos = {}
    def crear_equipo(self, nombre_equipo):
        self.equipos[nombre_equipo] = []
    def agregar_jugador(self, equipo, jugador):
        if equipo in self.equipos:
            self.equipos[equipo].append(jugador)
    def equipo_mayor_integrantes(self):
        if len(self.equipos) == 0:
            return None
        equipo_mayor = None
        mayor_cantidad = 0
        for equipo, jugadores in self.equipos.items():
            if len(jugadores) > mayor_cantidad:
                mayor_cantidad = len(jugadores)
                equipo_mayor = equipo
        return equipo_mayor
eq = Equipos()
eq.crear_equipo("A")
eq.crear_equipo("B")
eq.agregar_jugador("A","Juan")
eq.agregar_jugador("A","Pedro")

class AnalizadorString:
    def __init__(self):
        self.texto_mas_largo = ""
    def solo_vocales(self, letra):
        return letra.lower() in "aeiouáéíóú"
    def contar_por_tipo(self, texto):
        conteo = {
            "vocales": 0,
            "consonantes": 0,
            "digitos": 0
        }
        if len(texto) > len(self.texto_mas_largo):
            self.texto_mas_largo = texto
        for letra in texto:
            if self.solo_vocales(letra):
                conteo["vocales"] += 1
            elif letra.isdigit():
                conteo["digitos"] += 1
            elif letra.isalpha():
                conteo["consonantes"] += 1
        return conteo
astr = AnalizadorString()
print(astr.contar_por_tipo("Hola123"))

class Tareas:
    def __init__(self):
        self.tareas = []
    def agregar_tarea(self, descripcion, prioridad):
        self.tareas.append((descripcion, prioridad))
    def tareas_prioritarias(self):
        resultado = []
        for tarea in self.tareas:
            if tarea[1].lower() == "alta":
                resultado.append(tarea)
        return resultado
    def eliminar_completada(self, descripcion):
        for tarea in self.tareas:
            if tarea[0] == descripcion:
                self.tareas.remove(tarea)
                return True
        return False
t = Tareas()
t.agregar_tarea("Estudiar", "alta")
t.agregar_tarea("Leer", "baja")
print(t.tareas_prioritarias())

class ContadorFrecuencia:
    def __init__(self):
        self.frecuencias = {}
    def agregar_elemento(self, elemento):
        if elemento in self.frecuencias:
            self.frecuencias[elemento] += 1
        else:
            self.frecuencias[elemento] = 1
    def elemento_mas_frecuente(self):
        if len(self.frecuencias) == 0:
            return None
        elemento_mayor = None
        mayor = 0
        for elemento, frecuencia in self.frecuencias.items():
            if frecuencia > mayor:
                mayor = frecuencia
                elemento_mayor = elemento
        return elemento_mayor
    def frecuencia_elemento(self, elemento):
        return self.frecuencias.get(elemento, 0)
cf = ContadorFrecuencia()
cf.agregar_elemento("a")
cf.agregar_elemento("b")
cf.agregar_elemento("a")
print(cf.elemento_mas_frecuente())

class SelectorRango:
    def crear_rango(self, inicio, fin):
        numeros = []
        for numero in range(inicio, fin + 1):
            numeros.append(numero)
        return tuple(numeros)
    def elementos_en_multiples_rangos(self, *rangos):
        elementos = set()
        for rango in rangos:
            inicio = rango[0]
            fin = rango[1]
            numeros = self.crear_rango(inicio, fin)
            for numero in numeros:
                elementos.add(numero)
        return sorted(list(elementos))
sr = SelectorRango()
print(sr.crear_rango(1, 3))
print(sr.elementos_en_multiples_rangos((1, 3), (2, 4)))

class CombinadorListas:
    def intercalar(self, lista1, lista2):
        resultado = []
        mayor = max(len(lista1), len(lista2))
        for i in range(mayor):
            if i < len(lista1):
                resultado.append(lista1[i])
            if i < len(lista2):
                resultado.append(lista2[i])
        return resultado
    def intercalar_multiples(self, *listas):
        if len(listas) == 0:
            return []
        resultado = list(listas[0])
        for i in range(1, len(listas)):
            resultado = self.intercalar(resultado, listas[i])
        return resultado
cl = CombinadorListas()
print(cl.intercalar([1,2], [3,4]))

class RegistroNotas:
    def __init__(self):
        self.notas = {}
    def registrar(self, estudiante, nota):
        self.notas[estudiante] = nota
    def estudiantes_aprobados(self, nota_minima):
        aprobados = []
        for estudiante, nota in self.notas.items():
            if nota >= nota_minima:
                aprobados.append(estudiante)
        return aprobados
    def mejor_estudiante(self):
        if len(self.notas) == 0:
            return None
        mejor_nombre = None
        mejor_nota = None
        for estudiante, nota in self.notas.items():
            if mejor_nota is None or nota > mejor_nota:
                mejor_nombre = estudiante
                mejor_nota = nota
        return mejor_nombre, mejor_nota
rn = RegistroNotas()
rn.registrar("Ana", 95)
rn.registrar("Bob", 70)
print(rn.mejor_estudiante())

class DivisorFinder:
    def encontrar_divisores(self, numero):
        divisores = []
        if numero <= 0:
            return tuple(divisores)
        for i in range(1, numero + 1):
            if numero % i == 0:
                divisores.append(i)
        return tuple(divisores)
    def es_perfecto(self, numero):
        divisores = self.encontrar_divisores(numero)
        suma = 0
        for divisor in divisores:
            if divisor != numero:
                suma += divisor
        return suma == numero
    def encontrar_multiples_divisores(self, *numeros):
        resultado = {}
        for numero in numeros:
            resultado[numero] = self.encontrar_divisores(numero)
        return resultado
df = DivisorFinder()
print(df.encontrar_divisores(12))

class CodificadorCesar:
    def __init__(self):
        self.historial = {}
    def codificar_letra(self, letra, desplazamiento):
        if not letra.isalpha():
            return letra
        if letra.islower():
            inicio = ord('a')
        else:
            inicio = ord('A')
        codigo = ord(letra) - inicio
        nuevo_codigo = (codigo + desplazamiento) % 26
        return chr(nuevo_codigo + inicio)
    def codificar_palabra(self, palabra, desplazamiento):
        resultado = ""
        for letra in palabra:
            resultado += self.codificar_letra(letra, desplazamiento)
        self.historial[palabra] = resultado
        return resultado
cc = CodificadorCesar()
print(cc.codificar_palabra("hola", 3))

class AgrupadorEdades:
    def __init__(self):
        self.categorias = {
            "niño": [],
            "adolescente": [],
            "adulto": [],
            "mayor": []
        }
    def clasificar_edad(self, edad):
        if edad < 13:
            return "niño"
        elif edad < 18:
            return "adolescente"
        elif edad < 65:
            return "adulto"
        else:
            return "mayor"
    def agrupar_por_categoria(self, *edades):
        self.categorias = {
            "niño": [],
            "adolescente": [],
            "adulto": [],
            "mayor": []
        }
        for edad in edades:
            categoria = self.clasificar_edad(edad)
            self.categorias[categoria].append(edad)
        return self.categorias
    def edad_promedio_categoria(self, categoria):
        if categoria not in self.categorias:
            return 0
        edades = self.categorias[categoria]
        if len(edades) == 0:
            return 0
        return sum(edades) / len(edades)
ae = AgrupadorEdades()
print(ae.agrupar_por_categoria(5, 15, 30, 70))

class CalculadorDistancia:
    def __init__(self):
        self.distancias = []
    def distancia_euclidiana(self, p1, p2):
        x1 = p1[0]
        y1 = p1[1]
        x2 = p2[0]
        y2 = p2[1]
        distancia = (
            (x2 - x1) ** 2 +
            (y2 - y1) ** 2
        ) ** 0.5
        self.distancias.append(distancia)
        return distancia
    def punto_mas_cercano(self, referencia, *puntos):
        if len(puntos) == 0:
            return None
        punto_cercano = None
        menor_distancia = None
        for punto in puntos:
            distancia = self.distancia_euclidiana(
                referencia,
                punto
            )
            if menor_distancia is None or distancia < menor_distancia:
                menor_distancia = distancia
                punto_cercano = punto
        return punto_cercano
cd = CalculadorDistancia()
print(cd.distancia_euclidiana((0,0), (3,4)))

class Inventario:
    def __init__(self):
        self.productos = {}
    def agregar_stock(self, producto, cantidad):
        if producto in self.productos:
            self.productos[producto] += cantidad
        else:
            self.productos[producto] = cantidad
    def restar_stock(self, producto, cantidad):
        if producto not in self.productos:
            return False
        if self.productos[producto] < cantidad:
            return False
        self.productos[producto] -= cantidad
        return True
    def productos_bajo_stock(self, minimo):
        resultado = []
        for producto, cantidad in self.productos.items():
            if cantidad < minimo:
                resultado.append(producto)
        return resultado
inv = Inventario()
inv.agregar_stock("pan", 50)
print(inv.restar_stock("pan", 30))
print(inv.productos_bajo_stock(15))

class AnalizadorPatrones:
    def __init__(self):
        self.palabras = []
    def encontrar_palabras(self, texto, patron):
        palabras = texto.split()
        resultado = []
        for palabra in palabras:
            if palabra.lower().startswith(patron.lower()):
                resultado.append(palabra)
        return resultado
    def agrupar_por_longitud(self, texto):
        resultado = {}
        for palabra in texto.split():
            longitud = len(palabra)
            if longitud not in resultado:
                resultado[longitud] = []
            resultado[longitud].append(palabra)
        return resultado
    def palabras_unicas(self):
        return set(self.palabras)
    def cargar_texto(self, texto):
        palabras = texto.split()
        for palabra in palabras:
            self.palabras.append(palabra)
ap = AnalizadorPatrones()
print(ap.agrupar_por_longitud("el gato está aquí"))

# Ejercicios de práctica
class GestorAutos:
    def __init__(self):
        self.autos = {}
    def validar_anio(self, anio):
        return 1950 <= anio <= 2026
    def registrar_auto(self, placa, marca, anio):
        if self.validar_anio(anio):
            self.autos[placa] = {"marca": marca, "anio": anio}
        return self.autos
    def registrar_multiples(self, *autos):
        for placa, marca, anio in autos:
            self.registrar_auto(placa, marca, anio)
        return self.autos
    def autos_por_anio(self, anio_min):
        resultado = []
        for placa, datos in self.autos.items():
            if datos["anio"] >= anio_min:
                resultado.append(placa)
        return resultado
ga = GestorAutos()
ga.registrar_multiples(("ABC123", "Toyota", 2018), ("XYZ999", "Ford", 2010), ("LMN111", "Honda", 2022))
print(ga.autos_por_anio(2015))


class Biblioteca:
    def __init__(self):
        self.libros = {}
    def agregar_libro(self, titulo, autor, paginas):
        self.libros[titulo] = {"autor": autor, "paginas": paginas}
    def libros_de_autor(self, autor):
        resultado = []
        for titulo, datos in self.libros.items():
            if datos["autor"].lower() == autor.lower():
                resultado.append(titulo)
        return resultado
    def libro_mas_largo(self):
        if len(self.libros) == 0:
            return None
        mayor_titulo = None
        mayor_paginas = 0
        for titulo, datos in self.libros.items():
            if datos["paginas"] > mayor_paginas:
                mayor_paginas = datos["paginas"]
                mayor_titulo = titulo
        return mayor_titulo, mayor_paginas
bib = Biblioteca()
bib.agregar_libro("Cien años", "García Márquez", 417)
bib.agregar_libro("El otoño", "García Márquez", 272)
bib.agregar_libro("Rayuela", "Cortázar", 635)
print(bib.libros_de_autor("García Márquez"))
print(bib.libro_mas_largo())


class Zoologico:
    def __init__(self):
        self.animales = []
    def agregar_animal(self, nombre, especie, edad):
        self.animales.append({"nombre": nombre, "especie": especie, "edad": edad})
    def agregar_multiples(self, *animales):
        for nombre, especie, edad in animales:
            self.agregar_animal(nombre, especie, edad)
    def contar_por_especie(self):
        conteo = {}
        for animal in self.animales:
            especie = animal["especie"]
            if especie not in conteo:
                conteo[especie] = 0
            conteo[especie] += 1
        return conteo
    def animal_mas_viejo(self):
        if len(self.animales) == 0:
            return None
        mayor = self.animales[0]
        for animal in self.animales:
            if animal["edad"] > mayor["edad"]:
                mayor = animal
        return mayor["nombre"]
zoo = Zoologico()
zoo.agregar_multiples(("Simba", "león", 8), ("Dumbo", "elefante", 15), ("Nala", "león", 6))
print(zoo.contar_por_especie())
print(zoo.animal_mas_viejo())


class Recetario:
    def __init__(self):
        self.recetas = {}
    def agregar_receta(self, nombre, ingredientes):
        self.recetas[nombre] = list(ingredientes)
    def recetas_con_ingrediente(self, ingrediente):
        resultado = []
        for nombre, ingredientes in self.recetas.items():
            if ingrediente.lower() in [i.lower() for i in ingredientes]:
                resultado.append(nombre)
        return resultado
    def receta_mas_ingredientes(self):
        if len(self.recetas) == 0:
            return None
        mayor_nombre = None
        mayor = 0
        for nombre, ingredientes in self.recetas.items():
            if len(ingredientes) > mayor:
                mayor = len(ingredientes)
                mayor_nombre = nombre
        return mayor_nombre
rec = Recetario()
rec.agregar_receta("pasta", ["harina", "huevo", "sal"])
rec.agregar_receta("ensalada", ["lechuga", "tomate", "aceite", "sal"])
print(rec.recetas_con_ingrediente("sal"))
print(rec.receta_mas_ingredientes())


class Playlist:
    def __init__(self):
        self.canciones = []
    def agregar_cancion(self, titulo, artista, duracion):
        self.canciones.append({"titulo": titulo, "artista": artista, "duracion": duracion})
    def agregar_multiples(self, *canciones):
        for titulo, artista, duracion in canciones:
            self.agregar_cancion(titulo, artista, duracion)
    def duracion_total(self):
        return sum(c["duracion"] for c in self.canciones)
    def canciones_de_artista(self, artista):
        resultado = []
        for c in self.canciones:
            if c["artista"].lower() == artista.lower():
                resultado.append(c["titulo"])
        return resultado
pl = Playlist()
pl.agregar_multiples(("Imagine", "Lennon", 183), ("Hey Jude", "Beatles", 431), ("Yesterday", "Beatles", 125))
print(pl.duracion_total())
print(pl.canciones_de_artista("Beatles"))


class Cartelera:
    def __init__(self):
        self.peliculas = {}
    def agregar_pelicula(self, titulo, anio, puntaje):
        if 0 <= puntaje <= 10:
            self.peliculas[titulo] = {"anio": anio, "puntaje": puntaje}
    def peliculas_por_anio(self, anio_min, anio_max):
        resultado = []
        for titulo, datos in self.peliculas.items():
            if anio_min <= datos["anio"] <= anio_max:
                resultado.append(titulo)
        return resultado
    def mejor_pelicula(self):
        if len(self.peliculas) == 0:
            return None
        mejor = None
        mejor_puntaje = -1
        for titulo, datos in self.peliculas.items():
            if datos["puntaje"] > mejor_puntaje:
                mejor_puntaje = datos["puntaje"]
                mejor = titulo
        return mejor, mejor_puntaje
cin = Cartelera()
cin.agregar_pelicula("Matrix", 1999, 8.7)
cin.agregar_pelicula("Inception", 2010, 8.8)
cin.agregar_pelicula("Titanic", 1997, 7.9)
print(cin.peliculas_por_anio(1998, 2012))
print(cin.mejor_pelicula())


class Banco:
    def __init__(self):
        self.cuentas = {}
    def abrir_cuenta(self, titular, saldo=0):
        if titular not in self.cuentas:
            self.cuentas[titular] = saldo
        return self.cuentas[titular]
    def depositar(self, titular, monto):
        if titular not in self.cuentas or monto <= 0:
            return False
        self.cuentas[titular] += monto
        return True
    def retirar(self, titular, monto):
        if titular not in self.cuentas or monto <= 0:
            return False
        if self.cuentas[titular] < monto:
            return False
        self.cuentas[titular] -= monto
        return True
    def saldo_total(self):
        return sum(self.cuentas.values())
ban = Banco()
ban.abrir_cuenta("Ana", 100)
ban.abrir_cuenta("Bob", 50)
print(ban.depositar("Ana", 40))
print(ban.retirar("Bob", 20))
print(ban.saldo_total())


class Hotel:
    def __init__(self):
        self.habitaciones = {}
    def registrar_habitacion(self, numero, tipo, precio):
        self.habitaciones[numero] = {"tipo": tipo, "precio": precio, "ocupada": False}
    def ocupar(self, numero):
        if numero not in self.habitaciones:
            return False
        if self.habitaciones[numero]["ocupada"]:
            return False
        self.habitaciones[numero]["ocupada"] = True
        return True
    def disponibles(self):
        resultado = []
        for numero, datos in self.habitaciones.items():
            if not datos["ocupada"]:
                resultado.append(numero)
        return resultado
    def habitaciones_por_precio(self, precio_max):
        resultado = []
        for numero, datos in self.habitaciones.items():
            if datos["precio"] <= precio_max:
                resultado.append(numero)
        return resultado
ht = Hotel()
ht.registrar_habitacion(101, "simple", 40)
ht.registrar_habitacion(202, "doble", 70)
ht.ocupar(101)
print(ht.disponibles())
print(ht.habitaciones_por_precio(50))


class Restaurante:
    def __init__(self):
        self.pedidos = []
    def agregar_pedido(self, mesa, plato, precio):
        self.pedidos.append({"mesa": mesa, "plato": plato, "precio": precio})
    def total_mesa(self, mesa):
        total = 0
        for pedido in self.pedidos:
            if pedido["mesa"] == mesa:
                total += pedido["precio"]
        return total
    def platos_caros(self, minimo):
        resultado = []
        for pedido in self.pedidos:
            if pedido["precio"] >= minimo:
                resultado.append(pedido["plato"])
        return resultado
res = Restaurante()
res.agregar_pedido(1, "sopa", 4.5)
res.agregar_pedido(1, "steak", 12.0)
res.agregar_pedido(2, "ensalada", 6.0)
print(res.total_mesa(1))
print(res.platos_caros(6))


class Jardin:
    def __init__(self):
        self.plantas = {}
    def sembrar(self, nombre, tipo, riegos):
        self.plantas[nombre] = {"tipo": tipo, "riegos": riegos}
    def regar(self, nombre):
        if nombre not in self.plantas:
            return False
        self.plantas[nombre]["riegos"] += 1
        return True
    def plantas_secas(self, minimo_riegos):
        resultado = []
        for nombre, datos in self.plantas.items():
            if datos["riegos"] < minimo_riegos:
                resultado.append(nombre)
        return resultado
    def contar_por_tipo(self):
        conteo = {}
        for datos in self.plantas.values():
            tipo = datos["tipo"]
            if tipo not in conteo:
                conteo[tipo] = 0
            conteo[tipo] += 1
        return conteo
jd = Jardin()
jd.sembrar("rosa", "flor", 2)
jd.sembrar("albahaca", "hierba", 0)
jd.regar("rosa")
print(jd.plantas_secas(2))
print(jd.contar_por_tipo())


class Academia:
    def __init__(self):
        self.cursos = {}
    def crear_curso(self, nombre):
        if nombre not in self.cursos:
            self.cursos[nombre] = []
    def inscribir(self, curso, estudiante):
        if curso in self.cursos:
            self.cursos[curso].append(estudiante)
    def curso_mas_lleno(self):
        if len(self.cursos) == 0:
            return None
        mayor_curso = None
        mayor = -1
        for curso, alumnos in self.cursos.items():
            if len(alumnos) > mayor:
                mayor = len(alumnos)
                mayor_curso = curso
        return mayor_curso
    def estudiantes_unicos(self):
        unicos = set()
        for alumnos in self.cursos.values():
            for alumno in alumnos:
                unicos.add(alumno)
        return unicos
ac = Academia()
ac.crear_curso("Python")
ac.crear_curso("Excel")
ac.inscribir("Python", "Ana")
ac.inscribir("Python", "Luis")
ac.inscribir("Excel", "Ana")
print(ac.curso_mas_lleno())
print(ac.estudiantes_unicos())


class Gimnasio:
    def __init__(self):
        self.entrenos = []
    def registrar_entreno(self, persona, ejercicio, calorias):
        self.entrenos.append({"persona": persona, "ejercicio": ejercicio, "calorias": calorias})
    def calorias_persona(self, persona):
        total = 0
        for entreno in self.entrenos:
            if entreno["persona"] == persona:
                total += entreno["calorias"]
        return total
    def ejercicios_unicos(self):
        resultado = set()
        for entreno in self.entrenos:
            resultado.add(entreno["ejercicio"])
        return resultado
gim = Gimnasio()
gim.registrar_entreno("Ana", "correr", 300)
gim.registrar_entreno("Ana", "pesas", 150)
gim.registrar_entreno("Bob", "correr", 200)
print(gim.calorias_persona("Ana"))
print(gim.ejercicios_unicos())


class Aerolinea:
    def __init__(self):
        self.vuelos = []
    def agregar_vuelo(self, codigo, origen, destino, asientos):
        self.vuelos.append({
            "codigo": codigo,
            "origen": origen,
            "destino": destino,
            "asientos": asientos
        })
    def vuelos_hacia(self, destino):
        resultado = []
        for vuelo in self.vuelos:
            if vuelo["destino"].lower() == destino.lower():
                resultado.append(vuelo["codigo"])
        return resultado
    def vuelo_con_mas_asientos(self):
        if len(self.vuelos) == 0:
            return None
        mayor = self.vuelos[0]
        for vuelo in self.vuelos:
            if vuelo["asientos"] > mayor["asientos"]:
                mayor = vuelo
        return mayor["codigo"]
ae = Aerolinea()
ae.agregar_vuelo("LA100", "Lima", "Bogotá", 180)
ae.agregar_vuelo("AV220", "Lima", "Quito", 120)
ae.agregar_vuelo("LA330", "Cusco", "Bogotá", 90)
print(ae.vuelos_hacia("Bogotá"))
print(ae.vuelo_con_mas_asientos())


class TiendaJuegos:
    def __init__(self):
        self.juegos = {}
    def agregar_juego(self, titulo, precio, stock):
        self.juegos[titulo] = {"precio": precio, "stock": stock}
    def vender(self, titulo, cantidad):
        if titulo not in self.juegos:
            return False
        if self.juegos[titulo]["stock"] < cantidad:
            return False
        self.juegos[titulo]["stock"] -= cantidad
        return True
    def juegos_baratos(self, precio_max):
        resultado = []
        for titulo, datos in self.juegos.items():
            if datos["precio"] <= precio_max:
                resultado.append(titulo)
        return resultado
tj = TiendaJuegos()
tj.agregar_juego("Zelda", 60, 10)
tj.agregar_juego("Mario", 40, 5)
print(tj.vender("Mario", 2))
print(tj.juegos_baratos(50))


class SistemaSolar:
    def __init__(self):
        self.planetas = {}
    def agregar_planeta(self, nombre, distancia, lunas):
        self.planetas[nombre] = {"distancia": distancia, "lunas": lunas}
    def planeta_mas_lejos(self):
        if len(self.planetas) == 0:
            return None
        lejano = None
        mayor = -1
        for nombre, datos in self.planetas.items():
            if datos["distancia"] > mayor:
                mayor = datos["distancia"]
                lejano = nombre
        return lejano
    def planetas_con_lunas(self, minimo):
        resultado = []
        for nombre, datos in self.planetas.items():
            if datos["lunas"] >= minimo:
                resultado.append(nombre)
        return resultado
ss = SistemaSolar()
ss.agregar_planeta("Tierra", 1, 1)
ss.agregar_planeta("Marte", 1.5, 2)
ss.agregar_planeta("Júpiter", 5.2, 95)
print(ss.planeta_mas_lejos())
print(ss.planetas_con_lunas(2))


class Nomina:
    def __init__(self):
        self.empleados = {}
    def registrar_empleado(self, nombre, cargo, sueldo):
        self.empleados[nombre] = {"cargo": cargo, "sueldo": sueldo}
    def sueldo_promedio(self):
        if len(self.empleados) == 0:
            return 0
        return sum(e["sueldo"] for e in self.empleados.values()) / len(self.empleados)
    def empleados_sobre_promedio(self):
        promedio = self.sueldo_promedio()
        resultado = []
        for nombre, datos in self.empleados.items():
            if datos["sueldo"] > promedio:
                resultado.append(nombre)
        return resultado
    def empleados_por_cargo(self, cargo):
        resultado = []
        for nombre, datos in self.empleados.items():
            if datos["cargo"].lower() == cargo.lower():
                resultado.append(nombre)
        return resultado
nm = Nomina()
nm.registrar_empleado("Ana", "analista", 2500)
nm.registrar_empleado("Luis", "gerente", 4200)
nm.registrar_empleado("Eva", "analista", 2300)
print(nm.sueldo_promedio())
print(nm.empleados_sobre_promedio())


class Veterinaria:
    def __init__(self):
        self.mascotas = []
    def registrar_mascota(self, nombre, especie, peso):
        self.mascotas.append({"nombre": nombre, "especie": especie, "peso": peso})
    def registrar_multiples(self, *mascotas):
        for nombre, especie, peso in mascotas:
            self.registrar_mascota(nombre, especie, peso)
    def mascotas_por_especie(self, especie):
        resultado = []
        for m in self.mascotas:
            if m["especie"].lower() == especie.lower():
                resultado.append(m["nombre"])
        return resultado
    def mascota_mas_pesada(self):
        if len(self.mascotas) == 0:
            return None
        mayor = self.mascotas[0]
        for m in self.mascotas:
            if m["peso"] > mayor["peso"]:
                mayor = m
        return mayor["nombre"]
vet = Veterinaria()
vet.registrar_multiples(("Max", "perro", 18.5), ("Michi", "gato", 4.2), ("Rocky", "perro", 22.0))
print(vet.mascotas_por_especie("perro"))
print(vet.mascota_mas_pesada())


class CatalogoDiscos:
    def __init__(self):
        self.discos = {}
    def agregar_disco(self, titulo, artista, anio):
        self.discos[titulo] = {"artista": artista, "anio": anio}
    def discos_despues_de(self, anio):
        resultado = []
        for titulo, datos in self.discos.items():
            if datos["anio"] > anio:
                resultado.append(titulo)
        return resultado
    def artistas_unicos(self):
        artistas = set()
        for datos in self.discos.values():
            artistas.add(datos["artista"])
        return artistas
cd = CatalogoDiscos()
cd.agregar_disco("Abbey Road", "Beatles", 1969)
cd.agregar_disco("Thriller", "Jackson", 1982)
cd.agregar_disco("Bad", "Jackson", 1987)
print(cd.discos_despues_de(1970))
print(cd.artistas_unicos())


class RedSocial:
    def __init__(self):
        self.usuarios = {}
    def crear_usuario(self, nombre):
        if nombre not in self.usuarios:
            self.usuarios[nombre] = []
    def agregar_amigo(self, usuario, amigo):
        if usuario in self.usuarios and amigo != usuario:
            if amigo not in self.usuarios[usuario]:
                self.usuarios[usuario].append(amigo)
    def usuario_con_mas_amigos(self):
        if len(self.usuarios) == 0:
            return None
        mayor_usuario = None
        mayor = -1
        for usuario, amigos in self.usuarios.items():
            if len(amigos) > mayor:
                mayor = len(amigos)
                mayor_usuario = usuario
        return mayor_usuario
    def amigos_en_comun(self, u1, u2):
        if u1 not in self.usuarios or u2 not in self.usuarios:
            return []
        comunes = []
        for amigo in self.usuarios[u1]:
            if amigo in self.usuarios[u2]:
                comunes.append(amigo)
        return comunes
rs = RedSocial()
rs.crear_usuario("Ana")
rs.crear_usuario("Bob")
rs.crear_usuario("Eva")
rs.agregar_amigo("Ana", "Bob")
rs.agregar_amigo("Ana", "Eva")
rs.agregar_amigo("Bob", "Eva")
print(rs.usuario_con_mas_amigos())
print(rs.amigos_en_comun("Ana", "Bob"))


class Parqueadero:
    def __init__(self):
        self.vehiculos = {}
    def ingresar(self, placa, tipo, horas):
        self.vehiculos[placa] = {"tipo": tipo, "horas": horas}
    def cobrar(self, placa, tarifa_hora):
        if placa not in self.vehiculos:
            return 0
        return self.vehiculos[placa]["horas"] * tarifa_hora
    def vehiculos_por_tipo(self, tipo):
        resultado = []
        for placa, datos in self.vehiculos.items():
            if datos["tipo"].lower() == tipo.lower():
                resultado.append(placa)
        return resultado
    def mas_horas(self):
        if len(self.vehiculos) == 0:
            return None
        mayor_placa = None
        mayor = -1
        for placa, datos in self.vehiculos.items():
            if datos["horas"] > mayor:
                mayor = datos["horas"]
                mayor_placa = placa
        return mayor_placa
pk = Parqueadero()
pk.ingresar("ABC123", "auto", 3)
pk.ingresar("MOTO9", "moto", 5)
pk.ingresar("XYZ777", "auto", 2)
print(pk.cobrar("ABC123", 4))
print(pk.vehiculos_por_tipo("auto"))
print(pk.mas_horas())
