from fastapi import APIRouter, UploadFile, File, HTTPException
from parser.resume_parser import parse_resume

router = APIRouter()

@router.post("/upload")
def upload_resume(file: UploadFile = File(...)):
    try:
        content = parse_resume(file)
        return {"parsed_resume": content}
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))