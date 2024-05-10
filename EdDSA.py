import random

def generar_archivo(num_palabras):
    with open(f"C:\\Users\\Lap\\Documents\\Criptografia\\EdDSA\\texto_de_{num_palabras}.txt", "w") as archivo:
        lista_palabras = [
            "hola", "mundo", "ejemplo", "python", "programacion", "lenguaje", "criptografia", "seguridad",
            "casa", "perro", "gato", "auto", "mesa", "silla", "comida", "agua", "cafe", "amigo",
            "familia", "trabajo", "escuela", "amor", "vida", "juego", "fiesta", "musica", "libro",
            "pelicula", "viaje", "dinero", "tiempo", "mundo", "ciudad", "parque", "playa", "montaña",
            "deporte", "ejercicio", "salud", "medicina", "doctor", "enfermedad", "luz", "oscuridad",
            "calor", "frio", "lluvia", "viento", "nieve", "cielo", "estrella", "luna", "sol",
            "arbol", "flor", "fruta", "verdura", "color", "rojo", "azul", "verde", "amarillo"
        ]
        for _ in range(num_palabras):
            palabra = random.choice(lista_palabras)
            archivo.write(palabra + " ")

generar_archivo(10)  
generar_archivo(10)  
generar_archivo(1000)  
generar_archivo(10000)  
generar_archivo(100000)  
generar_archivo(1000000)  
generar_archivo(10000000)  
