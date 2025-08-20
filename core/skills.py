import re
import pandas as pd
from typing import Iterable, Set, List
from core.utils import TextNormalizer

try:
    from rapidfuzz import fuzz
    RAPIDFUZZ_AVAILABLE = True
except:
    RAPIDFUZZ_AVAILABLE = False


class SkillRepository:
    def __init__(self, base_skills: Iterable[str] | None = None):
        default_skills = {"python", "sql", "excel", "tableau", "aws", "java", "c++"}
        self._skills: Set[str] = set(s.casefold() for s in (base_skills or default_skills))

    def add_from_comma_text(self, value: str) -> None:
        for s in [x.strip() for x in value.split(",") if x.strip()]:
            self._skills.add(s.casefold())

    def add_from_csv_text(self, csv_text: str) -> None:
        df = pd.read_csv(io.StringIO(csv_text))
        for col in df.columns:
            for s in df[col].dropna().astype(str).tolist():
                self._skills.add(s.casefold())

    def get_all(self) -> Set[str]:
        return set(self._skills)


class SkillExtractor:
    def __init__(self, skills: Iterable[str], fuzzy_threshold: int = 0):
        self.skills: List[str] = sorted({s.casefold() for s in skills}, key=len, reverse=True)
        self.fuzzy_threshold = fuzzy_threshold

    def extract(self, raw_text: str) -> Set[str]:
        text = TextNormalizer.normalize(raw_text)
        found: Set[str] = set()

        for s in self.skills:
            if re.search(rf"(?<!\w){re.escape(s)}(?!\w)", text, flags=re.IGNORECASE):
                found.add(s)

        if self.fuzzy_threshold and RAPIDFUZZ_AVAILABLE:
            for s in self.skills:
                if s not in found and len(s) > 2:
                    score = fuzz.partial_ratio(s, text)
                    if score >= self.fuzzy_threshold:
                        found.add(s)
        return found