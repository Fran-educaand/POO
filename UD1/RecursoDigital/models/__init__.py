"""Paquete `models` que expone las clases de recursos digitales.

Permite `from models import LibroDigital, Podcast, VideoCurso, RecursoDigital, BibliotecaDigital`.
"""

from .RecursoDigital import RecursoDigital
from .LibroDigital import LibroDigital
from .Podcast import Podcast
from .VideoCurso import VideoCurso
from .BibliotecaDigital import BibliotecaDigital

__all__ = [
    "RecursoDigital",
    "LibroDigital",
    "Podcast",
    "VideoCurso",
    "BibliotecaDigital",
]
