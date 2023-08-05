import pycld2 as cld2


def detect_english(text: str | None) -> bool:
    if not text:
        return True

    _, _, _, detect_language = cld2.detect(text, returnVectors=True)
    return len(detect_language) == 1 and detect_language[0][2] == 'ENGLISH'
