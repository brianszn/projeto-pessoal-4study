from fastapi import APIRouter

router = APIRouter()

@router.get('/', response_model=None)
async def root():
    return {'message': 'Hello World'}