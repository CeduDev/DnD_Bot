import json
from consts import DC_CHAR_DICT, DC_BOT_CHANNEL_DICT, STAT_SKILL_ARRAY


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


def is_correct_character_stat_channel(interaction):
    return interaction.channel.name == DC_BOT_CHANNEL_DICT[interaction.user.name]


def get_skill(skill: str, character: str, CHAR_FILE_DICT):
    description = list(filter(lambda x: x[0] == skill, STAT_SKILL_ARRAY))[0]

    return f"Behold! The modifier for the skill '{description[1]}' unfolds before thee: {CHAR_FILE_DICT[character]['skills'][skill]}"


def add_to_skill(skill: str, character: str, CHAR_FILE_DICT):
    print("add")
    print(skill)
    print(character)


def remove_from_skill(skill: str, character: str, CHAR_FILE_DICT):
    print("remove")
    print(skill)
    print(character)


def set_skill(skill: str, character: str, CHAR_FILE_DICT):
    print("set")
    print(skill)
    print(character)
