import os
from fastapi import APIRouter, HTTPException, Request
from .utils import validate_single_key
from .services import math_service
from .services.ai_service import ask_ai

router = APIRouter()


@router.get("/health")
def health():
    return {
        "is_success": True,
        "official_email": os.getenv("EMAIL")
    }


@router.post("/bfhl")
async def bfhl(request: Request):
    try:
        body = await request.json()

        if not validate_single_key(body):
            raise HTTPException(status_code=400, detail="Exactly one key required")

        key = list(body.keys())[0]
        value = body[key]

        if key == "fibonacci":
            result = math_service.fibonacci(value)

        elif key == "prime":
            result = math_service.primes(value)

        elif key == "lcm":
            result = math_service.lcm(value)

        elif key == "hcf":
            result = math_service.hcf(value)

        elif key == "AI":
            result = await ask_ai(value)

        else:
            raise HTTPException(status_code=400, detail="Invalid key")

        return {
            "is_success": True,
            "official_email": os.getenv("EMAIL"),
            "data": result
        }

    except HTTPException as e:
        raise e
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))
    except Exception:
        raise HTTPException(status_code=500, detail="Internal server error")
