from fastapi import APIRouter
from app.api.endpoints import users_router, charity_project_router, donation_router

main_router = APIRouter()

main_router.include_router(
    charity_project_router,
    prefix='/charity_projects',
    tags=['Charity Projects']
)
main_router.include_router(
    donation_router,
    prefix='/donations',
    tags=['Donations']
)

main_router.include_router(users_router)
