import asyncio
from aiogram import Bot, Dispatcher, types
from aiogram.enums import ParseMode
from aiogram.client.default import DefaultBotProperties
from aiogram.filters import Command
from background import keep_alive

TOKEN = "8195530369:AAF6icdaf76w38rRUfuetDRNYDzuqPYB_QI"
ADMIN_IDS = [969783208,7213947960]

bot = Bot(
    token=TOKEN,
    default=DefaultBotProperties(parse_mode=ParseMode.HTML)
)
dp = Dispatcher()

WELCOME_MESSAGE = """
👋 <b>Привет, {name}!</b>

Я бот флуда. Вот наше инфо: https://t.me/infochannelgenshinfludd

📌 <i>Просто напиши роль которую ты хочешь, а так же когда у тебя день рождения(для внесения в инфо) и переходи по данной ссылке:https://t.me/+bjlQJT5cBk02ZjAy    </i>
"""


@dp.message(Command("start", "help"))
async def cmd_start(message: types.Message):
    await message.answer(
        WELCOME_MESSAGE.format(name=message.from_user.full_name),
        disable_web_page_preview=True
    )


@dp.message()
async def forward_to_admins(message: types.Message):
    user = message.from_user
    admin_text = (

        f"📩 <b>Новое сообщение</b>\n"
        f"От: @{user.username} (<code>{user.id}</code>)\n"
        f"Имя: {user.full_name}\n\n"
        f"Текст: <i>{message.text}</i>"
    )

    for admin_id in ADMIN_IDS:
        await bot.send_message(admin_id, admin_text)

    await message.answer("✅ Ваше сообщение отправлено администраторам")


async def main():
    await dp.start_polling(bot)

keep_alive()
if __name__ == "__main__":
    asyncio.run(main())