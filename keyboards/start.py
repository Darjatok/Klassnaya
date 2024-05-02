from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton


kb_start_next = InlineKeyboardMarkup(inline_keyboard=[
    [
        InlineKeyboardButton(
            text='Вперед',
            callback_data='next')]])

kb_start_back = InlineKeyboardMarkup(inline_keyboard=[
    [
        InlineKeyboardButton(
             text='Назад',
             callback_data='back')]])