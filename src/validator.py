from src.loader import load_json
from src.utils import normalize_place

nodes = load_json("nodes.json")


def validate_place(place: str) -> str:
    place = normalize_place(place)

    if place not in nodes:
        raise ValueError(f"'{place}'은(는) 존재하지 않는 장소입니다.")

    return place
