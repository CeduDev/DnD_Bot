from dotenv import load_dotenv
import os
import random
import re
import discord
import json
from texts import WRONG_DICE_TEXT, UNKNOWN_COMMAND_TEXT, HELP_TEXT
from consts import (
    CHAD_DC,
    DORYC_DC,
    TURKEY_DC,
    DM_DC,
    CHAD,
    DORYC,
    TURKEY,
    ALL_CHARACTERS,
    HELP_COMMAND,
    CAST_DICE_COMMAND,
    GET_CHARACTER_STAT,
    FUNNY1,
    FUNNY2,
    ONE_OR_TWO_DIGIT_REGEX,
)

load_dotenv()  # take environment variables from .env.

intents = discord.Intents.default()
intents.message_content = True

client = discord.Client(intents=intents)


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
    if (
        message_s[0] != CAST_DICE_COMMAND
        or len(message_s) != 2
        or re.search(ONE_OR_TWO_DIGIT_REGEX, message_s[1]) == None
    ):
        return WRONG_DICE_TEXT

    number = int(message_s[1])
    if number not in [4, 6, 8, 9, 12, 20]:
        return WRONG_DICE_TEXT

    return f"Thy magic number is: {random.randint(1, number)}!"


def get_character_stat(message):
    message_s = message.split(" ")
    if (
        message_s[0] != GET_CHARACTER_STAT
        or len(message_s) != 2
        or message_s[1] not in ALL_CHARACTERS
    ):
        return "Nope"

    return parse_character_stats(read_file(f"./characters/{message_s[1]}.txt"))


@client.event
async def on_ready():
    log(f"We have logged in as {client.user}")


@client.event
async def on_message(message):
    if message.author == client.user:
        return

    m = message.content

    print(message.author)

    if m == HELP_COMMAND:
        await message.channel.send(HELP_TEXT)
    elif m.startswith(CAST_DICE_COMMAND):
        await message.channel.send(cast_dice(m))
    elif m.startswith(GET_CHARACTER_STAT):
        await message.channel.send(get_character_stat(m))
    elif m == FUNNY1:
        await message.channel.send("Pippeli hihi")
    elif m == FUNNY2:
        await message.channel.send("Kikkeli hihi")
    elif m == "/ping":
        await message.channel.send("Pong")
    elif not m.startswith("/"):
        return
    else:
        await message.channel.send(UNKNOWN_COMMAND_TEXT)


chad_f = "./characters/chad.txt"
doryc_f = "./characters/doryc.txt"
turkey_f = "./characters/turkey.txt"

chad_dict = read_file(chad_f)
doryc_dict = read_file(doryc_f)
turkey_dict = read_file(turkey_f)


if __name__ == "__main__":
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
