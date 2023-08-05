# randseal
Simple package that can produce a seal image. The image is then output as a `discord.File` or `discord.Embed` for Pycord.

### Usage example
```py
import randseal
from discord import Bot, Intents

bot = Bot(intents=Intents.default())
client = randseal.Client()

@bot.slash_command()
async def sealimg(ctx):
  file=await client.asyncFile()
  await ctx.respond(file=file)

@bot.slash_command()
async def sealembed(ctx):
  await ctx.respond(embed=client.Embed())

bot.run("token")
```