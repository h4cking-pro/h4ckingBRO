"""Archivo principal del bot."""

__version__ = "0.0.1"

import json

import discord
from discord.ext import commands

from logs.logger import logger

# Configuracion.
with open("config.json", encoding="utf-8") as file:
    config = json.load(file)


class Bot(commands.Bot):
    """Clase principal del bot."""

    def __init__(self):
        """Inicializar el bot."""
        intents = discord.Intents.default()
        intents.members = True
        intents.guilds = True
        self.version = __version__
        self.chunk_at_startup = False

        super().__init__(config["PREFIX"],
                         token=config["TOKEN"],
                         description="H4ckingBRO - Bot para el servidor de H4ckingPRO",
                         intents=intents,
                         application_id=config["APPLICATION_ID"])

    async def on_ready(self):
        """Informacion del bot al iniciar."""
        logger.info("Bot %s conectado a %s servidores",
                    self.user.name,
                    len(self.guilds))

    async def setup_hook(self):
        """Carga y sincroniza los comandos"""
        await self.load_extension("cogs.misc")
        await self.tree.sync()

    async def on_command_error(self, ctx, error):
        """Log de errores."""
        logger.error(f"{ctx.message.author} in {ctx.message.guild}", exc_info=error)
        if isinstance(error, discord.ext.commands.errors.CommandNotFound):
            await ctx.send("```El bot usa SLASH COMMANDS```\n```Usa /help para ver los comandos```")
        if isinstance(error, discord.ext.commands.errors.MissingRequiredArgument):
            await ctx.send("```" + str(error) + "```"
                           + "```Usa /help para ver los comandos```")
        if isinstance(error, commands.BadArgument):
            await ctx.send("```" + str(error) + "```"
                           + "```Usa /help para ver los comandos```")


if __name__ == "__main__":
    h4ckingBRO = Bot()
    h4ckingBRO.run(config["TOKEN"])
