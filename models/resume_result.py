from dataclasses import dataclass
from typing import List

@dataclass
class ResumeResult:
    resume_name: str
    extracted_skills: List[str]
    missing_skills: List[str]
    match_percent: float
    match_count: int
    required_count: int