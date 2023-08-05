from json import loads
from pathlib import Path

from httpx import AsyncClient
from pymorphy2 import MorphAnalyzer

from .types import Analyzer
from .types import Report
from .words import FileWords


async def proofread_words() -> None:
    mistakes = load_mistakes()
    if not mistakes:
        return

    words = set()
    morph: Analyzer = MorphAnalyzer()

    async with AsyncClient() as client:
        for mistake in mistakes:
            normal = morph.parse(mistake)[0].normal_form
            response = await client.get(f"https://ru.wiktionary.org/wiki/{normal}")
            if response.status_code == 200:
                words.add(mistake)

    if not words:
        return

    file_words = FileWords(Path("wiktionary.json"))
    dictionary = file_words.get()
    dictionary.extend(words)
    dictionary.sort()
    file_words.set(dictionary)


def load_mistakes() -> set[str]:
    json_file = Path("yaspeller_report.json")
    if not json_file.exists():
        return set()

    content = json_file.read_text()
    report: Report = loads(content)

    return {item["word"] for each in report for item in each[1]["data"]}


@classmethod  # type: ignore[misc, no-untyped-def]
def _fix(cls):
    if cls.__init__ is object.__init__:  # type: ignore[misc]
        return []  # type: ignore[misc]
    import inspect

    args = inspect.getfullargspec(cls.__init__)[0]  # type: ignore[misc]
    return sorted(args[1:])  # type: ignore[misc]


import pymorphy2.units.base  # noqa: E402

pymorphy2.units.base.BaseAnalyzerUnit._get_param_names = _fix  # type: ignore[misc]
