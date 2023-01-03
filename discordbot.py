import discord
import json
import requests
import random


client = discord.Client()

sad_words = ['sad', 'bad', 'angry', 'blue', 'brokenhearted', 'cast down', 'crest fallen', 'dejected', 'depressed', 'despondent', 'disconsolate', 'doleful', 'down', 'downcast', 'downhearted', 'down in the mouth', 'droopy', 'forlorn', 'gloomy', 'glum', 'hangdog', 'heartbroken', 'heartsick', 'heartsore', 'heavyhearted', 'inconsolable', 'joyless', 'low', 'low-spirited', 'melancholic', 'melancholy', 'miserable', 'mournful', 'saddened', 'sorrowful', 'sorry', 'unhappy', 'woebegone', 'woeful', 'wretched']
starter_encouragements = [
    'Cheer Up!',
    'Hang in there!', 
    'You are a great person/bot',
    "It's okay, you'll get them next time", 
    'The sun is coming down', 
    'rou2 ya clint'
]
db = {}


def get_quote():
    response = requests.get("https://zenquotes.io/api/random")
    json_data = json.loads(response.text)
    quote = json_data[0]['q'] + " -" + json_data[0]['a']
    return quote


def update_encouragements(encouraging_message):
    if 'encouragements' in db.keys():
        encouragements = db['encouragements']
        encouragements.append(encouraging_message)
        db['encouragements'] = encouragements
    else:
        db['encouragements'] = [encouraging_message]


def del_message(index):
    encouragements = db['encouragements']
    if len(encouragements) > index:
        del encouragements[index]
        db['encouragements'] = encouragements


@client.event
async def on_ready():
    print(f'We have logged in as {client.user}')


@client.event
async def on_message(message):
    msg = message.content
    if message.author == client.user:
        return 
    
    if message.content.startswith('#hello'):
        await message.channel.send(f'Hello {message.author.nick}!')

    if message.content.startswith('#whoisboutrosgf'):
        await message.channel.send('Marie-Lou Issa')
    
    if message.content.startswith('#inspire'):
        await message.channel.send(get_quote())
    
    if message.content.startswith('#thank you'):
        await message.channel.send("Your very welcome!, if you ever need anything just the one who programmed me to tell me how!!!")
    
    options = starter_encouragements
    if 'encouragements' in db.keys():
        options += db['encouragements']


    if any(word in msg for word in sad_words) or any(word.upper() in msg for word in sad_words):
        await message.channel.send(random.choice(options))             
    

client.run('OTM3ODA2NTc5MzA1MTY0ODIx.YfhGcA.ihDcr5FUAJG0_rDZech9aM6LAQs')

