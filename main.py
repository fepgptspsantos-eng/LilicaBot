# ... (mantenha o topo do código igual ao anterior)

# Comando de Barra: /ban
@bot.tree.command(name="ban", description="Bane um usuário do servidor")
@app_commands.checks.has_permissions(ban_members=True)
async def ban(interaction: discord.Interaction, membro: discord.Member, motivo: str = "Não informado"):
    await membro.ban(reason=motivo)
    await interaction.response.send_message(f"🔨 O usuário {membro.name} foi banido por: {motivo}")

# Sistema de Histórico (Vigiar conversas)
@bot.event
async def on_message(message):
    if message.author == bot.user:
        return
    
    # Isso imprime no console da Railway tudo o que o povo fala
    print(f"[{message.channel}] {message.author}: {message.content}")
    
    # Se quiser salvar num arquivo de texto na Railway:
    with open("historico.txt", "a", encoding="utf-8") as f:
        f.write(f"{message.created_at} - {message.author}: {message.content}\n")

    await bot.process_commands(message)

# ... (mantenha o bot.run lá no final)

