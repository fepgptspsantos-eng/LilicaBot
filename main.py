import os
import discord
from discord.ext import commands
from discord import app_commands # Nova biblioteca para os comandos /

# Configurações de Intents
intents = discord.Intents.default()
intents.message_content = True
intents.members = True

# Criando o Bot
class MinhaLilica(commands.Bot):
    def __init__(self):
        super().__init__(command_prefix="!", intents=intents)

    async def setup_hook(self):
        # Isso sincroniza os comandos / com o Discord
        await self.tree.sync()
        print("Comandos de barra sincronizados!")

bot = MinhaLilica()

@bot.event
async def on_ready():
    print(f'Lilica tecnológica online como {bot.user}')

# Comando de Barra: /lock
@bot.tree.command(name="lock", description="Tranca o canal atual")
async def lock(interaction: discord.Interaction):
    await interaction.channel.set_permissions(interaction.guild.default_role, send_messages=False)
    await interaction.response.send_message("🔒 Este canal foi trancado pela Lilica!")

# Comando de Barra: /unlock
@bot.tree.command(name="unlock", description="Libera o canal atual")
async def unlock(interaction: discord.Interaction):
    await interaction.channel.set_permissions(interaction.guild.default_role, send_messages=True)
    await interaction.response.send_message("🔓 Este canal foi liberado pela Lilica!")

# Rodando o bot com o seu Token da Railway
bot.run(os.getenv('DISCORD_TOKEN'))

