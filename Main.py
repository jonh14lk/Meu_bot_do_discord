import discord
import asyncio
from random import randint
 
 
class MyClient(discord.Client):
    async def on_ready(self):
        print('Logged on as', self.user)
 
    async def on_message(self, message):
        # don't respond to ourselves
        if message.author == self.user:
            return
 
        if message.content == '!msg':
            num = randint(0,9)
            if num == 1:
                await message.channel.send('Mensagem')
            if num == 2:
                await message.channel.send('Mensagem')
            if num == 3:
                await message.channel.send('Mensagem')
            if num == 4:
                await message.channel.send('Mensagem')
            if num == 5:
                await message.channel.send('Mensagem')
            if num == 6:
                await message.channel.send('Mensagem')
            if num == 7:
                await message.channel.send('Mensagem')
            if num == 8:
                await message.channel.send('Mensagem')
            if num == 0:
                await message.channel.send('Mensagem')
            if num == 9:
                await message.channel.send('SMensagem')
 
 
 
 
client = MyClient()
 
 
 
client.run('TOKEN')
