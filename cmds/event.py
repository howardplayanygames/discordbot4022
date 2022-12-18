import discord
from discord.ext import commands
from core.classes import Cog_Extension
import json

with open('setting.json', 'r', encoding='utf8') as jfile:
    jdata = json.load(jfile)

class Event(Cog_Extension):
   @commands.Cog.listener()
   async def on_member_join(self, member):
    channel = self.bot.get_channel(int(jdata['Join_channel']))
    await channel.send(f'{member} join!')

   @commands.Cog.listener()
   async def on_member_remove(self, member):
    channel = self.bot.get_channel(int(jdata['Leave_channel']))
    await channel.send(f'{member} leave!')

   @commands.Cog.listener()
   async def on_message(self, msg):
      keyword = ('hi', 'HI', '安安', '有人嗎?', '嗨')
      if msg.content in keyword and msg.author != self.bot.user:
         await msg.channel.send('hi')

   

def setup(bot):
   bot.add_cog(Event(bot))