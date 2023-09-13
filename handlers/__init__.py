from aiogram import Router

from filters import ChatPrivateFilter


def setup_routers() -> Router:
    from .users import start, back, category
    from .errors import error_handler
    
    router = Router()
    
    # Устанавливаем локальный фильтр, если нужно
    start.router.message.filter(ChatPrivateFilter(chat_type=["private"]))
    
    router.include_routers(start.router, back.router, category.router, error_handler.router)
    
    return router
