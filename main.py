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
        self.saudacao_automatica.start() # Inicia a vigília do relógio
        await self.tree.sync()
        print("Comandos e Automação da Lilica prontos!")

bot = MinhaLilica()

# --- AUTOMAÇÃO DE SAUDAÇÃO ---
ID_DO_CANAL = 1476747962364465234 # O ID que você me mandou!

@tasks.loop(minutes=1) # Checa a cada minuto para não perder o horário
async def saudacao_automatica():
    canal = bot.get_channel(ID_DO_CANAL)
    if not canal:
        return

    agora = datetime.now()
    hora = agora.hour
    minuto = agora.minute

    # Configurado para mandar exatamente no minuto 00 de cada turno
    if hora == 8 and minuto == 0:
        await canal.send("☀️ **Bom dia, gente tecnológica!** A Lilica acabou de acordar para o RP!")
    elif hora == 13 and minuto == 0:
        await canal.send("🌤️ **Boa tarde!** Passando para lembrar que a Lilica está de olho no chat!")
    elif hora == 19 and minuto == 0:
        await canal.send("🌙 **Boa noite!** O chicote come, mas a Lilica deseja um ótimo descanso a todos!")

# --- COMANDOS DE BARRA (/) ---

@bot.tree.command(name="lock", description="Tranca o canal atual")
@app_commands.checks.has_permissions(manage_channels=True)
async def lock(interaction: discord.Interaction):
    await interaction.channel.set_permissions(interaction.guild.default_role, send_messages=False)
    await interaction.response.send_message("🔒 Este canal foi trancado pela Lilica!")

@bot.tree.command(name="unlock", description="Libera o canal atual")
@app_commands.checks.has_permissions(manage_channels=True)
async def unlock(interaction: discord.Interaction):
    await interaction.channel.set_permissions(interaction.guild.default_role, send_messages=True)
    await interaction.response.send_message("🔓 Este canal foi liberado pela Lilica!")

@bot.tree.command(name="ban", description="Bane um usuário")
@app_commands.checks.has_permissions(ban_members=True)
async def ban(interaction: discord.Interaction, membro: discord.Member, motivo: str = "Não informado"):
    await membro.ban(reason=motivo)
    await interaction.response.send_message(f"🔨 O usuário {membro.name} foi banido por: {motivo}")

# --- EVENTOS ---

@bot.event
async def on_ready():
    print(f'Lilica tecnológica online como {bot.user}')

@bot.event
async def on_message(message):
    if message.author == bot.user:
        return
    # Mostra o que o povo fala nos Logs da Railway
    print(f"HISTÓRICO: [{message.channel}] {message.author}: {message.content}")
    await bot.process_commands(message)

bot.run(os.getenv('DISCORD_TOKEN'))
