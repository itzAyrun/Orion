import os
from typing import List

import discord
from discord.ext import commands

from config import settings

class Orion(commands.Bot):
    def __init__(self) -> None:
        super().__init__(
            command_prefix=self._prefix_callable,
            intents=discord.Intents.all(),
            help_command=None,
            strip_after_prefix=settings.commands.strip_after_prefix,
            case_insensitive=settings.commands.case_insensitive,
        )

    async def load_extensions(self) -> None:
        for filename in os.listdir("src/extensions"):
            if filename in ["__pycache__", "__init__.py"]:
                continue  # ignore

            else:
                # filename[:-3] = file name without .py extension
                await self.load_extension(f"src.extensions.{filename[:-3]}")

    async def setup_hook(self) -> None:
        await self.load_extensions()
        await self.tree.sync()

    async def on_ready(self) -> None:
        print(f"Logged in as {self.user}")
    
    @staticmethod
    async def _prefix_callable(*_) -> List[str]:
        settings.reload()
        if settings.bot.prefix is None:
            return ["?"]

        return settings.bot.prefix
