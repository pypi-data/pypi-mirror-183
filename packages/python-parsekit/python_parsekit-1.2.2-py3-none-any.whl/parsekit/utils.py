from typing import Any, Iterable


def stringify(iterable: Iterable[Any]) -> Iterable[str]:
    for item in iterable:
        yield str(item) if item is not None else ""


def flatten(iterable: Iterable[Any]) -> Iterable[Any]:
    for item in iterable:
        if isinstance(item, list):
            yield from flatten(item)
        else:
            yield item


def filter(iterable: Iterable[Any]) -> Iterable[Any]:
    for item in iterable:
        if item:
            yield item
