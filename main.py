import discord

client = discord.Client()

@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith(',info'):
        embed = discord.Embed(title="Airo Bot Info", description="Check out these commands!", color=0xE2E2E2)
        embed.add_field(name=",info", value="Shows this box!")
        embed.add_field(name=",hello", value="Gives a nice greeting!")
        await message.channel.send(content=None, embed=embed)
    elif message.content.startswith(',hello'):
        await message.channel.send("Hey there, I'm Airo Bot!")
    elif message.content.startswith('oof'):
        await message.channel.send("oof, what's happening? ;-;")


client.run('NjE3NDA1MDQ2NzI4MDMyMzQ3.XWqphA.K6uKfsHF2K4DMoLZWFuA9foW97g')
