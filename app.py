import streamlit as st
from ui import ResumeSkillApp   # comes from ui/__init__.py

if __name__ == "__main__":
    app = ResumeSkillApp()
    app.main()