import discord
from discord import app_commands
import os

dc_token = os.environ['token']  #Token do Discord
id_do_servidor = os.environ['server_id']  #ID do servidor


class client(discord.Client):

  def __init__(self):
    super().__init__(intents=discord.Intents.default())
    self.synced = False  #para o bot não sincronizar os comandos mais de uma vez

  async def on_ready(self):
    await self.wait_until_ready()
    if not self.synced:  #Checar se os comandos slash foram sincronizados
      await tree.sync(guild=discord.Object(id=id_do_servidor))
      self.synced = True
    print(f"Entramos como {self.user}.")


aclient = client()
tree = app_commands.CommandTree(aclient)


@tree.command(guild=discord.Object(id=id_do_servidor),
              name='convite',
              description='Convite do Servidor')
async def slash2(interaction: discord.Interaction):
  await interaction.response.send_message(
    f"Use esse link para convidar seus amigos: https://discord.gg/PW3hzcU8hv",
    ephemeral=True)


@tree.command(guild=discord.Object(id=id_do_servidor),
              name='ajuda',
              description='Pedir ajuda')
async def slash3(interaction: discord.Interaction):
  await interaction.response.send_message(
    f"Confira o canal <#1050558128527249458> para saber mais sobre o servidor, ou entre em contato com a equipe de suporte <#1051304909741502504>",
    ephemeral=True)


@tree.command(guild=discord.Object(id=id_do_servidor),
              name='regras',
              description='Canal de Regras.')
async def slash4(interaction: discord.Interaction):
  await interaction.response.send_message(
    f"Confira o canal <#1025086181244932226>", ephemeral=True)


aclient.run(dc_token)
