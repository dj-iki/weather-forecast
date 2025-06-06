from fastapi import APIRouter, status, Depends
from ..dependencies.dummy import get_print_dummy

router = APIRouter(
    prefix="/dummy",
    tags=["dummy"],
)


@router.get("/", status_code=status.HTTP_200_OK)
def dummy(print_dummy=Depends(get_print_dummy)):
    return {"message": print_dummy()}
