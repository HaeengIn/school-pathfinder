from src.loader import load_json

nodes = load_json("nodes.json")
aliases = load_json("aliases.json")


def normalize_place(place: str) -> str:
    place = place.strip()
    return aliases.get(place, place)


def print_path(path: list[str], cost: int) -> None:
    print("=" * 40)
    print(" " * 11, "=== 최적경로 ===")
    print("=" * 40)

    for i, place in enumerate(path):
        floor = nodes[place]["floor"]
        print(f"{place} ({floor}층)")

        if i != len(path) - 1:
            print("↓")

    print()
    print(f"총 이동 비용 : {cost}")
