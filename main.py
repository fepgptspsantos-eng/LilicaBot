import os
import discord
import asyncio
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

# Função para rodar o bot com proteção contra o erro 429
async def main():
    try:
        await bot.start(os.getenv('DISCORD_TOKEN'))
    except discord.errors.HTTPException as e:
        if e.status == 429:
            print("O Discord bloqueou o acesso temporariamente (Erro 429).")
        else:
            raise e

if __name__ == "__main__":
    asyncio.run(main())
    
