from fastapi import APIRouter

router = APIRouter()

@router.get("/")
def list_available_skills():
    return {
        "skills": [
            "Python", "FastAPI", "PostgreSQL", "DSA", "AWS", "React", "Docker"
        ]
    }