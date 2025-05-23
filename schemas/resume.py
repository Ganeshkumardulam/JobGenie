from pydantic import BaseModel

class ResumeText(BaseModel):
    content: str