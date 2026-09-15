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