import json
import random

FICHERO = "titanic.json"

def mostrar_datos(data):
    """Muestra los datos formateados por pantalla."""
    campos = ["PassengerId", "Name", "Sex", "Age", "Survived", "Pclass"]

    for entrada in data:
        for campo in campos:
            print(f"{campo}: {entrada.get(campo, 'N/A')}")
        print("-" * 40)


def añadir_nueva_entrada(data):
    """Añade una nueva entrada ficticia al dataset."""
    nueva_entrada = {
        "PassengerId": max(item["PassengerId"] for item in data) + 1,
        "Name": "Fictitious Passenger",
        "Sex": random.choice(["male", "female"]),
        "Age": round(random.uniform(1, 80), 1),
        "Survived": random.choice([0, 1]),
        "Pclass": random.choice([1, 2, 3])
    }

    data.append(nueva_entrada)
    return data


def guardar_datos(data):
    """Guarda los datos nuevamente en el fichero JSON."""
    with open(FICHERO, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=4, ensure_ascii=False)


def main():
    # Leer dataset
    with open(FICHERO, "r", encoding="utf-8") as f:
        data = json.load(f)

    print("\n=== CONTENIDO ORIGINAL ===\n")
    mostrar_datos(data)

    # Añadir nueva entrada
    data = añadir_nueva_entrada(data)

    # Guardar cambios
    guardar_datos(data)

    print("\n=== NUEVA ENTRADA AÑADIDA ===\n")
    mostrar_datos([data[-1]])


if __name__ == "__main__":
    main()
