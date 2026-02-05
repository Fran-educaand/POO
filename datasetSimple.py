import json
import random

# Archivo descargado
FICHERO = "titanic.json"

# Campos que queremos mostrar
CAMPOS = ["PassengerId", "Name", "Sex", "Age", "Survived", "Pclass"]

# Leer JSON
with open(FICHERO, "r", encoding="utf-8") as f:
    data = json.load(f)

# Mostrar datos
for p in data:
    for campo in CAMPOS:
        print(f"{campo}: {p.get(campo)}")
    print("-" * 30)

# Crear nueva entrada sencilla
nuevo = {
    "PassengerId": data[-1]["PassengerId"] + 1,
    "Name": "Passenger Test",
    "Sex": random.choice(["male", "female"]),
    "Age": random.randint(1, 80),
    "Survived": random.choice([0, 1]),
    "Pclass": random.choice([1, 2, 3])
}

# Añadir al dataset
data.append(nuevo)

# Guardar de nuevo
with open(FICHERO, "w", encoding="utf-8") as f:
    json.dump(data, f, indent=4)

print("\nNueva entrada añadida:")
for campo in CAMPOS:
    print(f"{campo}: {nuevo[campo]}")
