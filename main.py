import os
import discord
from discord.ext import commands, tasks
from discord import app_commands
from datetime import datetime

# Configurações de Intents
intents = discord.Intents.default()
intents.message_content = True
intents.members = True

class MinhaLilica(commands.Bot):
    def __init__(self):
        super().__init__(command_prefix="!", intents=intents)

    async def setup_hook(self):
        self.saudacao_automatica.start() 
        await self.tree.sync()
        print("Lilica atualizada: Lock, Unlock, Ban e Automação prontos!")

bot = MinhaLilica()

# --- 1. AUTOMAÇÃO DE SAUDAÇÃO ---
ID_DO_CANAL = 1476747962364465234 

@tasks.loop(minutes=1)
async def saudacao_automatica():
    canal = bot.get_channel(ID_DO_CANAL)
    if not canal: return
    agora = datetime.now()
    if agora.minute == 0:
        if agora.hour == 8:
            await canal.send("☀️ **Bom dia!** A Lilica acordou para o RP!")
        elif agora.hour == 13:
            await canal.send("🌤️ **Boa tarde!** Lilica online e vigilante!")
        elif agora.hour == 19:
            await canal.send("🌙 **Boa noite!** Bom descanso a todos!")

# --- 2. COMANDOS DE BARRA (RECUPERADOS) ---

@bot.tree.command(name="lock", description="Tranca o canal")
@app_commands.checks.has_permissions(manage_channels=True)
async def lock(interaction: discord.Interaction):
    await interaction.channel.set_permissions(interaction.guild.default_role, send_messages=False)
    await interaction.response.send_message("🔒 Canal trancado!")

@bot.tree.command(name="unlock", description="Libera o canal")
@app_commands.checks.has_permissions(manage_channels=True)
async def unlock(interaction: discord.Interaction):
    await interaction.channel.set_permissions(interaction.guild.default_role, send_messages=True)
    await interaction.response.send_message("🔓 Canal liberado!")

@bot.tree.command(name="ban", description="Bane um usuário")
@app_commands.checks.has_permissions(ban_members=True)
async def ban(interaction: discord.Interaction, membro: discord.Member, motivo: str = "Não informado"):
    await membro.ban(reason=motivo)
    await interaction.response.send_message(f"🔨 {membro.name} banido: {motivo}")

# --- 3. EVENTOS E HISTÓRICO ---

@bot.event
async def on_ready():
    print(f'Lilica online como {bot.user}')

@bot.event
async def on_message(message):
    if message.author == bot.user: return
    print(f"LOG: [{message.channel}] {message.author}: {message.content}")
    await bot.process_commands(message)

bot.run(os.getenv('DISCORD_TOKEN'))

