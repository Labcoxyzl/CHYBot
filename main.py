#basic bot
import discord
import os
import requests #for http request
import json
import random
from discord.ext import commands
from replit import db #database(dictionary)
from stayOnline import stay_online
requestList = []



####################  Functions  ##########################
def getQuote(): #random quote
  response = requests.get("https://zenquotes.io/api/random")
  quoteData = json.loads(response.text)
  quote = quoteData[0]['q'] + " -" + quoteData[0]['a']
  return(quote)

def trollPlay():
  return "Incomplete"
###################  Discord  #############################

client = discord.Client() #get client

bot = commands.Bot(command_prefix='?', case_insensitive=True)
bot.remove_command('help')
#Discord bots is basically callback func spams
# @client.event
# async def on_ready(): #when bot is ready
#   print('Successfully logged in as {0.user}'.format(client))

@bot.event
async def on_ready(): #setup
  await bot.change_presence(status=discord.Status.online, activity=discord.Game('Stack Overflow ?help'))
  print('Successfully logged in as {0.user}'.format(bot))

@bot.event
async def on_command_error(ctx, error):
  if isinstance(error, commands.MissingRequiredArgument):
    await ctx.send("Missing Arguments!")


################  Discord: Commands  ######################## 

@bot.command(aliases=['hello','hi'])
async def ping(ctx):
  await ctx.send(f"Ping successful, bot is online at {round(bot.latency * 1000)}ms")

@bot.command()
async def play(ctx):
  await ctx.send("Work in progress")

@bot.command()
async def addrole(ctx, role: discord.Role, member: discord.Member=None):
    member = member or ctx.message.author
    print(role)
    await member.add_roles(member, role)
  
@bot.command()
async def rmb(ctx, user: discord.Member=None, *, msg):
  user = user or ctx.message.author
  db[f"{user}"] = db[f"{user}"] + [msg]
  await ctx.send(f"'{msg}' saved as a reminder for {user}")


@bot.command()
async def remind(ctx, user: discord.Member=None):
  await ctx.send((db.keys()))
  user = user or ctx.message.author
  await ctx.send(user)
  db[f"{user}"] = "asdada"
  val = db[f"{user}"]
  await ctx.send(f"{val}")


# @bot.command()
# async def mute(ctx, member: discord.Member, *, reason=None):
#     role = discord.utils.get(member.guild.roles, name='Muted')
#     await member.add_roles(member, role)
#     embed=discord.Embed(title="User Muted!", description="**{0}** was muted by **{1}**!".format(member, ctx.message.author), color=0xff00f6)
#     await bot.say(embed=embed)

# @bot.command()
# @commands.bot_has_permissions(mute_members=True)
# async def muteAll(self, ctx):
#     if ctx.author.voice and ctx.author.voice.channel:
#         channel = ctx.author.voice.channel
#         for member in channel.members:
#             await member.edit(mute=True)
#     else:
#       await ctx.send("You are not connected to a voice channel!")

@bot.command()
#@commands.has_permissions(mute_members=True)
async def mute(ctx, member: discord.Member, *, reason=None):
  await member.mute(reason=reason)
  await ctx.send(f"{member} has been muted.")


@bot.command(aliases=['command','commands','commandlist'])
async def help(ctx):
  with open('commandList.json', 'r') as cFile:
    global cDict
    cDict = json.load(cFile)
  cMessage = "COMMAND LIST (command - use)\n(commands cannot be combined)\n"
  for command in cDict:
    cMessage += f"\n{command}\t\t-\t{cDict[command]}"
  await ctx.send(cMessage) #respond message
  
@bot.command()
async def flip(ctx):
  with ctx.channel.typing():
    await ctx.send("Flipping coin...")
    flip = random.randint(0,1)
    if(flip == 0):
      await ctx.send("Flip returned heads.")
    if(flip == 1):
      await ctx.send("Flip returned tails.")


@bot.command(aliases=['spoil'])
async def spl(ctx, *, message):
  #await ctx.channel.purge(limit=1)
  await ctx.message.delete()
  await ctx.send(f"||{message}||")


@bot.command()
async def quote(ctx):
  await ctx.send(getQuote())

@bot.command(aliases=['req','reqs'])
async def request(ctx, *, req):
  requestList.append(str(req))
  await ctx.send(f"Request '{req}' has been added.")


@bot.command()
async def clear(ctx, amount=2):
  if(amount>10):
    await ctx.send(f"{amount} is too many")
  elif(amount<1):
    await ctx.send("You cant delete less than 1 message")
  else:
    await ctx.channel.purge(limit=amount+1)

@clear.error
async def clear_error(ctx, error):
  await ctx.send(f"Please use format !clear [integer]; {error}")

@bot.command()
async def prefix(ctx, prefix='!'):
  bot = commands.Bot(command_prefix=prefix , case_insensitive=True)
  bot.remove_command('help')
  await ctx.send(f"Current prefix is '{prefix}'")



########## ATERNOS #########





stay_online() #keeps bot online and alive with web server
bot.run(os.getenv('TOKEN')) #runs bot using token(secret!)
