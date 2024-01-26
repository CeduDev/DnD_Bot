from dotenv import load_dotenv
import os
import random
import re
import discord
import json

load_dotenv()  # take environment variables from .env.

intents = discord.Intents.default()
intents.message_content = True

client = discord.Client(intents=intents)

# Character names
CHAD = "chad"
DORYC = "doryc"
TURKEY = "turkey"
ALL_CHARACTERS = [CHAD, DORYC, TURKEY]

# Commands
HELP_COMMAND = '/help'
CAST_DICE_COMMAND = '/cast_dice'
GET_CHARACTER_STAT = '/get_stats'
FUNNY1 = "/kikkeli"
FUNNY2 = "/pippeli"

# Regexes
ONE_OR_TWO_DIGIT_REGEX = '^\\d{1,2}$'

WRONG_DICE_TEXT = f"""
Ah, valiant seeker, thy attempt to cast the dice with a cryptic value hath summoned the ire of the arcane spirits. Beware, for the forces of the ethereal realm frown upon such mystic insolence.

In the realm of the enchanted dice, only the sacred numerals 4, 6, 8, 9, 12, and 20 may be offered in tribute. The alchemy of a cryptic value is forbidden and confounds the very fabric of the mystical weave.

Reconsider, noble user, and adhere to the sacred incantations. Let not the digits stray into the forbidden territories, lest the dice of destiny withhold their revelations. May the mystical journey ahead be one of compliance and enlightenment.
"""

UNKNOWN_COMMAND_TEXT = f"""
Hail, seeker of the arcane! Thy attempt at an unknown command hath stirred the ethereal winds. Fear not, for guidance lies in the sacred "{HELP_COMMAND}" command, unveiling the secrets of our realm. Let the mystic incantations guide thee, and may the digital ether reveal its wisdom on this path of discovery.
"""

HELP_TEXT = f"""

Greetings, noble user of the arcane arts! Behold the mystic commands at your disposal:

{HELP_COMMAND}:
Ah, ye seeker of wisdom, to unravel the mysteries, invoke this incantation "{HELP_COMMAND}". A scroll of knowledge shall be revealed, unfurling the secrets of our mystical realm to guide thee on thine journey.

{CAST_DICE_COMMAND}:
Venture forth into the unknown with the command "{CAST_DICE_COMMAND}" Craft your fate by providing a single or double-digit offering, forsooth, but beware, for only the digits 4, 6, 8, 9, 12, and 20 are permitted in this sacred chant. May the roll of the enchanted dice shape thy destiny and unveil the path that lies ahead.

May the arcane forces guide you on your quest, and may the digits align in your favor, brave adventurer!
"""

def read_file(file):
    return json.load(open(file))

def write_file(dict_out, file):
    json.dump(dict_out, open(file, "w"))
    return

def parse_character_stats(char_dict):
    return f"""
The stats of {char_dict["name"]} are the following:

Current health: {char_dict["current_hp"]}
Max health: {char_dict["max_hp"]}
Initiative: {char_dict["initiative"]}
Armor class: {char_dict["armor_class"]}
    """

def log(text):
    print("=============== {} ===============".format(text))

def cast_dice(message):
    message_s = message.split(" ")
    if message_s[0] != CAST_DICE_COMMAND or len(message_s) != 2 or re.search(ONE_OR_TWO_DIGIT_REGEX, message_s[1]) == None: return WRONG_DICE_TEXT

    number = int(message_s[1])
    if number not in [4, 6, 8, 9, 12, 20]:
        return WRONG_DICE_TEXT
    
    return f'Thy magic number is: {random.randint(1, number)}!'

def get_character_stat(message):
    message_s = message.split(" ")
    if message_s[0] != GET_CHARACTER_STAT or len(message_s) != 2 or message_s[1] not in ALL_CHARACTERS: return "Nope"

    return parse_character_stats(read_file(f'./characters/{message_s[1]}.txt'))

@client.event
async def on_ready():
    log(f'We have logged in as {client.user}')

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    m = message.content

    if m == HELP_COMMAND: await message.channel.send(HELP_TEXT)
    elif m.startswith(CAST_DICE_COMMAND): await message.channel.send(cast_dice(m))
    elif m.startswith(GET_CHARACTER_STAT): await message.channel.send(get_character_stat(m))
    elif m == FUNNY1: await message.channel.send("Pippeli hihi")
    elif m == FUNNY2: await message.channel.send("Kikkeli hihi")
    elif not m.startswith("/"): return
    else: await message.channel.send(UNKNOWN_COMMAND_TEXT)

chad_f = "./characters/chad.txt"
doryc_f = "./characters/doryc.txt"
turkey_f = "./characters/turkey.txt"

chad_dict = read_file(chad_f)
doryc_dict = read_file(doryc_f)
turkey_dict = read_file(turkey_f)


if __name__ == '__main__':    
    log("Successfully read all the character files!")
    log("Running client...")
    client.run(os.getenv("BOT_PASSWORD"))
    log("Bot has stopped, writing files...")
    try:
        write_file(chad_dict, chad_f)
        write_file(doryc_dict, doryc_f)
        write_file(turkey_dict, turkey_f)
    except:
        log("Failed writing files...")
    log("Shutting down...")
