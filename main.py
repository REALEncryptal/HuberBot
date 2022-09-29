# bot.py
import os
import random
import discord
from discord.ext import commands
TOKEN = "token here"

client = discord.Client()


def listToString(s):
    # initialize an empty string
    str1 = " "

    # return string
    return (str1.join(s))


@client.event
async def on_ready():
    print(f'{client.user.name} has connected to Discord!')

@client.event
async def on_member_join(member):
    await member.create_dm()
    await member.dm_channel.send(
        f'Hi {member.name}, this is hubery bot.'
    )

##-- Character

def createAccount(userId):
    input_dictionary.update({userId: {
        "smortness":[]
    }})

input_dictionary = {}

file = open("Python.txt", "w")
file.write("%s = %s\n" % ("input_dictionary", input_dictionary))

file.close()

f = open('Python.txt', 'r')
if f.mode == 'r':
    contents = f.read()

happiness = 77

characterList = [
    ":warning:**This message contains something dumb, reading is NOT advised**:warning:",
    "bruh",
    "your mama so fat",
    "👹💥💥👹👺👹📉📉💀💥👿👹🔪🔪",
    "your moms a hoe l bozo",
    "https://media.tenor.co/videos/9506ccd5116b9a838145aefd1d3ccef5/mp4",
    "FIGHT ME I DARE YOU",
    "TWHEN THE DUSYET SUSSY SI SO SUSSY MEGA"
]

@client.event
async def on_message(message):
    global happiness

    if message.author.id == 497969149889216542:
        if message.content == "hubery set feelings max":
            happiness = 100

    if not message.author.id == 868555480820228116:

        if random.randint(0,1000) == 1:
            await message.reply(random.choice(characterList))

        if random.randint(0,40) == 1:
            if message.author.id == 630214422018916373:    ### HUBERY
                await message.reply('https://cdn.discordapp.com/emojis/933865784353120296.webp?size=96&quality=lossless')
            elif message.author.id == 761079741927129149:   ### NEO
                await message.reply('https://tenor.com/view/matrix-dodge-neo-gif-13288848')
            if message.author.id == 724893987785277460:   ### AMANDA L BOZO
                await message.reply('Amanda')
        if message.content.startswith("<:hubery:933865784353120296>"):
            split = message.content.lower().split()
            if len(split) > 1:


                if split[1] == "joke":
                    print(random.choice(os.listdir("jokes\\")))
                    await message.reply(file=discord.File("jokes\\"+random.choice(os.listdir("jokes\\"))))

                if split[1] == "schedule":
                    await message.reply(file=discord.File('images/schedule.png'))
                if split[1] == "sus":
                    await message.reply("https://tenor.com/view/sus-suspicious-gif-23068645")
                if split[1] == "deez":
                    await message.reply("nuts")

                if split[1] == "feelings":

                    await message.reply(str(happiness)+"% happy!")

                if split[1] == "your":
                    if random.randint(0,1) == 1:
                        await message.reply("mama is not hot sorry")
                    else:
                        await message.reply("mama is hot")
                if split[1] == "say":
                    if split[2] == "joe":
                        await message.reply("mama")
                    else:
                        await message.reply(listToString(split[2:]))
                if split[1] == "ping":
                    if split[2] == "joe":
                        await message.reply("mama")
                    else:
                        await message.reply("<@&886153269288783923> "+listToString(split[2:]))
        if message.content == "help":
            await message.reply("prefix for this bot is :hubery:   if no worky then ask server owner to add emoji named hubery :)")
        if any(ext in message.content.lower() for ext in ['hubery bot', 'hubebot','huberbot','huberybot']):
            if happiness < 0:
                await message.channel.send("Hubery bot is so depressed his happiness levels are in the negatives! oh and also hes dead so rip")
            elif happiness < 10:
                await message.channel.send("Hubery bot is thinking of permanent sleep if yk what i mean")
            elif happiness < 30:
                await message.channel.send("Hubery bot is feeling depressed.. :(")
            if True:
                if any(ext in message.content.lower() for ext in
                       ["good", "cool", "awesome", "epic", "nice", "not bad", "smart", "pog", "love"]):
                    await message.reply(random.choice([
                        "Thank you dude!",
                        "Thx bro",
                        ":)",
                        "ayyyyy",
                        "lets go",
                        "very pogers m",
                        "agree",
                        "valid",
                        "yes",
                    ]))
                    if random.randint(1, 5) == 1:
                        happiness = happiness + 2
                        print("happiness levels: ", happiness)
                elif any(ext in message.content.lower() for ext in ["bad", "suck", "dumb", "annoy", "trash", "garbage", "awful", "cringe", "dont like", "don't like", "shit"]):
                    await message.reply(random.choice([
                        "say that again bruh",
                        "why doe",
                        "what did you say?",
                        "dam",
                        "😢",
                        "dude that hurts..",
                        "dude..",
                        "why??",
                        "im not that bad",
                        "https://tenor.com/view/stewie-family-guy-die2nite-bitches-gif-4693098",
                        "https://tenor.com/view/somebody-gonna-die-today-kill-psycho-kill-you-knife-gif-16287296",
                        "reminds me of you ngl",
                        "sounds like a you problem",
                        "stop whining",
                        "me? I think you should look in the mirror",
                        "yeah nah",
                        "didnt ask + dont care",
                        "look whose talkin",
                        "i will make you do the dead",
                        "thats not what your mom said",
                        "look at dis dudeeeeeee HAAH",
                        "ok and?",
                        "som body gON DIE today",
                        "you better start running big boi",
                        "694.206.9.420   this you?",
                        "get a job",
                        "your adopted",
                        "you are ooga booga brain l bozo"
                    ]))
                    if random.randint(1,5) == 1:
                        happiness = happiness - 3
                        print("happiness levels: ", happiness)
                else:
                    await message.reply(random.choice([
                        "Heard my name..?",
                        "I heard my name whats up",
                        "what did you say?"
                    ]))
                await message.guild.get_member(client.user.id).edit(nick="huberbot "+str(happiness)+"%")





client.run(TOKEN)
