import discord
from discord.ext.commands import Bot
from discord.ext import commands
import asyncio
import time
import random
import datetime
import sqlite3

coinconn = sqlite3.connect('coinStorage.db')
c = coinconn.cursor()


Client = discord.Client()
client = commands.Bot(command_prefix = "?")

chat_filter = ["NIG", "NIGGER", "NIGGA", "N1GG3R", "JEW", "JEWS"]
bypass_list = [" "]


@client.event
async def on_ready():
  print("Management || Bot is Online and ready.")
  await client.change_presence(game=discord.Game(name="EastVeiw Management | ?help"))


invBlacklist = []

numOfMessages = 0

@client.event
async def on_member_join(member):
  role = discord.utils.get(member.server.roles, name="Regular")
  await client.add_roles(member, role)
  emb = (discord.Embed(description=None, colour=0x3DF270))
  welcome = client.get_channel("430163464867151882")
  emb.add_field(name="New Member", value="Welcome to EastView, <@%s>! Have a great time with your RP. Before going anywhere, feel free to check out the useful links text channel! If you need staff, feel free to use @Staff and staff will be with you as soon as possible! Also say '?cmds' to get started! " % (member.id), inline=False)
  await client.send_message(welcome, embed=emb)

@client.event

async def on_message_delete(message):
  logschannel = client.get_channel("430209484489752588")
  emb = (discord.Embed(description=None, colour=0xFF0000))
  emb.add_field(name="Message Deletion",value="A message was deleted in <#%s>" % (message.channel.id),inline=False)
  emb.add_field(name="Message created by", value="%s" % (message.author), inline=False)
  emb.add_field(name="Message", value="%s" % (message.content), inline=False)
  await client.send_message(logschannel, embed=emb)

@client.event 

async def on_message_edit(before, after):
  logschannel = client.get_channel("430209484489752588")
  emb = (discord.Embed(description=None, colour=0xFF0000))
  emb.add_field(name="Edited Message",value="A message was edited in <#%s>" % (after.channel.id),inline=False)
  emb.add_field(name="Message edited by", value="%s" % (after.author), inline=False)
  emb.add_field(name="Original Message", value="%s" % (before.content), inline=False)
  emb.add_field(name="Edited Message", value="%s" % (after.content), inline=False)
  await client.send_message(logschannel, embed=emb)
  
@client.command()
async def foo(arg):
    pass
    await client.send_message(ctx.message.channel, arg)
 
@client.event
async def on_message(message):
    contents = message.content.split(" ")
    for word in contents:
        if word.upper() in chat_filter:
            if not message.author.id in bypass_list:
                try:
                    await client.delete_message(message)
                    await client.send_message(message.channel, "**HEY DONT SAY THAT!!**")
                except discord.errors.NotFound:
                    return
    numOfMessages +1
    if message.content.upper().startswith('?HELP'):
        emb = (discord.Embed(description=None, colour=0x3DF270))
        emb.add_field(name="Welcome to EastView!",value="I am here to serve and protect this server. For version info, say `?version`. I am still being coded and I barely have commands, but that will change!",inline=False)
        print("%s ran the ?help command!" % (message.author.id))
        await client.send_message(message.channel, embed=emb)
    if message.content.upper().startswith('?VERSION') or message.content.upper().startswith('*VERSION') or message.content.upper().startswith('-VERSION') or message.content.upper().startswith('>VERSION'):
       emb = (discord.Embed(description=None, colour=0x3DF270))
       emb.add_field(name="Version", value="I am in Alpha stages. I am still being made and some features might not work.", inline=False)
       await client.send_message(message.channel, embed=emb)
       print("%s ran the ?version command!" % (message.author.id))
    if message.content.upper().startswith('?8BALL') or message.content.upper().startswith('*8BALL') or message.content.upper().startswith('-8BALL') or message.content.upper().startswith('>8BALL'):
        userID = message.author.id
        randnum = random.randint(1,11)
        if randnum == 1:
            await client.send_message(message.channel,"<@%s> :8ball: It is likely. :8ball:" % (userID))
        if randnum == 2:
            await client.send_message(message.channel, "<@%s> :8ball: I am afraid not. :8ball:" % (userID))
        if randnum == 3:
            await client.send_message(message.channel, "<@%s> :8ball: I do not see it in the future. :8ball:" % (userID))
        if randnum == 4:
            await client.send_message(message.channel, "<@%s> :8ball: Very possible. :8ball:" % (userID))
        if randnum == 5:
            await client.send_message(message.channel, "<@%s> :8ball: There is a very bad chance. :8ball:" % (userID))
        if randnum == 6:
            await client.send_message(message.channel, "<@%s> :8ball: I see it in the future. :8ball:" % (userID))
        if randnum == 7:
            await client.send_message(message.channel, "<@%s> :8ball: There is an great chance. :8ball:" % (userID))
        if randnum == 8:
            await client.send_message(message.channel, "<@%s> :8ball: I do not see this happening. :8ball:" % (userID))
        if randnum == 9:
            await client.send_message(message.channel, "<@%s> :8ball: I see something positive. :8ball:" % (userID))
        if randnum == 10:
            await client.send_message(message.channel, "<@%s> :8ball: I don't see it. You may as well walk away. :8ball:" % (userID))
    if message.content.upper().startswith('?KICK'):
          if "430187539668664341" in [role.id for role in message.author.roles]:
            await client.send_message(message.channel, "<@%s> :white_check_mark: You have kicked <@%s> successfully." % (message.author.id, message.mentions[0].id))
            await client.kick(message.mentions[0])
          else:
            await client.send_message(message.channel, "<@%s> :x: You are not an admin and cannot run this command!" % (message.author.id))
    if message.content.upper().startswith('?BAN'):
          if "430187539668664341" in [role.id for role in message.author.roles]:
            await client.send_message(message.channel, "<@%s> :white_check_mark: You have banned <@%s> successfully." % (message.author.id, message.mentions[0].id))
            await client.ban(message.mentions[0], delete_message_days=7)
          else:
            await client.send_message(message.channel, "<@%s> :x: You are not an admin and cannot run this command!" % (message.author.id))
    if message.content.upper().startswith('?MUTE'):
      if "430187539668664341" in [role.id for role in message.author.roles]:
         muted = discord.utils.get(message.server.roles, name="Muted")
         await client.add_roles(message.mentions[0], muted)
         await client.send_message(message.channel, "<@%s> :white_check_mark: You have muted <@%s>! Run `?unmute @user` to unmute this user!" % (message.author.id, message.mentions[0].id))
      else:
         await client.send_message(message.channel, "<@%s> :x: You are not an admin and cannot run that command!" % (message.author.id))
    if message.content.upper().startswith('?UNBAN'):
          args = message.content.split(" ")
          if "430187539668664341" in [role.id for role in message.author.roles]:
            uid = " ".join(args[1:])
            await client.send_message(message.channel, "<@%s> :white_check_mark: You have unbanned %s successfully." % (message.author.id, uid))
            await client.unban(message.server, client.get_user_info(uid))
          else:
            await client.send_message(message.channel, "<@%s> :x: You are not an admin and cannot run this command!" % (message.author.id))
    if message.content.upper().startswith('?UNMUTE'):
      if "430187539668664341" in [role.id for role in message.author.roles]:
         muted = discord.utils.get(message.server.roles, name="Muted")
         await client.remove_roles(message.mentions[0], muted)
         await client.send_message(message.channel, "<@%s> :white_check_mark: You have unmuted <@%s>! Made a mistake? Use `?mute @user`" % (message.author.id, message.mentions[0].id))
      else:
         await client.send_message(message.channel, "<@%s> :x: You are not an admin and cannot run that command!" % (message.author.id))
    if message.content.upper().startswith('?ANNE'):
      if "430187539668664341" in [role.id for role in message.author.roles]:
         args = message.content.split(" ")
         announcechannel = client.get_channel("430163492998217728")
         emb = (discord.Embed(description=None, colour=0xFFA500))
         emb.add_field(name="Announcement by %s" % (message.author), value="%s" % (" ".join(args[1:])), inline=False)
         await client.send_message(announcechannel, "<@&430220800306446348>")
         await client.send_message(announcechannel, embed=emb)
      else:
         await client.send_message(message.channel, "<@%s> :x: You are not an admin and cannot run that command!" % (message.author.id))
    if message.content.upper().startswith('?SET'):
       c.execute("CREATE TABLE IF NOT EXISTS coinStorage(user TEXT, coins INTEGER)")
       emb = (discord.Embed(description=None, colour=0x3DF270))
       emb.add_field(name="Success", value="You have added a table to the Coin Storage Database!", inline=False)
       await client.send_message(message.channel, embed=emb)
    if message.content.upper().startswith('?REGISTER'):
       user = str(message.author)
       val = int(1000)
       c.execute("INSERT INTO coinStorage VALUES (?, ?)",
          (user, val))
       coinconn.commit()
       emb = (discord.Embed(description=None, colour=0x3DF270))
       emb.add_field(name="Success", value="You have registered yourself to the Coin Storage Database! User: `%s` | Coins: `1000`" % (message.author), inline=False)
       await client.send_message(message.channel, embed=emb)
    if message.content.upper().startswith('?COINS'):
           c.execute('SELECT * FROM coinStorage')
           data = c.fetchall()
           for row in data:
              if row[0] == str(message.author):
                 emb = (discord.Embed(description=None, colour=0x3DF270))
                 emb.add_field(name="Coins", value="You have %s coins!" % (row[1]), inline=False)
                 await client.send_message(message.channel, embed=emb)
    if message.content.upper().startswith('?WARN'):
        if "430187539668664341" in [role.id for role in message.author.roles]:
                                                                              args = message.content.split(" ")
                                                                              chan = client.get_channel("430209484489752588")
                                                                              embed = (discord.Embed(description=None, colour=0x00ff00))
                                                                              embed.add_field(name="Someone Has Been Warned By %s" % (message.author), value="%s" % (" ".join(args[1:])), inline=False)
                                                                              embed2 = (discord.Embed(description=None, colour=0x00ff00))
                                                                              embed2.add_field(name="You Have Successfully Warned Somebody!", value="You Have Warned Someone! You Have Warned Them For The Following: %s" % (" ".join(args[1:])), inline=False)
                                                                              await client.send_message(message.channel, embed=embed2)
                                                                              await client.send_message(chan, embed=embed)
        else:
            await client.send_message(message.channel, "You Do Not Have Permission")
    if message.content.upper().startswith('?CMDS'):
                                                  embed3 = (discord.Embed(description=None, colour=0x00ff00))
                                                  embed3.set_author(name="Server Commands")
                                                  embed3.add_field(name="?SET -Starts Coins", value="?PING -Plays Ping Pong", inline=True)
                                                  embed3.add_field(name="?Register - Registers you to the bank", value="?Coins - Checks your coins", inline=True)
                                                  embed3.add_field(name="cookie and milk -gives you cookies and milk", value="?8ball (your words) -plays 8ball", inline=True)
                                                  embed3.add_field(name="?VERSION -tells you the bot version", value="N/A", inline=True)
                                                  await client.send_message(message.channel, embed=embed3)
    if message.content.upper().startswith('?ADMINCMDS'):
        if "430187539668664341" in [role.id for role in message.author.roles]:
                                                                             embed3 = (discord.Embed(description=None, colour=0x00ff00))
                                                                             embed3.set_author(name="Server Admin Commands")
                                                                             embed3.add_field(name="?KICK @user", value="?ANNE (announcement)", inline=True)
                                                                             embed3.add_field(name="?MUTE @user/?UNMUTE @user", value="?BAN @user/?UNBAN @user", inline=True)
                                                                             embed3.add_field(name="?WARN @(WARNED PERSON) For (your words)", value="N/A", inline=True)
                                                                             await client.send_message(message.channel, embed=embed3)
        else:
            await client.send_message(message.channel, "You Do Not Have Permission")
    if message.content == "cookies and milk":
        await client.send_message(message.channel, "Here's your cookie :cookie: . Almost forgot your milk :milk:!")
    if message.content.upper().startswith('?PING'):
        userID = message.author.id
        await client.send_message(message.channel, ":ping_pong: pong!")
client.run("NDMwMjAyMjU2MjgyMDkxNTIw.DaMwmA.bVnzFLy1SgnNx9DeuGhhpX61QKc")
