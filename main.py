from src.pathfinder import find_path
from src.utils import print_path
from src.validator import validate_place


def main():
    print("=" * 40)
    print(" " * 5, "학교 최적 경로 탐색 프로그램")
    print("=" * 40)

    while True:
        try:
            start = input("\n출발지 (exit 입력 시 종료): ").strip()

            if start.lower() == "exit":
                print("\n프로그램을 종료합니다.")
                break

            goal = input("목적지 (exit 입력 시 종료): ").strip()

            if goal.lower() == "exit":
                print("\n프로그램을 종료합니다.")
                break

            start = validate_place(start)
            goal = validate_place(goal)
            path, cost = find_path(start, goal)

            print()
            print_path(path, cost)

        except ValueError as e:
            print(f"\n오류: {e}")

        except KeyboardInterrupt:
            print("\n\n프로그램을 종료합니다.")
            break

        except Exception as e:
            print(f"\n예상치 못한 오류가 발생했습니다.\n{e}")


if __name__ == "__main__":
    main()
