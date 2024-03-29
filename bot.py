from dotenv import load_dotenv
import os
import random
import re
import discord
from discord.ext import commands
from discord import app_commands
from discord.app_commands import Choice
import helpers
import texts
import consts
import typing
import sys

load_dotenv()

intents = discord.Intents.default()
intents.message_content = True
client = commands.Bot(command_prefix="/", intents=intents)


@client.tree.command(name="ping", description="Ping pong")
async def ping(interaction: discord.Interaction):
    await interaction.response.send_message("pong")


# TODO! Add functionality attack dice (needs weapon inventory)
@client.tree.command(
    name=consts.CAST_DICE_COMMAND_GENERAL,
    description=texts.CAST_DICE_DESCRIPTION_GENERAL,
)
@app_commands.describe(dice="Dice to throw")
@app_commands.choices(
    dice=[
        Choice(name="d2", value=2),
        Choice(name="d4", value=4),
        Choice(name="d6", value=6),
        Choice(name="d8", value=8),
        Choice(name="d9", value=9),
        Choice(name="d12", value=12),
        Choice(name="d20", value=20),
    ]
)
async def cast_dice(interaction: discord.Interaction, dice: int):
    if not helpers.is_correct_character_stat_channel(interaction):
        await interaction.response.send_message(texts.INCORRECT_CHANNEL_TEXT)
        return

    await interaction.response.send_message(helpers.throw_general(dice))


@client.tree.command(
    name=consts.CAST_DICE_COMMAND_SAVING,
    description=texts.CAST_DICE_DESCRIPTION_SAVING,
)
@app_commands.describe(
    saving_type="Which type you throw for", character="Character name"
)
@app_commands.choices(
    saving_type=list(
        map(
            lambda x: Choice(name=x[1], value=x[0]),
            consts.SAVING_THROW_ARRAY,
        )
    ),
    character=[
        Choice(name=consts.CHAD, value=consts.CHAD),
        Choice(name=consts.DORYC, value=consts.DORYC),
        Choice(name=consts.TURKEY, value=consts.TURKEY),
    ],
)
async def cast_dice_saving(
    interaction: discord.Interaction, saving_type: str, character: str
):
    author = interaction.user.name
    if author != consts.DM_DC and not helpers.is_your_character(author, character):
        await interaction.response.send_message(texts.ONLY_DM_TEXT_AND_YOUR_CHARACTER)
        return

    await interaction.response.send_message(
        helpers.throw_saving(saving_type, character, CHAR_FILE_DICT)
    )


@client.tree.command(
    name=consts.CAST_DICE_COMMAND_SKILL,
    description=texts.CAST_DICE_DESCRIPTION_SKILL,
)
@app_commands.describe(skill="What skill to throw with", character="Character name")
@app_commands.choices(
    skill=list(
        map(
            lambda x: Choice(name=x[1], value=x[0]),
            consts.STAT_SKILL_ARRAY,
        )
    ),
    character=[
        Choice(name=consts.CHAD, value=consts.CHAD),
        Choice(name=consts.DORYC, value=consts.DORYC),
        Choice(name=consts.TURKEY, value=consts.TURKEY),
    ],
)
async def cast_dice_skill(interaction: discord.Interaction, skill: str, character: str):
    author = interaction.user.name
    if author != consts.DM_DC and not helpers.is_your_character(author, character):
        await interaction.response.send_message(texts.ONLY_DM_TEXT_AND_YOUR_CHARACTER)
        return

    await interaction.response.send_message(
        helpers.throw_skill(skill, character, CHAR_FILE_DICT)
    )


@client.tree.command(
    name=consts.CAST_DICE_COMMAND_DEATH_SAVE,
    description=texts.CAST_DICE_DESCRIPTION_DEATH_SAVE,
)
@app_commands.describe(character="Character name")
@app_commands.choices(
    character=[
        Choice(name=consts.CHAD, value=consts.CHAD),
        Choice(name=consts.DORYC, value=consts.DORYC),
        Choice(name=consts.TURKEY, value=consts.TURKEY),
    ],
)
async def cast_dice_death_save(interaction: discord.Interaction, character: str):
    author = interaction.user.name
    if author != consts.DM_DC and not helpers.is_your_character(author, character):
        await interaction.response.send_message(texts.ONLY_DM_TEXT_AND_YOUR_CHARACTER)
        return
    res = helpers.throw_death_save(character, CHAR_FILE_DICT)
    helpers.write_file(CHAR_FILE_DICT[character], CHAR_FILE[character])
    await interaction.response.send_message(res)


@client.tree.command(
    name=consts.GET_CHARACTER_STAT_COMMAND,
    description=texts.GET_CHARACTER_STAT_DESCRIPTION,
)
@app_commands.describe(character="Character name")
@app_commands.choices(
    character=[
        Choice(name=consts.CHAD, value=consts.CHAD),
        Choice(name=consts.DORYC, value=consts.DORYC),
        Choice(name=consts.TURKEY, value=consts.TURKEY),
    ]
)
async def get_character_stat(interaction: discord.Interaction, character: str):
    if not helpers.is_correct_character_stat_channel(interaction, character):
        await interaction.response.send_message(texts.INCORRECT_CHANNEL_TEXT)
        return

    author = interaction.user.name
    if author != consts.DM_DC and not helpers.is_your_character(author, character):
        await interaction.response.send_message(texts.ONLY_DM_TEXT_AND_YOUR_CHARACTER)
        return

    await interaction.response.send_message(
        helpers.parse_character_stats(
            helpers.read_file(f"./characters/{character}.json")
        )
    )


@client.tree.command(name=consts.STAT_COMMAND, description=texts.STAT_DESCRIPTION)
@app_commands.describe(
    action="What action to take",
    stat="Which stat to act on",
    character="Character name",
    value="Value to act with",
)
@app_commands.choices(
    action=list(
        map(
            lambda x: Choice(name=x[1], value=x[0]),
            consts.ACTION_ARRAY,
        )
    ),
    stat=list(
        map(
            lambda x: Choice(name=x[1], value=x[0]),
            consts.STAT_ARRAY,
        )
    ),
    character=[
        Choice(name=consts.CHAD, value=consts.CHAD),
        Choice(name=consts.DORYC, value=consts.DORYC),
        Choice(name=consts.TURKEY, value=consts.TURKEY),
    ],
)
async def stat(
    interaction: discord.Interaction,
    action: str,
    stat: str,
    character: str,
    value: typing.Optional[int] = sys.maxsize,
):
    if not helpers.is_correct_character_stat_channel(interaction, character):
        await interaction.response.send_message(texts.INCORRECT_CHANNEL_TEXT)
        return

    author = interaction.user.name
    if author != consts.DM_DC and not helpers.is_your_character(author, character):
        await interaction.response.send_message(texts.ONLY_DM_TEXT_AND_YOUR_CHARACTER)
        return

    if action == consts.GET[0]:
        await interaction.response.send_message(
            helpers.get_stat(stat, character, CHAR_FILE_DICT)
        )
    elif action == consts.ADD[0]:
        res = helpers.add_to_stat(stat, character, CHAR_FILE_DICT, value)
        helpers.write_file(CHAR_FILE_DICT[character], CHAR_FILE[character])
        await interaction.response.send_message(res)
    elif action == consts.REMOVE[0]:
        res = helpers.remove_from_stat(stat, character, CHAR_FILE_DICT, value)
        helpers.write_file(CHAR_FILE_DICT[character], CHAR_FILE[character])
        await interaction.response.send_message(res)
    elif action == consts.SET[0]:
        res = helpers.set_stat(stat, character, CHAR_FILE_DICT, value)
        helpers.write_file(CHAR_FILE_DICT[character], CHAR_FILE[character])
        await interaction.response.send_message(res)
    else:
        await interaction.response.send_message("wtf")


@client.tree.command(name=consts.SKILL_COMMAND, description=texts.SKILL_DESCRIPTION)
@app_commands.describe(
    action="What action to take",
    skill="Which skill to act on",
    character="Character name",
    value="Value to act with",
)
@app_commands.choices(
    action=list(
        map(
            lambda x: Choice(name=x[1], value=x[0]),
            consts.ACTION_ARRAY,
        )
    ),
    skill=list(
        map(
            lambda x: Choice(name=x[1], value=x[0]),
            consts.STAT_SKILL_ARRAY,
        )
    ),
    character=[
        Choice(name=consts.CHAD, value=consts.CHAD),
        Choice(name=consts.DORYC, value=consts.DORYC),
        Choice(name=consts.TURKEY, value=consts.TURKEY),
    ],
)
async def skill(
    interaction: discord.Interaction,
    action: str,
    skill: str,
    character: str,
    value: typing.Optional[int] = sys.maxsize,
):
    if not helpers.is_correct_character_stat_channel(interaction, character):
        await interaction.response.send_message(texts.INCORRECT_CHANNEL_TEXT)
        return

    author = interaction.user.name
    if author != consts.DM_DC and not helpers.is_your_character(author, character):
        await interaction.response.send_message(texts.ONLY_DM_TEXT_AND_YOUR_CHARACTER)
        return

    if action == consts.GET[0]:
        await interaction.response.send_message(
            helpers.get_skill(skill, character, CHAR_FILE_DICT)
        )
    elif action == consts.ADD[0]:
        res = helpers.add_to_skill(skill, character, CHAR_FILE_DICT, value)
        helpers.write_file(CHAR_FILE_DICT[character], CHAR_FILE[character])
        await interaction.response.send_message(res)
    elif action == consts.REMOVE[0]:
        res = helpers.remove_from_skill(skill, character, CHAR_FILE_DICT, value)
        helpers.write_file(CHAR_FILE_DICT[character], CHAR_FILE[character])
        await interaction.response.send_message(res)
    elif action == consts.SET[0]:
        res = helpers.set_skill(skill, character, CHAR_FILE_DICT, value)
        helpers.write_file(CHAR_FILE_DICT[character], CHAR_FILE[character])
        await interaction.response.send_message(res)
    else:
        await interaction.response.send_message("wtf")


@client.tree.command(
    name=consts.DEATH_SAVES_COMMAND, description=texts.DEATH_SAVES_DESCRIPTION
)
@app_commands.describe(
    action="What action to take",
    version="Which version to act on",
    character="Character name",
    value="Value to act with",
)
@app_commands.choices(
    action=list(
        map(
            lambda x: Choice(name=x[1], value=x[0]),
            consts.ACTION_ARRAY,
        )
    ),
    version=list(
        map(
            lambda x: Choice(name=x[1], value=x[0]),
            consts.DEATH_SAVES_ARR,
        )
    ),
    character=[
        Choice(name=consts.CHAD, value=consts.CHAD),
        Choice(name=consts.DORYC, value=consts.DORYC),
        Choice(name=consts.TURKEY, value=consts.TURKEY),
    ],
    value=[
        Choice(name=0, value=0),
        Choice(name=1, value=1),
        Choice(name=2, value=2),
        Choice(name=3, value=3),
    ],
)
async def death_saves(
    interaction: discord.Interaction,
    action: str,
    version: str,
    character: str,
    value: typing.Optional[int] = sys.maxsize,
):
    if not helpers.is_correct_character_stat_channel(interaction, character):
        await interaction.response.send_message(texts.INCORRECT_CHANNEL_TEXT)
        return

    author = interaction.user.name
    if author != consts.DM_DC and not helpers.is_your_character(author, character):
        await interaction.response.send_message(texts.ONLY_DM_TEXT_AND_YOUR_CHARACTER)
        return

    if action == consts.GET[0]:
        await interaction.response.send_message(
            helpers.get_death_save(version, character, CHAR_FILE_DICT)
        )
    elif action == consts.ADD[0]:
        res = helpers.add_to_death_save(version, character, CHAR_FILE_DICT, value)
        helpers.write_file(CHAR_FILE_DICT[character], CHAR_FILE[character])
        await interaction.response.send_message(res)
    elif action == consts.REMOVE[0]:
        res = helpers.remove_from_death_save(version, character, CHAR_FILE_DICT, value)
        helpers.write_file(CHAR_FILE_DICT[character], CHAR_FILE[character])
        await interaction.response.send_message(res)
    elif action == consts.SET[0]:
        res = helpers.set_death_save(version, character, CHAR_FILE_DICT, value)
        helpers.write_file(CHAR_FILE_DICT[character], CHAR_FILE[character])
        await interaction.response.send_message(res)
    else:
        await interaction.response.send_message("wtf")


@client.tree.command(
    name=consts.SAVING_THROWS_COMMAND, description=texts.SAVING_THROWS_DESCRIPTION
)
@app_commands.describe(
    action="What action to take",
    saving_throw="Which saving throw to act on",
    character="Character name",
    value="Value to act with",
)
@app_commands.choices(
    action=list(
        map(
            lambda x: Choice(name=x[1], value=x[0]),
            consts.ACTION_ARRAY,
        )
    ),
    saving_throw=list(
        map(
            lambda x: Choice(name=x[1], value=x[0]),
            consts.SAVING_THROW_ARRAY,
        )
    ),
    character=[
        Choice(name=consts.CHAD, value=consts.CHAD),
        Choice(name=consts.DORYC, value=consts.DORYC),
        Choice(name=consts.TURKEY, value=consts.TURKEY),
    ],
)
async def saving_throw(
    interaction: discord.Interaction,
    action: str,
    saving_throw: str,
    character: str,
    value: typing.Optional[int] = sys.maxsize,
):
    if not helpers.is_correct_character_stat_channel(interaction, character):
        await interaction.response.send_message(texts.INCORRECT_CHANNEL_TEXT)
        return

    author = interaction.user.name
    if author != consts.DM_DC and not helpers.is_your_character(author, character):
        await interaction.response.send_message(texts.ONLY_DM_TEXT_AND_YOUR_CHARACTER)
        return

    if action == consts.GET[0]:
        await interaction.response.send_message(
            helpers.get_saving_throw(saving_throw, character, CHAR_FILE_DICT)
        )
    elif action == consts.ADD[0]:
        res = helpers.add_to_saving_throw(
            saving_throw, character, CHAR_FILE_DICT, value
        )
        helpers.write_file(CHAR_FILE_DICT[character], CHAR_FILE[character])
        await interaction.response.send_message(res)
    elif action == consts.REMOVE[0]:
        res = helpers.remove_from_saving_throw(
            saving_throw, character, CHAR_FILE_DICT, value
        )
        helpers.write_file(CHAR_FILE_DICT[character], CHAR_FILE[character])
        await interaction.response.send_message(res)
    elif action == consts.SET[0]:
        res = helpers.set_saving_throw(saving_throw, character, CHAR_FILE_DICT, value)
        helpers.write_file(CHAR_FILE_DICT[character], CHAR_FILE[character])
        await interaction.response.send_message(res)
    else:
        await interaction.response.send_message("wtf")


@client.tree.command(
    name=consts.ABILITY_SCORE_COMMAND, description=texts.ABILITY_SCORE_DESCRIPTION
)
@app_commands.describe(
    action="What action to take",
    ability_score="Which ability score to act on",
    base_or_modifier="Act on base or modifier",
    character="Character name",
    value="Value to act with",
)
@app_commands.choices(
    action=list(
        map(
            lambda x: Choice(name=x[1], value=x[0]),
            consts.ACTION_ARRAY,
        )
    ),
    ability_score=list(
        map(
            lambda x: Choice(name=x[1], value=x[0]),
            consts.ABILITY_SCORE_ARRAY,
        )
    ),
    base_or_modifier=[
        Choice(
            name=consts.STAT_ABILITY_SCORE_BASE[1],
            value=consts.STAT_ABILITY_SCORE_BASE[0],
        ),
        Choice(
            name=consts.STAT_ABILITY_SCORE_MODIFIER[1],
            value=consts.STAT_ABILITY_SCORE_MODIFIER[0],
        ),
    ],
    character=[
        Choice(name=consts.CHAD, value=consts.CHAD),
        Choice(name=consts.DORYC, value=consts.DORYC),
        Choice(name=consts.TURKEY, value=consts.TURKEY),
    ],
)
async def ability_score(
    interaction: discord.Interaction,
    action: str,
    ability_score: str,
    base_or_modifier: str,
    character: str,
    value: typing.Optional[int] = sys.maxsize,
):
    if not helpers.is_correct_character_stat_channel(interaction, character):
        await interaction.response.send_message(texts.INCORRECT_CHANNEL_TEXT)
        return

    author = interaction.user.name
    if author != consts.DM_DC and not helpers.is_your_character(author, character):
        await interaction.response.send_message(texts.ONLY_DM_TEXT_AND_YOUR_CHARACTER)
        return

    if action == consts.GET[0]:
        await interaction.response.send_message(
            helpers.get_ability_score(
                ability_score, base_or_modifier, character, CHAR_FILE_DICT
            )
        )
    elif action == consts.ADD[0]:
        res = helpers.add_to_ability_score(
            ability_score, base_or_modifier, character, CHAR_FILE_DICT, value
        )
        helpers.write_file(CHAR_FILE_DICT[character], CHAR_FILE[character])
        await interaction.response.send_message(res)
    elif action == consts.REMOVE[0]:
        res = helpers.remove_from_ability_score(
            ability_score, base_or_modifier, character, CHAR_FILE_DICT, value
        )
        helpers.write_file(CHAR_FILE_DICT[character], CHAR_FILE[character])
        await interaction.response.send_message(res)
    elif action == consts.SET[0]:
        res = helpers.set_ability_score(
            ability_score, base_or_modifier, character, CHAR_FILE_DICT, value
        )
        helpers.write_file(CHAR_FILE_DICT[character], CHAR_FILE[character])
        await interaction.response.send_message(res)
    else:
        await interaction.response.send_message("wtf")


# TODO! Add command for inventory (how to get a dynamic list of items to choice in the UI?)


@client.tree.command(name=consts.HELP_COMMAND, description=texts.HELP_DESCRIPTION)
async def help(interaction: discord.Interaction):
    await interaction.response.send_message(texts.HELP_TEXT1)
    await interaction.followup.send(texts.HELP_TEXT2)
    await interaction.followup.send(texts.HELP_TEXT3)


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
    helpers.log(f"We have logged in as {client.user}")


chad_f = "./characters/chad.json"
doryc_f = "./characters/doryc.json"
turkey_f = "./characters/turkey.json"

chad_dict = helpers.read_file(chad_f)
doryc_dict = helpers.read_file(doryc_f)
turkey_dict = helpers.read_file(turkey_f)

CHAR_FILE_DICT = {
    consts.CHAD: chad_dict,
    consts.DORYC: doryc_dict,
    consts.TURKEY: turkey_dict,
}

CHAR_FILE = {
    consts.CHAD: chad_f,
    consts.DORYC: doryc_f,
    consts.TURKEY: turkey_f,
}

if __name__ == "__main__":
    helpers.log("Successfully read all the character files!")
    helpers.log("Running client...")
    client.run(os.getenv("BOT_PASSWORD"))
    helpers.log("Bot has stopped, writing files...")
    try:
        helpers.write_file(chad_dict, chad_f)
        helpers.write_file(doryc_dict, doryc_f)
        helpers.write_file(turkey_dict, turkey_f)
        helpers.log("Successfully wrote files")
    except:
        helpers.log("Failed writing files...")
    helpers.log("Shutting down...")
