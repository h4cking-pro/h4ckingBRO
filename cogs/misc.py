"""Comandos miscelaneos."""

import discord
import psutil
from discord import app_commands
from discord.ext import commands

from logs.logger import logger


class Misc(commands.Cog):
    """Clase para comandos miscelaneos"""

    def __init__(self, bot: commands.Bot):
        self.bot = bot

    # end def

    ####################################################################################################################
    @app_commands.command(name="info", description="ℹ️ Info del bot ℹ️")
    async def info(self, interaction: discord.Interaction):
        try:
            servers = len(self.bot.guilds)

            members = 0
            for guild in self.bot.guilds:
                members += guild.member_count

            channels = 0
            for guild in self.bot.guilds:
                for text_channels in guild.text_channels:
                    channels += 1

            embed = discord.Embed(title=":information_source: __**INFORMACION**__ :information_source:")
            embed.add_field(name=":earth_americas: **Servidores** :earth_americas:", value=f"Serving {servers} servers",
                            inline=False)
            embed.add_field(name=":busts_in_silhouette: **Usado por**:busts_in_silhouette: ",
                            value=f"Usado por {members} personas", inline=False)
            embed.add_field(name=":satellite: **CANALES** :satellite:", value=f"{channels}", inline=False)
            embed.add_field(name=":gear: **Version** :gear:", value=f"{self.bot.version}", inline=False)
            embed.add_field(name=":bar_chart: **USO DEL VPS** :bar_chart:",
                            value=f"CPU: {psutil.cpu_percent()}% RAM: {psutil.virtual_memory()[2]}%", inline=False)
            try:
                await interaction.response.send_message(embed=embed)
            except Exception as e:
                logger.exception(f"Failed to send info embed: {e}")
        except Exception as e:
            logger.exception(f"Failed to send info command: {e}")

    @app_commands.command(name="help",
                          description="help command")
    async def help_command(self, interaction: discord.Interaction):
        try:
            misc = (
                "`/info` => Información del bot. "
                "\n`/help` => Muestra este comando")

            embed = discord.Embed(title="__**Lista de comandos**__", color=0xf77e33)
            embed.add_field(name=":balloon:  Misc  :balloon:", value=misc, inline=False)

            await interaction.response.send_message(embed=embed)
        except Exception as e:
            logger.exception(f"{interaction.user.name}  intento usar /help pero fallo\n{e}")


async def setup(bot: commands.Bot):
    await bot.add_cog(
        Misc(bot)
    )
