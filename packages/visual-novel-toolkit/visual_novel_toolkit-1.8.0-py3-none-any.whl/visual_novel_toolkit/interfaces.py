from typing import Protocol


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
