from loader import load_json

aliases = load_json("aliases.json")


def normalize_place(place: str) -> str:
    place = place.strip()

    return aliases.get(place, place)


def print_path(path: list[str]) -> None:
    print("\n최적 경로")

    for place in path[:-1]:
        print(f"{place}")
        print("↓")

    print(path[-1])
