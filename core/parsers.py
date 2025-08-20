import io
from PyPDF2 import PdfReader

class FileReaders:
    @staticmethod
    def read_pdf(file_bytes: bytes) -> str:
        reader = PdfReader(io.BytesIO(file_bytes))
        return "\n".join([page.extract_text() or "" for page in reader.pages])

    @staticmethod
    def read_txt(file_bytes: bytes) -> str:
        return file_bytes.decode("utf-8", errors="ignore")

class ResumeParser:
    def parse(self, file_name: str, file_bytes: bytes) -> str:
        if file_name.lower().endswith(".pdf"):
            return FileReaders.read_pdf(file_bytes)
        elif file_name.lower().endswith(".txt"):
            return FileReaders.read_txt(file_bytes)
        return ""