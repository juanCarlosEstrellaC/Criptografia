import os
import time
import hashlib
from cryptography.hazmat.primitives import serialization
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives.asymmetric import ed25519

def generar_par_claves():
    clave_privada = ed25519.Ed25519PrivateKey.generate()
    clave_publica = clave_privada.public_key()
    return clave_privada, clave_publica

def firmar_archivo(clave_privada, archivo):
    with open(archivo, "rb") as f:
        mensaje = f.read()
    firma = clave_privada.sign(mensaje)
    return firma

def verificar_firma(clave_publica, archivo, firma):
    with open(archivo, "rb") as f:
        mensaje = f.read()
    try:
        clave_publica.verify(firma, mensaje)
        return True
    except:
        return False

import time

def ejecutar():
    archivos = [
        "C:\\Users\\Lap\\Documents\\Criptografia\\EdDSA\\texto_de_10.txt",
        "C:\\Users\\Lap\\Documents\\Criptografia\\EdDSA\\texto_de_1000.txt",
        "C:\\Users\\Lap\\Documents\\Criptografia\\EdDSA\\texto_de_10000.txt",
        "C:\\Users\\Lap\\Documents\\Criptografia\\EdDSA\\texto_de_100000.txt",
        "C:\\Users\\Lap\\Documents\\Criptografia\\EdDSA\\texto_de_1000000.txt",
        "C:\\Users\\Lap\\Documents\\Criptografia\\EdDSA\\texto_de_10000000.txt"
    ]

    for archivo in archivos:
        print(f"\nProcesando archivo: {archivo}")
        clave_privada, clave_publica = generar_par_claves()

        tiempo_inicio = time.time() * 1000  # Convertir segundos a milisegundos
        firma = firmar_archivo(clave_privada, archivo)
        print("Tiempo de firma:", time.time() * 1000 - tiempo_inicio, "milisegundos")

        tiempo_inicio = time.time() * 1000  # Convertir segundos a milisegundos
        verificado = verificar_firma(clave_publica, archivo, firma)
        print("Tiempo de verificación:", time.time() * 1000 - tiempo_inicio, "milisegundos")
        print("Firma verificada:", verificado)


print("Resultados")
ejecutar()

