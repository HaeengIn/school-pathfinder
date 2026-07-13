from pathlib import Path
import json

DATA_DIR = Path(__file__).parent.parent / "data"


def load_json(filename: str):
    with open(DATA_DIR / filename, encoding="utf-8") as f:
        return json.load(f)
