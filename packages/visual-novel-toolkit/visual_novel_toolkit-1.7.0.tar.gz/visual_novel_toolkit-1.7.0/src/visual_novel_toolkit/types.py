from typing import Protocol
from typing import TypeAlias
from typing import TypedDict


class YASpeller(TypedDict, total=False):
    dictionary: list[str]


class Item(TypedDict, total=False):
    word: str


class Items(TypedDict, total=False):
    data: list[Item]


Report: TypeAlias = list[tuple[bool, Items]]


class Words(Protocol):
    def get(self) -> list[str]:
        raise RuntimeError

    def set(self, value: list[str]) -> None:
        raise RuntimeError


class Form(Protocol):
    normal_form: str


class Analyzer(Protocol):
    def parse(self, content: str) -> list[Form]:
        raise RuntimeError
