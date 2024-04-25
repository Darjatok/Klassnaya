import asyncio

from aiogram import Bot, Dispatcher, Router, F
from aiogram.types import Message, BotCommand, InlineKeyboardButton, ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardMarkup, CallbackQuery
from aiogram.filters import Command
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import State, StatesGroup

bot = Bot(token="7028205352:AAEUzZzpdJHlLDoabeQUvCSRIR8u99aREdM")
dp = Dispatcher()
router = Router()

@router.message(Command("start"))
async def start_handler(msg: Message):
    await bot.set_my_commands([
            BotCommand(command="start", description="Начало работы"),
            BotCommand(command="new_game", description="Начало игры"),
            BotCommand(command="delete", description="Отчислиться")
    ]) 

    inline_markup = InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton(text='Вперёд', callback_data='next')]
    ])
    await msg.answer(text='Страница 1', reply_markup=inline_markup)
@router.callback_query(F.data == 'next')
async def next_handler(callback_query: CallbackQuery):
    inline_markup = InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton(text='Назад', callback_data='back')]
    ])
    await callback_query.message.edit_text(
        text='Страница 2',
        reply_markup=inline_markup)

@router.callback_query(F.data == 'back')
async def next_handler(callback_query: CallbackQuery):
    inline_markup = InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton(text='Вперёд', callback_data='next')]
    ])
    await callback_query.message.edit_text(
        text='Страница 1',
        reply_markup=inline_markup)



async def main():
    await dp.start_polling(bot)
 

dp.include_routers(router)

if __name__ == '__main__':
    asyncio.run(main())
