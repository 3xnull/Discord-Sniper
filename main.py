import asyncio
import json
import time
from os import system
from random import randint
from discord.ext import commands
import re
import httpx
from colorama import Fore, init
import platform



init()
data = {}

with open('token.json') as sex:
    data = json.load(sex)
token = data['token']
invitesniper = data['invitesnipe']

os = platform.system()

if os == "Windows":
    system("cls")
else:
    system("clear")
    print(chr(27) + "[2J")

print(Fore.RED + """\

 █████╗ ███╗   ███╗██╗███████╗
██╔══██╗████╗ ████║██║╚══███╔╝
███████║██╔████╔██║██║  ███╔╝ 
██╔══██║██║╚██╔╝██║██║ ███╔╝  
██║  ██║██║ ╚═╝ ██║██║███████╗
╚═╝  ╚═╝╚═╝     ╚═╝╚═╝╚══════╝
                              

 """.replace('█', '█' + Fore.CYAN))
print("========================================")
Eagle = commands.Bot(command_prefix=".", self_Eagle=True)
ready = False

codeRegex = re.compile("(discord.com/gifts/|discordapp.com/gifts/|discord.gift/)([a-zA-Z0-9]+)")


try:
    @Eagle.event
    async def on_message(ctx):
        global ready
        if not ready:
            print(Fore.CYAN + 'AMIZ Sniper | ON\n' + Fore.LIGHTBLUE_EX + ' [DEV] - stoned.eagle#0001' + 'servers' + str(
                len(Eagle.guilds)) + ' Servers 🔫\n' + Fore.RESET)
            print(Fore.LIGHTBLUE_EX + time.strftime("%H:%M:%S ", time.localtime()) + Fore.RESET, end='')
            print(f"{Fore.LIGHTGREEN_EX}[START] - Eagle is ready")
            if invitesniper == 'True':
                print(Fore.LIGHTBLUE_EX + "[ENABLED] - Invite Sniper: ON")
            else:
                print("[DISABLED] - Invite Sniper: OFF")
            ready = True
        if codeRegex.search(ctx.content):
            print(Fore.LIGHTBLUE_EX + time.strftime("%H:%M:%S ", time.localtime()) + Fore.RESET, end='')
            code = codeRegex.search(ctx.content).group(2)

            start_time = time.time()
            if len(code) < 16:
                try:
                    print(
                        Fore.RED + "[INVALID] -  Invalid Code: " + code + " From " + ctx.author.name + "#" + ctx.author.discriminator + ". |" + ctx.jump_url  )
                except:
                    print(
                        Fore.RED + "[INVALID]  - Invalid Code | " + code + " From " + ctx.author.name + "#" + ctx.author.discriminator + Fore.RESET)

            else:
                async with httpx.AsyncClient() as client:
                    result = await client.post(
                        'https://discordapp.com/api/v6/entitlements/gift-codes/' + code + '/redeem',
                        json={'channel_id': str(ctx.channel.id)},
                        headers={'authorization': token, 'user-agent': 'Mozilla/5.0'})
                    delay = (time.time() - start_time)
                    try:
                        print(
                            Fore.LIGHTGREEN_EX + "[-] Sniped code: " + Fore.LIGHTRED_EX + code + Fore.RESET + " From " + ctx.author.name + "#" + ctx.author.discriminator + Fore.LIGHTMAGENTA_EX + " [" + ctx.guild.name + " > " + ctx.channel.name + "]" + Fore.RESET)
                    except:
                        print(
                            Fore.LIGHTGREEN_EX + "[-] Sniped code: " + Fore.LIGHTRED_EX + code + Fore.RESET + " From " + ctx.author.name + "#" + ctx.author.discriminator + Fore.RESET)

                if 'This gift has been redeemed already' in str(result.content):
                    print(Fore.LIGHTBLUE_EX + time.strftime("%H:%M:%S ", time.localtime()) + Fore.RESET, end='')
                    print(Fore.LIGHTYELLOW_EX + "[REDEEMED] - Code has been already redeemed" + Fore.RESET,
                          end='')
                elif 'nitro' in str(result.content):
                    print(Fore.LIGHTBLUE_EX + time.strftime("%H:%M:%S ", time.localtime()) + Fore.RESET, end='')
                    print(Fore.GREEN + f"[SNIPED] - GG, Nitro Applied to{Eagle.user}"  + Fore.RESET, end='')
                elif 'Unknown Gift Code' in str(result.content):
                    print(Fore.LIGHTBLUE_EX + time.strftime("%H:%M:%S ", time.localtime()) + Fore.RESET, end='')
                    print(Fore.LIGHTRED_EX + "[-] Invalid Code" + Fore.RESET, end=' ')
                print(" Delay:" + Fore.GREEN + " %.3fs" % delay + Fore.RESET)
        elif (('**giveaway**' in str(ctx.content).lower() or ('react with' in str(
                ctx.content).lower() and 'giveaway' in str(ctx.content).lower()))):
            try:
                await asyncio.sleep(randint(100, 200))
                await ctx.add_reaction("🎉")
                print(Fore.LIGHTBLUE_EX + time.strftime("%H:%M:%S ", time.localtime()) + Fore.RESET, end='')
                print(
                    Fore.LIGHTYELLOW_EX + "[-] Enter Giveaway " + Fore.LIGHTMAGENTA_EX + " [" + ctx.guild.name + " > " + ctx.channel.name + "]" + Fore.RESET)
            except:
                print(Fore.LIGHTBLUE_EX + time.strftime("%H:%M:%S ", time.localtime()) + Fore.RESET, end='')
                print(
                      Fore.RED + "[ERROR] - Something went wrong with Giveaway Sniper " + Fore.LIGHTMAGENTA_EX + " [" + ctx.guild.name + " > " + ctx.channel.name + "]" + Fore.RESET)
        elif '<@' + str(Eagle.user.id) + '>' in ctx.content and (
                'giveaway' in str(ctx.content).lower() or 'won' in ctx.content or 'winner' in str(
            ctx.content).lower()):
            print(Fore.LIGHTBLUE_EX + time.strftime("%H:%M:%S ", time.localtime()) + Fore.RESET, end='')
            try:
                won = re.search("You won the \*\*(.*)\*\*", ctx.content).group(1)
            except:
                won = "UNKNOWN"
            print(
                Fore.GREEN + "[GIVEAWAY] - Giveaway Won: " + Fore.LIGHTCYAN_EX + won + Fore.LIGHTMAGENTA_EX + " [" + ctx.guild.name + " > " + ctx.channel.name + "]" + Fore.RESET)

        elif 'discord.gg' in str(ctx.content).lower():
            print(Fore.LIGHTBLUE_EX + time.strftime("%H:%M:%S ", time.localtime()) + Fore.RESET, end='')
            try:
              if invitesniper == 'True':
               print(Fore.BLUE + "[INVITE] - Invite Found")
              else:
                return
            except:
                print("[INFO] - Invite not resolved")
            if invitesniper == 'True':
             print(
                Fore.GREEN + "[INVITE] - Invite Found: " + Fore.LIGHTCYAN_EX + ctx.content + Fore.LIGHTMAGENTA_EX + " [" + ctx.guild.name + " > " + ctx.channel.name + "]" + Fore.RESET)
            else:
              return

    Eagle.run(token, bot=False)
except:
  print(Fore.LIGHTRED_EX + "[ERROR] - Invalid Token Detected")
  print(Fore.LIGHTBLUE_EX + "[TIP] - Put your Token in token.json")

  time.sleep(500)
  print("[BRUH] - bro fix ur token lmfao")
