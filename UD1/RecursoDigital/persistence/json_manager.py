"""Gestor JSON para la carpeta `data`.

Funciones:
- read_data(): devuelve lista/dict leído desde `data/recursos.json`.
- write_data(data): sobrescribe `data/recursos.json`.
"""
from pathlib import Path
import json

ROOT = Path(__file__).resolve().parent.parent
DATA_FILE = ROOT / "data" / "recursos.json"

def _ensure_file():
    if not DATA_FILE.exists():
        DATA_FILE.parent.mkdir(parents=True, exist_ok=True)
        DATA_FILE.write_text("[]", encoding="utf-8")

def read_data():
    _ensure_file()
    try:
        with DATA_FILE.open("r", encoding="utf-8") as f:
            return json.load(f)
    except (json.JSONDecodeError, ValueError):
        return []

def write_data(data):
    DATA_FILE.parent.mkdir(parents=True, exist_ok=True)
    with DATA_FILE.open("w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=2)

__all__ = ["read_data", "write_data", "DATA_FILE"]
