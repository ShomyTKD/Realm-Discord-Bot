import discord
from discord import Color
import random

async def ex(args, message, client, invoke):
    num = random.randint(1, 14)
    if(num == 1):
        await client.send_file(message.channel, "classes/Archer.png")
        em = discord.Embed(title='Archer', description='The Archer has a long-range attack and can acquire very powerful weapons. \nMore info: https://www.realmeye.com/wiki/archer', color=Color.green())
        await client.send_message(message.channel, embed=em)
    elif(num == 2):
        await client.send_file(message.channel, "classes/Assassin.png")
        em = discord.Embed(title='Assassin', description='The Assassin fights from medium range and uses poison to damage his enemies over time. \nMore info: https://www.realmeye.com/wiki/assassin', color=Color.green())
        await client.send_message(message.channel, embed=em)
    elif(num == 3):
        await client.send_file(message.channel, "classes/Huntress.png")
        em = discord.Embed(title='Huntress', description='The Huntress uses arrows and traps to defeat her enemies. \nMore info: https://www.realmeye.com/wiki/huntress', color=Color.green())
        await client.send_message(message.channel, embed=em)
    elif(num == 4):
        await client.send_file(message.channel, "classes/Knight.png")
        em = discord.Embed(title='Knight', description='The Knight fights at close range, wears heavy armor, and uses his shield to stun enemies. \nMore info: https://www.realmeye.com/wiki/knight', color=Color.green())
        await client.send_message(message.channel, embed=em)
    elif(num == 5):
        await client.send_file(message.channel, "classes/Mystic.png")
        em = discord.Embed(title='Mystic', description='The Mystic fights with a staff and uses her crystal orb to bind enemies to a distant plane. \nMore info: https://www.realmeye.com/wiki/mystic', color=Color.green())
        await client.send_message(message.channel, embed=em)
    elif(num == 6):
        await client.send_file(message.channel, "classes/Necromancer.png")
        em = discord.Embed(title='Necromancer', description='The Necromancer drains life from his enemies to heal himself and his allies. \nMore info: https://www.realmeye.com/wiki/necromancer', color=Color.green())
        await client.send_message(message.channel, embed=em)
    elif(num == 7):
        await client.send_file(message.channel, "classes/Ninja.png")
        em = discord.Embed(title='Ninja', description='The Ninja relies on speed and skill, using katanas and ninja stars to deal formidable amounts of damage. \nMore info: https://www.realmeye.com/wiki/ninja', color=Color.green())
        await client.send_message(message.channel, embed=em)
    elif(num == 8):
        await client.send_file(message.channel, "classes/Paladin.png")
        em = discord.Embed(title='Paladin', description='The Paladin can deal damage at close range, wear heavy armor, and heal himself and his allies. \nMore info: https://www.realmeye.com/wiki/paladin', color=Color.green())
        await client.send_message(message.channel, embed=em)
    elif(num == 9):
        await client.send_file(message.channel, "classes/Priest.png")
        em = discord.Embed(title='Priest', description='The Priest attacks at long range and can heal himself and his allies. \nMore info: https://www.realmeye.com/wiki/priest', color=Color.green())
        await client.send_message(message.channel, embed=em)
    elif(num == 10):
        await client.send_file(message.channel, "classes/Rogue.png")
        em = discord.Embed(title='Rogue', description='The Rogue relies on his speed to deal damage at medium range while avoiding attacks. \nMore info: https://www.realmeye.com/wiki/rogue', color=Color.green())
        await client.send_message(message.channel, embed=em)
    elif(num == 11):
        await client.send_file(message.channel, "classes/Sorcerer.png")
        em = discord.Embed(title='Sorcerer', description='The Sorcerer can attack from the longest range with a wand, and he uses his scepter to fire blasts of chain lightning at his enemies. \nMore info: https://www.realmeye.com/wiki/sorcerer', color=Color.green())
        await client.send_message(message.channel, embed=em)
    elif(num == 12):
        await client.send_file(message.channel, "classes/Trickster.png")
        em = discord.Embed(title='Trickster', description='The Trickster fights with a dagger while using her magical prism to distract enemies. \nMore info: https://www.realmeye.com/wiki/trickster', color=Color.green())
        await client.send_message(message.channel, embed=em)
    elif(num == 13):
        await client.send_file(message.channel, "classes/Warrior.png")
        em = discord.Embed(title='Warrior', description='The Warrior wears strong armor and uses his magic helmet to inspire his allies in battle. \nMore info: https://www.realmeye.com/wiki/warrior', color=Color.green())
        await client.send_message(message.channel, embed=em)
    elif(num == 14):
        await client.send_file(message.channel, "classes/Wizard.png")
        em = discord.Embed(title='Wizard', description='The Wizard deals damage from a long distance and blasts enemies with powerful spells. \nMore info: https://www.realmeye.com/wiki/wizard', color=Color.green())
        await client.send_message(message.channel, embed=em)
    else:
        await client.send_message(message.channel, "Ooops, something went wrong!")
