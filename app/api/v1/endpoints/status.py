from fastapi import APIRouter

router = APIRouter()


@router.get("")
@router.get("/")  # Add both route patterns to handle with and without trailing slash
async def get_status() -> dict[str, str]:
    """
    Health check endpoint to verify the API is running.
    """
    return {"status": "ok"}
