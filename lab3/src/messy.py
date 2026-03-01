import sys
from dataclasses import dataclass


def calc(x: int, y: int) -> int:
    return x + y


@dataclass
class Data:
    id: int
    name: str


def do_stuff(a: int | None, b: int, c: int | None = None) -> int:
    _ = c
    if a is None:
        a = 0
    return calc(a, b)


def main() -> int:
    data_obj = Data(1, "test")
    print(do_stuff(data_obj.id, 2))
    return 0


if __name__ == "__main__":
    sys.exit(main())
