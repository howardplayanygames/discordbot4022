import discord
from discord.ext import commands
from core.classes import Cog_Extension
import json
import random

with open('setting.json', 'r', encoding='utf8') as jfile:
    jdata = json.load(jfile)


class Main(Cog_Extension):

    @commands.command()
    async def ping(self, ctx):
       await ctx.send(f'{round(self.bot.latency*1000)} (ms)')

    @commands.command()
    async def say(self, ctx, *,msg):
       await ctx.message.delete()
       await ctx.send(msg)
      
    @commands.command()
    async def clean(self, ctx, num : int):
       await ctx.channel.purge(limit=num+1)

    @commands.command()
    async def rand_squad(self,ctx):
      online = []
      for member in ctx.guild.members:
        if str(member.status) == 'online'and member.bot == False:
           online.append(member.name)

      random_online = random.sample(online, k=12)

      for squad in range(3):
        a = random.sample(random_online, k=4)
        await ctx.send(f"{squad+1}小隊:" + str(a))
        for name in a:
          random_online.remove(name)



    @commands.command()
    async def test(self, ctx):
      embed=discord.Embed(title='機器人資訊', color=0x12d3d0)
      embed.set_author(name='製作人 HowardPlaygames, url=http://www.youtube.com/channel/UC3bUWrwHKKRaT_qfUJ_qbfQ, icon_url=https://cdn.discordapp.com/attachments/1044907781368598598/1052523411806617672/roblox.png')
      embed.set_thumbnail('url=http://cdn.discordapp.com/attachments/1044907781368598598/1052521962204844062/mc.png')
      embed.add_field(name="機器人狀態", value='目前處於開發階段', inline=False)
      embed.add_field(name="能使用的功能", value= 'ping'  'rand__squad'  'pic'  'url__pic'  'help', inline=False)
      embed.add_field(name="使用前注意事項", value=   "rand_squad只有在成員滿時才能用(不包含機器人)", inline=False)
      embed.set_footer(text="祝你使用愉快")
      await ctx.send(embed=embed)


    #@commands.command()
    #async def codetest(self, ctx):
      #pass

    #@codetest.command()
    #async def python(self, ctx):
      #await ctx.send("python")
      
    #@codetest.command()
    #async def javascript(self, ctx):
      #await ctx.send("ajava")

    #@codetest.command()
    #async def cpp(self, ctx):
      #await ctx.send("c++")


def setup(bot):
   bot.add_cog(Main(bot))