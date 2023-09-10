from aiogram import Router
from router.user import router as user_router

router = Router()

router.include_routers(user_router)