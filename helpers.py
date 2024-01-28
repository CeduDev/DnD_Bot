import json
import sys
from consts import (
    DC_CHAR_DICT,
    DC_BOT_CHANNEL_DICT,
    CHAR_BOT_CHANNEL_DICT,
    STAT_SKILL_ARRAY,
    STAT_ARRAY,
    DEATH_SAVES_ARR,
)
from texts import FORGOT_VALUE_TEXT, OUT_OF_BOUND_DEATH_SAVE


def log(text):
    print("=============== {} ===============".format(text))


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


def is_your_character(author, message_character):
    return DC_CHAR_DICT[author] == message_character


def is_correct_character_stat_channel(interaction, character=""):
    if character == "":
        return interaction.channel.name in DC_BOT_CHANNEL_DICT[interaction.user.name]
    else:
        return (
            interaction.channel.name in DC_BOT_CHANNEL_DICT[interaction.user.name]
            and character == CHAR_BOT_CHANNEL_DICT[interaction.channel.name]
        )


def get_skill(skill: str, character: str, CHAR_FILE_DICT):
    description = list(filter(lambda x: x[0] == skill, STAT_SKILL_ARRAY))[0]

    return f"Behold! The modifier for the skill '{description[1]}' unfolds before thee: {CHAR_FILE_DICT[character]['skills'][skill]}"


# Skill functions


def add_to_skill(skill: str, character: str, CHAR_FILE_DICT, value: int):
    if value == sys.maxsize:
        return FORGOT_VALUE_TEXT
    else:
        description = list(filter(lambda x: x[0] == skill, STAT_SKILL_ARRAY))[0]
        res_value = CHAR_FILE_DICT[character]["skills"][skill] + value
        CHAR_FILE_DICT[character]["skills"][skill] = res_value
        return f"Huzzah! With a triumphant invocation, thou hast successfully added a value of {value} to thy skill '{description[1]}', resulting in {res_value}, weaving newfound prowess into the fabric of thy character's destiny in our digital realm."


def remove_from_skill(skill: str, character: str, CHAR_FILE_DICT, value: int):
    if value == sys.maxsize:
        return FORGOT_VALUE_TEXT
    else:
        description = list(filter(lambda x: x[0] == skill, STAT_SKILL_ARRAY))[0]
        res_value = CHAR_FILE_DICT[character]["skills"][skill] - value
        CHAR_FILE_DICT[character]["skills"][skill] = res_value
        return f"Huzzah! With a triumphant invocation, thou hast successfully removed a value of {value} to thy skill '{description[1]}', resulting in {res_value}, weaving newfound prowess into the fabric of thy character's destiny in our digital realm."


def set_skill(skill: str, character: str, CHAR_FILE_DICT, value: int):
    if value == sys.maxsize:
        return FORGOT_VALUE_TEXT
    else:
        description = list(filter(lambda x: x[0] == skill, STAT_SKILL_ARRAY))[0]
        CHAR_FILE_DICT[character]["skills"][skill] = value
        return f"Huzzah! With a triumphant invocation, thou hast successfully set a value of {value} to thy skill '{description[1]}', weaving newfound prowess into the fabric of thy character's destiny in our digital realm."


# Stat actions


def get_stat(stat: str, character: str, CHAR_FILE_DICT):
    description = list(filter(lambda x: x[0] == stat, STAT_ARRAY))[0]

    return f"Behold! The modifier for the stat '{description[1]}' unfolds before thee: {CHAR_FILE_DICT[character][stat]}"


def add_to_stat(stat: str, character: str, CHAR_FILE_DICT, value: int):
    if value == sys.maxsize:
        return FORGOT_VALUE_TEXT
    else:
        description = list(filter(lambda x: x[0] == stat, STAT_ARRAY))[0]
        res_value = CHAR_FILE_DICT[character][stat] + value
        CHAR_FILE_DICT[character][stat] = res_value
        return f"Huzzah! With a triumphant invocation, thou hast successfully added a value of {value} to thy stat '{description[1]}', resulting in {res_value}, weaving newfound prowess into the fabric of thy character's destiny in our digital realm."


def remove_from_stat(stat: str, character: str, CHAR_FILE_DICT, value: int):
    if value == sys.maxsize:
        return FORGOT_VALUE_TEXT
    else:
        description = list(filter(lambda x: x[0] == stat, STAT_ARRAY))[0]
        res_value = CHAR_FILE_DICT[character][stat] - value
        CHAR_FILE_DICT[character][stat] = res_value
        return f"Huzzah! With a triumphant invocation, thou hast successfully removed a value of {value} to thy stat '{description[1]}', resulting in {res_value}, weaving newfound prowess into the fabric of thy character's destiny in our digital realm."


def set_stat(stat: str, character: str, CHAR_FILE_DICT, value: int):
    if value == sys.maxsize:
        return FORGOT_VALUE_TEXT
    else:
        description = list(filter(lambda x: x[0] == stat, STAT_ARRAY))[0]
        CHAR_FILE_DICT[character][stat] = value
        return f"Huzzah! With a triumphant invocation, thou hast successfully set a value of {value} to thy stat '{description[1]}', weaving newfound prowess into the fabric of thy character's destiny in our digital realm."


# Death save actions


def get_death_save(version: str, character: str, CHAR_FILE_DICT):
    description = list(filter(lambda x: x[0] == version, DEATH_SAVES_ARR))[0]

    return f"Behold! The modifier for the death save '{description[1]}' unfolds before thee: {CHAR_FILE_DICT[character]['death_saves'][version]}"


def add_to_death_save(version: str, character: str, CHAR_FILE_DICT, value: int):
    if value == sys.maxsize:
        return FORGOT_VALUE_TEXT
    else:
        res_value = CHAR_FILE_DICT[character]["death_saves"][version] + value
        if res_value > 3 or res_value < 0:
            return OUT_OF_BOUND_DEATH_SAVE
        description = list(filter(lambda x: x[0] == version, DEATH_SAVES_ARR))[0]
        CHAR_FILE_DICT[character]["death_saves"][version] = res_value
        return f"Huzzah! With a triumphant invocation, thou hast successfully added a value of {value} to thy death save '{description[1]}', resulting in {res_value}, weaving newfound prowess into the fabric of thy character's destiny in our digital realm."


def remove_from_death_save(version: str, character: str, CHAR_FILE_DICT, value: int):
    if value == sys.maxsize:
        return FORGOT_VALUE_TEXT
    else:
        res_value = CHAR_FILE_DICT[character]["death_saves"][version] - value
        if res_value > 3 or res_value < 0:
            return OUT_OF_BOUND_DEATH_SAVE
        description = list(filter(lambda x: x[0] == version, DEATH_SAVES_ARR))[0]
        CHAR_FILE_DICT[character]["death_saves"][version] = res_value
        return f"Huzzah! With a triumphant invocation, thou hast successfully removed a value of {value} to thy death save '{description[1]}', resulting in {res_value}, weaving newfound prowess into the fabric of thy character's destiny in our digital realm."


def set_death_save(version: str, character: str, CHAR_FILE_DICT, value: int):
    if value == sys.maxsize:
        return FORGOT_VALUE_TEXT
    else:
        if value > 3 or value < 0:
            return OUT_OF_BOUND_DEATH_SAVE
        description = list(filter(lambda x: x[0] == version, DEATH_SAVES_ARR))[0]
        CHAR_FILE_DICT[character]["death_saves"][version] = value
        return f"Huzzah! With a triumphant invocation, thou hast successfully set a value of {value} to thy death save '{description[1]}', weaving newfound prowess into the fabric of thy character's destiny in our digital realm."
