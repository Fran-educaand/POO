"""Paquete `persistence` que expone el gestor JSON.

Importar `read_data` y `write_data` desde `persistence.json_manager`.
"""

from .json_manager import read_data, write_data, DATA_FILE

__all__ = ["read_data", "write_data", "DATA_FILE"]
