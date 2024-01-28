from dotenv import load_dotenv
import os
import random
import re
import discord
from discord.ext import commands
from discord import app_commands
from helpers import (
    log,
    read_file,
    write_file,
    parse_character_stats,
    is_your_character,
    is_correct_character_stat_channel,
    get_skill,
    add_to_skill,
    remove_from_skill,
    set_skill,
)
import texts
import consts

load_dotenv()

intents = discord.Intents.default()
intents.message_content = True
client = commands.Bot(command_prefix="/", intents=intents)


@client.tree.command(name="ping", description="Ping pong")
async def ping(interaction: discord.Interaction):
    await interaction.response.send_message("pong")


@client.tree.command(
    name=consts.CAST_DICE_COMMAND,
    description=texts.CAST_DICE_DESCRIPTION,
)
@app_commands.describe(dice="Dice to throw")
@app_commands.choices(
    dice=[
        app_commands.Choice(name="d4", value=4),
        app_commands.Choice(name="d6", value=6),
        app_commands.Choice(name="d8", value=8),
        app_commands.Choice(name="d9", value=9),
        app_commands.Choice(name="d12", value=12),
        app_commands.Choice(name="d20", value=20),
    ]
)
async def cast_dice(interaction: discord.Interaction, dice: int):
    if not is_correct_character_stat_channel(interaction):
        await interaction.response.send_message(texts.INCORRECT_CHANNEL_TEXT)
        return

    await interaction.response.send_message(
        f"Thy magic d{dice} number is: {random.randint(1, dice)}!"
    )


@client.tree.command(
    name=consts.GET_CHARACTER_STAT_COMMAND,
    description=texts.GET_CHARACTER_STAT_DESCRIPTION,
)
@app_commands.describe(character="Character name")
@app_commands.choices(
    character=[
        app_commands.Choice(name=consts.CHAD, value=consts.CHAD),
        app_commands.Choice(name=consts.DORYC, value=consts.DORYC),
        app_commands.Choice(name=consts.TURKEY, value=consts.TURKEY),
    ]
)
async def get_character_stat(interaction: discord.Interaction, character: str):
    if not is_correct_character_stat_channel(interaction):
        await interaction.response.send_message(texts.INCORRECT_CHANNEL_TEXT)
        return

    author = interaction.user.name
    if author != consts.DM_DC and not is_your_character(author, character):
        await interaction.response.send_message(texts.ONLY_DM_TEXT_AND_YOUR_CHARACTER)
        return

    await interaction.response.send_message(
        parse_character_stats(read_file(f"./characters/{character}.txt"))
    )


@client.tree.command(name=consts.SKILL_COMMAND, description=texts.SKILL_DESCRIPTION)
@app_commands.describe(
    action="What action to take",
    skill="Which skill to act on",
    character="Character name",
)
@app_commands.choices(
    action=list(
        map(
            lambda x: app_commands.Choice(name=x[1], value=x[0]),
            consts.ACTION_ARRAY,
        )
    ),
    skill=list(
        map(
            lambda x: app_commands.Choice(name=x[1], value=x[0]),
            consts.STAT_SKILL_ARRAY,
        )
    ),
    character=[
        app_commands.Choice(name=consts.CHAD, value=consts.CHAD),
        app_commands.Choice(name=consts.DORYC, value=consts.DORYC),
        app_commands.Choice(name=consts.TURKEY, value=consts.TURKEY),
    ],
)
async def skill(
    interaction: discord.Interaction, action: str, skill: str, character: str
):
    if not is_correct_character_stat_channel(interaction):
        await interaction.response.send_message(texts.INCORRECT_CHANNEL_TEXT)
        return

    author = interaction.user.name
    if author != consts.DM_DC and not is_your_character(author, character):
        await interaction.response.send_message(texts.ONLY_DM_TEXT_AND_YOUR_CHARACTER)
        return

    if action == consts.GET[0]:
        await interaction.response.send_message(
            get_skill(skill, character, CHAR_FILE_DICT)
        )
    elif action == consts.ADD[0]:
        add_to_skill(skill, character, CHAR_FILE_DICT)
        await interaction.response.send_message("pippeli hihi")
    elif action == consts.REMOVE[0]:
        remove_from_skill(skill, character, CHAR_FILE_DICT)
        await interaction.response.send_message("pippeli hihi")
    elif action == consts.SET[0]:
        set_skill(skill, character, CHAR_FILE_DICT)
        await interaction.response.send_message("pippeli hihi")
    else:
        print("wtf")
        await interaction.response.send_message("pippeli hihi")


@client.tree.command(name=consts.HELP_COMMAND, description=texts.HELP_DESCRIPTION)
async def help(interaction: discord.Interaction):
    await interaction.response.send_message(texts.HELP_TEXT)


@client.tree.command(
    name=consts.FUNNY1_COMMAND,
    description="hihi",
)
async def kikkeli(interaction: discord.Interaction):
    await interaction.response.send_message("pippeli hihi")


@client.tree.command(
    name=consts.FUNNY2_COMMAND,
    description="hihi",
)
async def pippeli(interaction: discord.Interaction):
    await interaction.response.send_message("kikkeli hihi")


# This should only be run when no command was selected from the menu in discord
@client.event
async def on_message(message):
    if message.author == client.user:
        return

    m = message.content

    if not m.startswith("/"):
        return
    else:
        await message.channel.send(texts.UNKNOWN_COMMAND_TEXT)


@client.event
async def on_ready():
    await client.change_presence(status=discord.Status.online)
    await client.tree.sync()
    log(f"We have logged in as {client.user}")


chad_f = "./characters/chad.txt"
doryc_f = "./characters/doryc.txt"
turkey_f = "./characters/turkey.txt"

chad_dict = read_file(chad_f)
doryc_dict = read_file(doryc_f)
turkey_dict = read_file(turkey_f)

CHAR_FILE_DICT = {
    consts.CHAD: chad_dict,
    consts.DORYC: doryc_dict,
    consts.TURKEY: turkey_dict,
}

if __name__ == "__main__":
    log("Successfully read all the character files!")
    log("Running client...")
    client.run(os.getenv("BOT_PASSWORD"))
    log("Bot has stopped, writing files...")
    try:
        write_file(chad_dict, chad_f)
        write_file(doryc_dict, doryc_f)
        write_file(turkey_dict, turkey_f)
        log("Successfully wrote files")
    except:
        log("Failed writing files...")
    log("Shutting down...")
