import os
import random
import discord
import json
from dotenv import load_dotenv

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')
client = discord.Client()

@client.event
async def on_ready():
    print(f'{client.user} has connected to Discord!')

@client.event
async def on_message(msg):
    if msg.author == client.user: #ignores the message if it comes from the bot
        return

    #splits the message to find the arguments. stored in the format of a list
    splitMsg = msg.content.split(' ')
    args = splitMsg[1:]

    #Confession handler. Looks for DMs and sends them for approval.
    if isinstance(msg.channel, discord.channel.DMChannel):

        #stores confessions in a seperate text document
        confessions = open('confessions.txt', 'r')
        count = 0
        for line in confessions:
            count += 1

        confessions = open('confessions.txt', 'a+')
        confessions.write(str(msg.content))
        confessions.write("\n")
        confessions.close

        print("Confession Received")
        approvalChannel = client.get_channel(772794603954110466)
        fullConfession = "#" + str(count) + ": ", str(msg.content)
        await approvalChannel.send(''.join(fullConfession))

    #Checks whether the message starts with the prefix. If this is not there, bot replies to every message
    if msg.content.startswith("="):
        if msg.content.startswith('=ping'): #ping command
            await msg.channel.send('Pong!')
        elif msg.content.startswith('=help'): #help command
            await msg.channel.send('jeuseBot\'s help menu can be found at: http://jb.joemama.site')
        elif msg.content.startswith('=sunglasses'): #sunglasses command
            if msg.author.id == 258582004738555904:
                await msg.channel.send("<@258582004738555904> is SO FUCKING COOL. All the ladies fall for him wherever he goes. He is super cool and super smart and super amazing and is the perfect specimen of human being. I really fucking love him because he is so cool and he also made me so that makes him EXTRA COOL!!!!!!!!!!!!!!!!!")
            else:
                await msg.channel.send(":sunglasses: im really cool, and so is <@" + str(msg.author.id) + ">")
        elif msg.content.startswith('=speak'): #speak command
            await msg.channel.send(' '.join(args))
        elif msg.content.startswith('=avatar') or msg.content.startswith('=pfp'): #pfp command
            if msg.content == "=pfp" or msg.content == "=avatar" :
                await msg.channel.send("Your avatar: " + str(msg.author.avatar_url))
            else:
                mentioned = msg.mentions[0]
                await msg.channel.send("<@" + str(mentioned.id) + ">\'s avatar is: " + str(mentioned.avatar_url))
        elif msg.content == '=fuck you': #insult command
            await msg.channel.send("Ay fuck you too, buddy")
        elif msg.content.startswith("=random"): #rng command
            if args:
                await msg.channel.send(random.randint(0, int(args[0])))
            else:
                await msg.channel.send(random.randint(0, 10))
        elif msg.content.startswith("=math") or msg.content.startswith("=calc") or msg.content.startswith("=calculate") or msg.content.startswith("=maths"):
            if args[1] == "+":
                sumOfNum = int(args[0]) + int(args[2])
                await msg.channel.send('```' + str(sumOfNum) + '```') #theres probably a better way to format these answers
            elif args[1] == "-":
                difference = int(args[0]) - int(args[2])
                await msg.channel.send('```' + str(difference) + '```')
            elif args[1] == "*":
                result = int(args[0]) * int(args[2])
                await msg.channel.send('```' + str(result) + '```')
            elif args[1] == "/":
                quotient = int(args[0]) / int(args[2])
                await msg.channel.send('```' + str(quotient) + '```')
        elif msg.content.startswith("=a"):
            #opens the text document from previous code, stores all confessions in a list
            with open('confessions.txt', 'r') as data:
                data = data.readlines()

            numToApprove = splitMsg.pop(1)
            print("confession #" + numToApprove, "will be approved.")
            confessionChannel = client.get_channel(772794910826430494)
            await confessionChannel.send("Confession received: " + data[int(numToApprove)])
        elif msg.content.startswith('=github'):
            await msg.channel.send("jeuseBot's code can be found at: https://github.com/Meme25327/jeuseBot")
        elif msg.content.startswith('=ftoc'):
            farenheit = float(args[0])
            celsius = str(int((farenheit - 32) * 5/9))
            result = str(farenheit) + " degrees farenheit is equal to " + str(celsius) + " degrees celsius."
            await msg.channel.send(''.join(result))
        elif msg.content.startswith("=ctof"):
            celsius = float(args[0])
            farenheit = str(int((celsius * 9/5) + 32))
            result = str(celsius) + " degrees celsius is equal to " + str(farenheit) + " degrees farenheit"
            msg.channel.send(''.join(result))
        elif msg.content.startswith('= '):
            print("poo")
        else:
            await msg.channel.send('Command not recognized. Try =help!')

client.run(TOKEN)