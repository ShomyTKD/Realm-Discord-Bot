import discord
from discord import Game, Color

from commands import cmd_whattoplay

import SECRETS
# Prefix for commands
PREFIX = '!'

client = discord.Client()

commands = {
    "WHATTOPLAY": cmd_whattoplay,
}

# Some serious stuff is going on down there!

@client.event
# When bot connects
async def on_ready():
    print("Realm Bot is ready to give you all info you need! Running on following server(s):\n")
    for s in client.servers:
        print(" - %s (%s)" % (s.name, s.id))
    # We are setting bots game to be something
    await client.change_presence(game=Game(name="Realm of The Mad God"))

@client.event
# Bot responds on commands
async def on_message(message):
    try:
        print(message.content + " - " + message.author.name) # Debugging
    except UnicodeEncodeError:
        return
    # Checking if message starts with prefix '!'
    if message.content.startswith(PREFIX):
        # Setting invoke and args
        invoke = message.content.upper()[len(PREFIX):].split(" ")[0]
        args = message.content.split(" ")[1:]
        print("INVOKE: %s\nARGS: %s" % (invoke, args.__str__()[1:-1].replace("'", "")))
        # Doing something really complicated for humans
        if commands.__contains__(invoke):
            cmd = commands[invoke]
            await cmd.ex(args, message, client, invoke)
        else:
            await client.send_message(message.channel, embed=discord.Embed(color=Color.red(), description="The command '%s' does not exist!" % invoke))

# Some secret file, don't look!
client.run(SECRETS.TOKEN)
