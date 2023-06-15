from fastapi import APIRouter, Request

from dto.token_dto import TokenDto

TOKEN_ENDPOINT: str = "/{tenant_id}/oauth2/token"

router: APIRouter = APIRouter()


@router.post(TOKEN_ENDPOINT)
async def get_auth_token(request: Request) -> TokenDto:
    resource_name = await request.form()
    return TokenDto(resource_name["resource"])
