from dotenv import load_dotenv
import os
import random
import re
import discord
from discord.ext import commands
from discord import app_commands
from helpers import log, read_file, write_file, parse_character_stats, is_your_character
from texts import (
    CAST_DICE_DESCRIPTION,
    UNKNOWN_COMMAND_TEXT,
    HELP_TEXT,
    ONLY_DM_TEXT_AND_YOUR_CHARACTER,
    GET_CHARACTER_STAT_DESCRIPTION,
    HELP_DESCRIPTION,
)
from consts import (
    DM_DC,
    CHAD,
    DORYC,
    TURKEY,
    HELP_COMMAND,
    CAST_DICE_COMMAND,
    GET_CHARACTER_STAT_COMMAND,
    FUNNY1_COMMAND,
    FUNNY2_COMMAND,
)

load_dotenv()

intents = discord.Intents.default()
intents.message_content = True
client = commands.Bot(command_prefix="/", intents=intents)


@client.tree.command(name="ping", description="Ping pong")
async def ping(interaction: discord.Interaction):
    await interaction.response.send_message("pong")


@client.tree.command(
    name=CAST_DICE_COMMAND,
    description=CAST_DICE_DESCRIPTION,
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
    await interaction.response.send_message(
        f"Thy magic d{dice} number is: {random.randint(1, dice)}!"
    )


@client.tree.command(
    name=GET_CHARACTER_STAT_COMMAND,
    description=GET_CHARACTER_STAT_DESCRIPTION,
)
@app_commands.describe(character="Character name")
@app_commands.choices(
    character=[
        app_commands.Choice(name=CHAD, value=CHAD),
        app_commands.Choice(name=DORYC, value=DORYC),
        app_commands.Choice(name=TURKEY, value=TURKEY),
    ]
)
async def get_character_stat(interaction: discord.Interaction, character: str):
    author = interaction.user.name
    if author != DM_DC and not is_your_character(author, character):
        await interaction.response.send_message(ONLY_DM_TEXT_AND_YOUR_CHARACTER)
        return

    await interaction.response.send_message(
        parse_character_stats(read_file(f"./characters/{character}.txt"))
    )


@client.tree.command(name=HELP_COMMAND, description=HELP_DESCRIPTION)
async def help(interaction: discord.Interaction):
    await interaction.response.send_message(HELP_TEXT)


@client.tree.command(
    name=FUNNY1_COMMAND,
    description="hihi",
)
async def kikkeli(interaction: discord.Interaction):
    await interaction.response.send_message("pippeli hihi")


@client.tree.command(
    name=FUNNY2_COMMAND,
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
        await message.channel.send(UNKNOWN_COMMAND_TEXT)


@client.event
async def on_ready():
    await client.change_presence(status=discord.Status.online)
    await client.tree.sync()
    log(f"We have logged in as {client.user}")


if __name__ == "__main__":
    chad_f = "./characters/chad.txt"
    doryc_f = "./characters/doryc.txt"
    turkey_f = "./characters/turkey.txt"

    chad_dict = read_file(chad_f)
    doryc_dict = read_file(doryc_f)
    turkey_dict = read_file(turkey_f)

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
