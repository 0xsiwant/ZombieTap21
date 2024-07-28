import asyncio
from logging import INFO, basicConfig

from aiogram import Bot, Dispatcher
from aiogram.types import BotCommand, MenuButtonWebApp, WebAppInfo

from handlers.start import StartCommand
from handlers.add_friend import AddFriendCommand
from config import TOKEN


class TelegramBot:
    def __init__(self):
        self.bot = Bot(token=TOKEN)
        self.dp = Dispatcher()

        self.start_command = StartCommand()
        add_friend_command = AddFriendCommand()
        self.dp.include_routers(add_friend_command.router_add_friend, self.start_command.router_start)

        self.command_list = [
            BotCommand(command="start", description="Start Bot 🤖"),
            BotCommand(command="add_friend", description="Add Friend ➕")
        ]

    async def run(self):
        await self.dp.start_polling(self.bot)
        await self.bot.set_my_commands(self.command_list)

        web_app_info = WebAppInfo(url=self.start_command.web_app_url)
        menu_button = MenuButtonWebApp(text="Open Web App", web_app=web_app_info)
        await self.bot.set_chat_menu_button(menu_button=menu_button)


if __name__ == "__main__":
    basicConfig(level=INFO)
    bot = TelegramBot()
    try:
        asyncio.run(bot.run())
    except KeyboardInterrupt:
        print("Close connection!")
