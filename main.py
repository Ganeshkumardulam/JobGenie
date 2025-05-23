from fastapi import FastAPI
from routes import interview, resume, skills
from fastapi.middleware.cors import CORSMiddleware
from middlewares.error_handler import resume_parsing_exception_handler
from exceptions.custom_exceptions import ResumeParsingError



app = FastAPI(title="JobGenie - AI Interview Simulator")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(interview.router, prefix="/interview", tags=["Interview"])
app.include_router(resume.router, prefix="/resume", tags=["Resume"])
app.include_router(skills.router, prefix="/skills", tags=["Skills"])
app.add_exception_handler(ResumeParsingError, resume_parsing_exception_handler)

@app.get("/")
def read_root():
    return {"message": "Welcome to JobGenie - AI Interview Simulator"}