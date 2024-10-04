from discord.ext import commands
from discord.ext.commands import Cog, Context

from src.bot import Orion


class Ping(Cog):
    def __init__(self, bot: Orion) -> None:
        self.bot = bot

    @commands.hybrid_command(
        name="ping", description="Returns Orion's latency/ping in ms"
    )
    async def ping(self, ctx: Context) -> None:
        await ctx.reply(
            f"Pong!\n``{round((self.bot.latency * 1000), 2)}`` ms", ephemeral=True
        )


async def setup(bot: Orion) -> None:
    await bot.add_cog(Ping(bot))
