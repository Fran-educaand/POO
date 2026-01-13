1. Objetivo de la entrega
El objetivo es separar correctamente las clases del modelo en ficheros independientes, crear una estructura de directorios profesional y convertir determinadas carpetas en paquetes Python mediante el uso de __init__.py.

Esta entrega evalúa tu capacidad para:

Aplicar programación orientada a objetos de forma estructurada.
Organizar un proyecto Python más allá de un único fichero.
Preparar el código para futuras ampliaciones (persistencia, base de datos, web).
2. Punto de partida
Debes partir del código de gestión de recursos digitales ya realizado en clase, que incluye al menos los siguientes tipos de recursos:

Libro digital
Vídeo digital
Podcast
Todos ellos deben modelarse mediante herencia a partir de una clase base común.

3. Estructura obligatoria del proyecto
Debes reorganizar el proyecto para que tenga, como mínimo, la siguiente estructura:

proyecto_recursos/
│
├── models/
│   ├── __init__.py
│   ├── recurso_digital.py
│   ├── libro_digital.py
│   ├── video_digital.py
│   └── podcast.py
│
├── persistence/
│   ├── __init__.py
│   └── json_manager.py
│
├── data/
│   └── recursos.json
│
├── main.py
└── README.md
Importante:

La carpeta models debe ser un paquete Python (contiene __init__.py).
La carpeta persistence también debe ser un paquete Python.
La carpeta data contiene datos, no código, y no debe llevar __init__.py.
4. Requisitos técnicos
Cada clase del modelo debe estar en su propio fichero.
RecursoDigital será la clase base común.
LibroDigital, VideoDigital y Podcast deben heredar de ella.
Los atributos deben estar encapsulados (atributos privados y uso de @property).
main.py no debe contener clases, solo lógica de ejecución.
El programa debe ejecutarse correctamente desde main.py.