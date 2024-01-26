from dotenv import load_dotenv
import os
import random
import re
import discord

load_dotenv()  # take environment variables from .env.

intents = discord.Intents.default()
intents.message_content = True

client = discord.Client(intents=intents)

HELP_COMMAND = '/help'
CAST_DICE_COMMAND = '/cast_dice'
ONE_OR_TWO_DIGIT_REGEX = '^\\d{1,2}$'
FUNNY1 = "/kikkeli"
FUNNY2 = "/pippeli"

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

def cast_dice(message):
    message_s = message.split(" ")
    if message_s[0] != CAST_DICE_COMMAND or len(message_s) != 2 or re.search(ONE_OR_TWO_DIGIT_REGEX, message_s[1]) == None: return WRONG_DICE_TEXT

    number = int(message_s[1])
    if number not in [4, 6, 8, 9, 12, 20]:
        return WRONG_DICE_TEXT
    
    return f'Thy magic number is: {random.randint(1, number)}!' 


@client.event
async def on_ready():
    print(f'We have logged in as {client.user}')

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    m = message.content

    if m == HELP_COMMAND: await message.channel.send(HELP_TEXT)
    elif m.startswith(CAST_DICE_COMMAND): await message.channel.send(cast_dice(m))
    elif m == FUNNY1: await message.channel.send("Pippeli hihi")
    elif m == FUNNY2: await message.channel.send("Kikkeli hihi")
    elif not m.startswith("/"): return
    else: await message.channel.send(UNKNOWN_COMMAND_TEXT)
        

client.run(os.getenv("BOT_PASSWORD"))
