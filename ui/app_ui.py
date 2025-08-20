from models import ResumeResult
from core import ResumeParser, SkillRepository, SkillExtractor, JDMatcher, ReportBuilder

import streamlit as st


class ResumeSkillApp:
    def __init__(self):
        st.set_page_config(page_title="Resume Skill Extractor", page_icon="🧠", layout="wide")
        self.parser = ResumeParser()

    def main(self):
        st.title("📄🔎 Resume Skill Extractor")
        st.caption("Upload resumes and job-required skills to check skill match.")

        uploaded_resumes = st.file_uploader("Upload resumes (PDF/TXT)", type=["pdf","txt"], accept_multiple_files=True)
        jd_text = st.text_area("Enter Job Skills (comma-separated)", height=100)

        process = st.button("▶ Extract & Match", type="primary")

        if process:
            if not uploaded_resumes or not jd_text.strip():
                st.warning("Upload resumes and enter job skills first.")
                return

            required_skills = [s.strip() for s in jd_text.split(",") if s.strip()]
            skill_repo = SkillRepository()
            extractor = SkillExtractor(skill_repo.get_all())

            results = []
            for f in uploaded_resumes:
                raw_text = self.parser.parse(f.name, f.read())
                extracted = extractor.extract(raw_text)
                matched, missing, match_percent, match_count, req_count = JDMatcher.compare(extracted, required_skills)

                results.append(
                    ResumeResult(
                        resume_name=f.name,
                        extracted_skills=list(extracted),
                        missing_skills=missing,
                        match_percent=match_percent,
                        match_count=match_count,
                        required_count=req_count
                    )
                )

            df = ReportBuilder.make_dataframe(results)
            st.dataframe(df, use_container_width=True)
            st.download_button("Download CSV", ReportBuilder.to_csv_bytes(df), "report.csv", "text/csv")