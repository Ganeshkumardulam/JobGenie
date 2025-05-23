from fastapi import Request
from fastapi.responses import JSONResponse
from exceptions.custom_exceptions import ResumeParsingError

async def resume_parsing_exception_handler(request: Request, exc: ResumeParsingError):
    return JSONResponse(
        status_code=400,
        content={"message": f"Resume parsing error: {exc.message}"},
    )
