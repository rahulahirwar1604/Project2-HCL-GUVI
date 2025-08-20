import pandas as pd
from models.resume_result import ResumeResult

class ReportBuilder:
    @staticmethod
    def make_dataframe(results):
        rows = []
        for r in results:
            rows.append({
                "Resume": r.resume_name,
                "Extracted Skills": ", ".join(sorted(r.extracted_skills)),
                "Missing Skills": ", ".join(sorted(r.missing_skills)),
                "Match %": r.match_percent,
                "Matched/Required": f"{r.match_count}/{r.required_count}",
            })
        return pd.DataFrame(rows)

    @staticmethod
    def to_csv_bytes(df: pd.DataFrame) -> bytes:
        return df.to_csv(index=False).encode("utf-8")