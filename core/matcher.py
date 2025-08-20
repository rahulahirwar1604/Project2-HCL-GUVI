from typing import Iterable, List, Tuple

class JDMatcher:
    @staticmethod
    def compare(extracted: Iterable[str], required_skills: Iterable[str]) -> Tuple[List[str], List[str], float, int, int]:
        extracted_set = {s.casefold() for s in extracted}
        required_set = {s.strip().casefold() for s in required_skills if s.strip()}
        matched = sorted(extracted_set.intersection(required_set))
        missing = sorted(required_set.difference(extracted_set))
        req_count = max(len(required_set), 1)
        match_count = len(matched)
        match_percent = round((match_count / req_count) * 100.0, 2)
        return matched, missing, match_percent, match_count, req_count