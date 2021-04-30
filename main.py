#basic bot
import discord
import os
import requests #for http request
import json
import random
from discord.ext import commands
import asyncio
from replit import db #database(dictionary)
from stayOnline import stay_online
requests = []

from aternosapi import AternosAPI





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
bot = commands.Bot(command_prefix='!', case_insensitive=True)
bot.remove_command('help')
#Discord bots is basically callback func spams
# @client.event
# async def on_ready(): #when bot is ready
#   print('Successfully logged in as {0.user}'.format(client))

@bot.event
async def on_ready(): #setup
  await bot.change_presence(status=discord.Status.online, activity=discord.Game('Stack Overflow !help'))
  print('Successfully logged in as {0.user}'.format(bot))

@bot.event
async def on_command_error(ctx, error):
  if isinstance(error, commands.MissingRequiredArgument):
    await ctx.send("Missing Arguments!")


################  Discord: Commands  ######################## 
headers_cookie = "ATERNOS_SEC_oi3l9lqmwr000000=dm4l7ez67r000000; __cfduid=d4a97da766b70c5a243ffe861652ad1fd1608467870; _ga=GA1.2.298194745.1608467871; PHPSESSID=mgqcbfu0tt4kuspb5otq57mq5h; ATERNOS_SESSION=L5pIVbQCHXkinKDd00m00SQgATSm3j2y4H1H90HukxV9ACkJ2wc5Trqk4ZNmElTr5ZwVtW0w8JEhwiP2ypLooTvZBMozGKqeyX5U; __gads=ID=fc9cbd4b939ee79e:T=1608467942:S=ALNI_MbnSRBvzORZows9BciIr14ntaspLQ; _pbjs_userid_consent_data=3524755945110770; SKpbjs-unifiedid=%7B%22TDID%22%3A%223f176185-8791-456e-9e75-76e50a83cbf4%22%2C%22TDID_LOOKUP%22%3A%22FALSE%22%2C%22TDID_CREATED_AT%22%3A%222020-12-20T12%3A39%3A51%22%7D; SKpbjs-unifiedid_last=Sun%2C%2020%20Dec%202020%2012%3A39%3A51%20GMT; SKpbjs-id5id=%7B%22created_at%22%3A%222020-12-20T12%3A39%3A52.308Z%22%2C%22id5_consent%22%3Atrue%2C%22original_uid%22%3A%22ID5-ZHMOlas4R5UajBtrP3P8Bq6d0XBHk1m8TzGWcf8Vcg%22%2C%22universal_uid%22%3A%22ID5-ZHMOlas4R5UajBtrP3P8Bq6d0XBHk1m8TzGWcf8Vcg%22%2C%22signature%22%3A%22ID5_AXs20pDPTH9-Q6-95qQDgTILTa0Iq0sRipD5MPkvZ_lV179KAGxEYuTf-eiyQKSXQq-2Hx8m8IcRmZxpuRCTeH4%22%2C%22link_type%22%3A0%2C%22cascade_needed%22%3Atrue%7D; SKpbjs-id5id_last=Sun%2C%2020%20Dec%202020%2012%3A39%3A52%20GMT; id5id.1st_212_nb=0; GED_PLAYLIST_ACTIVITY=W3sidSI6IjhYbWoiLCJ0c2wiOjE2MDg0Njc5OTgsIm52IjoxLCJ1cHQiOjE2MDg0Njc5ODgsImx0IjoxNjA4NDY3OTk4fV0.; ATERNOS_LANGUAGE=en; _gid=GA1.2.639329051.1608898662; cto_bidid=pvEXR19qJTJGZkh5UzZmQXlFcFIlMkJTU0tRYyUyQlJZdWt1S0tUN0V1eXBEcnRSeU1YcjFEZVoyUjlZdDNKdXljMVNFcjhhdVE2UWVvUEg1MEJBc3dSb1BRVTFNY1l6dyUzRCUzRA; cto_bundle=FJdlA192bThCeHg4RyUyRmh3UzdPWVdlMXZ3cG02TWxpYzlwVEklMkZLSnVMUUlyeFU1TkRwNTBtWkExa1hRV2NPOW1NUHZFcTNHbVZTR1NMTmVpMlU1OVVyRjBzek1LQ3QzYmZLWlEyTGtGQWowOUpUSnhjRWhGSGQ2c2NzRlo2aW03M1dYRVY; ATERNOS_SERVER=pqFILHodovq3IssA; cto_bundle=9IsxVl9ZRFJJZ0ZqR1BRR1JmRFp0dWFBU2hBR09JUkc1WmVhQWZHQUolMkZ3ZG5YakxjZGlpVW9iZjY2eFJSc0d4VmM4JTJCMjZ0dGpsb01BSVFBdnNGNDVVN3pqTzgyJTJGT29qdml1UyUyQm50ZGl3WE1zMnhOSWZ0Tkp1b05BQnhWZmdlZ3Y1YURwWUZtTDdvYzExbVprNEx4Zm9xbnNodyUzRCUzRA; id5id.1st_364_nb=2"
mcTOKEN = "CqSDBVGXlXS3itZQj8oT"
server = AternosAPI(headers_cookie, mcTOKEN)

# @bot.command()
# async def mc(ctx, args1):
#   args1 = args1.lower()
#   if args1 == "start":
#     await ctx.send(server.StartServer())
#   if args1 == "stop":
#     await ctx.send(server.StopServer())
#   if args1 == "status":
#     await ctx.send(server.GetStatus())
#   if args1 == "info":
#     await ctx.send(server.GetServerInfo())
#   else:
#     await ctx.send("Invalid input")
@bot.command()
async def mc_start(ctx):
  await ctx.send(server.StartServer())
@bot.command()
async def mc_stop(ctx):
  await ctx.send(server.StopServer())
@bot.command()
async def mc_status(ctx):
  await ctx.send(server.GetStatus())
@bot.command()
async def mc_info(ctx):
  await ctx.send(server.GetServerInfo())

@bot.command()
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
  print(cMessage)
  await ctx.send(cMessage) #respond message
  
@bot.command()
async def flip(ctx):
  await ctx.send("Flipping coin...")

  flip = random.randint(0,1)
  if(flip == 0):
    await ctx.send("Flip returned heads.")
  if(flip == 1):
    await ctx.send("Flip returned tails.")

@bot.command()
async def spl(ctx, *, message):
  message = "||"+message+"||"
  await ctx.send(message)  


@bot.command()
async def quote(ctx):
    await ctx.send(getQuote())

@bot.command(aliases=['req','reqs'])
async def request(ctx, *, req):
  requests.append(str(req))
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
  await ctx.send("Please use format !clear [integer] ")



########## ATERNOS #########





stay_online() #keeps bot online and alive with web server
bot.run(os.getenv('TOKEN')) #runs bot using token(secret!)
t