from collections.abc import Callable, Iterable, Iterator
import string
from typing import Union, overload


def _extract_pin(
    poem: str,
    fallback: str = "0",
    index_fn: Callable[[int], int] = lambda i: i,
    strip_punctuation: bool = False,
) -> str:
    digits: list[str] = []
    for line_index, line in enumerate(poem.splitlines()):
        words = line.split()
        target_idx = index_fn(line_index)

        if 0 <= target_idx < len(words):
            word = words[target_idx]
            if strip_punctuation:
                word = word.strip(string.punctuation)
            digits.append(str(len(word)))
        else:
            digits.append(fallback)

    return "".join(digits)


@overload
def pin_extractor(
    poems: str,
    *,
    fallback: str = ...,
    index_fn: Callable[[int], int] = ...,
    strip_punctuation: bool = ...,
) -> str: ...


@overload
def pin_extractor(
    poems: Iterable[str],
    *,
    fallback: str = ...,
    index_fn: Callable[[int], int] = ...,
    strip_punctuation: bool = ...,
) -> Iterator[str]: ...


def pin_extractor(
    poems: Union[str, Iterable[str]],
    *,
    fallback: str = "0",
    index_fn: Callable[[int], int] = lambda i: i,
    strip_punctuation: bool = False,
) -> Union[str, Iterator[str]]:
    if isinstance(poems, str):
        return _extract_pin(
            poems,
            fallback=fallback,
            index_fn=index_fn,
            strip_punctuation=strip_punctuation,
        )

    return (
        _extract_pin(
            poem,
            fallback=fallback,
            index_fn=index_fn,
            strip_punctuation=strip_punctuation,
        )
        for poem in poems
    )