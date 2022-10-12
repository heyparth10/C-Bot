import os
import discord
from bot import BOT
import os
import time

intent = discord.Intents.default()
intent.members = True
intent.message_content = True
client = discord.Client(intents=intent)
bot = BOT()


async def my_background_task():
  await client.wait_until_ready()  # ensures cache is loaded
  channel = client.get_channel(1028930221660979253)
  message = []
  while not client.is_closed():
    message = bot.list_new_contests()
    if len(message) != 0:
      for i in range(len(message)):
        embedVar = message[i]
        await channel.send(embed = embedVar)
    #time.sleep(3600)


@client.event
async def on_ready():
  print('We have logged in as {0.user}'.format(client))


@client.event
async def on_message(message):
  if message.author == client.user:
    return

  if message.content.startswith('$SENDinfo'):
    await message.channel.send('Sending Contest info!')
    client.loop.create_task(my_background_task())


my_secret = os.environ['TOKEN']
client.run(my_secret)
