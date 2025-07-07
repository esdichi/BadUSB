import hashlib
import os
from datetime import datetime

ruta = "PAYLOAD.EXE"

# Tamaño en bytes
tamaño = os.path.getsize(ruta)

# Hash MD5
with open(ruta, "rb") as f:
    hash_md5 = hashlib.md5(f.read()).hexdigest().upper()

# Fecha y hora de modificación
tiempo = os.path.getmtime(ruta)
fecha = datetime.fromtimestamp(tiempo).strftime("%Y-%m-%d")
hora = datetime.fromtimestamp(tiempo).strftime("%H:%M")

print(f"FS = {tamaño}")
print(f"HV = {hash_md5}")
print(f"DA = {fecha}")
print(f"TI = {hora}")

input("Pulsa Enter para cerrar...")