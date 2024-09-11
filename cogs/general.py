from helper import get_markup, get_capacity

import discord
from discord.ext import commands
from discord.ext.commands import Context

# Here we name the cog and create a new class for the cog.
class General(commands.Cog, name="general"):
    def __init__(self, bot) -> None:
        self.bot = bot

    @commands.hybrid_command(
        name="now",
        description="Get the class capacity now",
    )
    async def now(self, context: Context) -> None:
        new_value = get_capacity(get_markup(self.bot.url), self.bot.code)
        await context.send(f"Currently: {new_value}\nPreviously: {self.bot.value}")
        self.bot.value = new_value

    @commands.hybrid_command(
        name="change",
        description="Change URL and class code to check",
    )
    async def change(self, context: Context, url: str, code: str) -> None:
        _,_,url = url.partition(':')
        _,_,code = code.partition(':')
        self.bot.url = str(url)
        self.bot.code = str(code)
        self.bot.value = get_capacity(get_markup(url), code)
        await context.send(f"Changed to:\nURL: {self.bot.url}\nCode: {self.bot.code}\nAnd currently, the value is {self.bot.value}.")

    @commands.hybrid_command(
        name="register",
        description="Register a new channelID (only works in server)",
    )
    async def register(self, context: Context, channel_id: str) -> None:
        _,_,channel_id = channel_id.partition(':')
        if channel_id:
            self.bot.channels.add(channel_id)
            await context.send(f"Registered the channel ID {channel_id} for updates")

# And then we finally add the cog to the bot so that it can load, unload, reload and use it's content.
async def setup(bot) -> None:
    await bot.add_cog(General(bot))