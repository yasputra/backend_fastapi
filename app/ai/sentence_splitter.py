import re


def split_sentences(text: str) -> list[str]:
    sentences = re.split(r"[.!?]+", text)

    return [
        sentence.strip()
        for sentence in sentences
        if sentence.strip()
    ]