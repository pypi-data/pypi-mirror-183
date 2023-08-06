import pydantic

__all__ = (
    'BaseResponse',
)


class BaseResponse(pydantic.BaseModel):
    success: bool

