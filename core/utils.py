import re

class TextNormalizer:
    @staticmethod
    def normalize(text: str) -> str:
        if not text:
            return ""
        text = text.casefold()
        text = re.sub(r"[^\w\s\+]", " ", text)
        text = re.sub(r"\s+", " ", text).strip()
        return text