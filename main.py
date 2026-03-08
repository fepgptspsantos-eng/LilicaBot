import os
import discord
from discord.ext import commands

# Configurações para a Lilica ler as mensagens e gerenciar membros
intents = discord.Intents.default()
intents.message_content = True
intents.members = True

# O prefixo para os comandos nos seus clãs de Roblox e Polícia RP
bot = commands.Bot(command_prefix='!', intents=intents)

@bot.event
async def on_ready():
    print(f'Lilica tecnológica online como {bot.user}')

@bot.command()
async def lock(ctx):
    await ctx.channel.set_permissions(ctx.guild.default_role, send_messages=False)
    await ctx.send("🔒 Este canal foi trancado pela Lilica!")

@bot.command()
async def unlock(ctx):
    await ctx.channel.set_permissions(ctx.guild.default_role, send_messages=True)
    await ctx.send("🔓 Este canal foi liberado pela Lilica!")

# Seu Token oficial da Lilica inserido abaixo
bot.run(os.getenv('DISCORD_TOKEN'))


